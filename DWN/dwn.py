from datetime import datetime
import os
import logging
import time
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from sklearn.model_selection import train_test_split
import torch
from torchwnn.encoding import DistributiveThermometer, GaussianThermometer, Thermometer
from embeddings import ScatterCode
from utils import (
    add_header,
    binarize,
    create_encoder,
    get_min_max,
    load_mnist,
    load_from_uci,
    to_tensor,
    encode_labels,
)
from torch import nn
import torch_dwn as dwn
from torch.nn.functional import cross_entropy
from codecarbon import EmissionsTracker

log_file = os.path.join(os.path.dirname(__file__), "dwn.log")

logging.basicConfig(
    level=logging.INFO,
    format="[DWN] - %(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)


class DWN(object):

    num_slices: str
    num_dimensions: str
    num_bits_thermometer: str
    encoder_definitions: list
    datasets: list
    csv_file: str
    epochs: int
    repeat_times: int
    device: str
    batch_size: int
    current_dataset: str
    scatter_code: bool

    def __init__(
        self,
        num_slices,
        num_dimensions,
        num_bits_thermometer,
        datasets,
        times=10,
        epochs=10,
        batch_size=32,
        scatter_code=False,
    ):
        self.num_slices = num_slices
        self.num_dimensions = num_dimensions
        self.num_bits_thermometer = num_bits_thermometer
        self.datasets = datasets
        self.repeat_times = times
        self.epochs = epochs
        self.batch_size = batch_size
        self.current_dataset = ""
        self.scatter_code = scatter_code

        if self.scatter_code:
            self.encoder_definitions = [("Scatter Code", ScatterCode)]
        else:
            self.encoder_definitions = [
                ("Distributive", DistributiveThermometer),
                ("Gaussian", GaussianThermometer),
                ("Linear", Thermometer),
            ]

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.csv_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            f"metrics.csv",
        )

    def run(self):
        for dataset in self.datasets:

            self.num_bits_thermometer = dataset.get("num_bits_thermometer", 10)
            self.address_size = dataset.get("address_size", 10)
            dataset_id = dataset["id"]

            self.execute_dataset(dataset_id)

    def execute_dataset(self, dataset_id):

        logging.info(
            f"Processing dataset ID: {dataset_id}, num_slices: {self.num_slices}, num_dimensions: {self.num_dimensions}"
        )

        if dataset_id == "MNIST":
            X, y, name = load_mnist()
        else:
            X, y, name = load_from_uci(dataset_id)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.33, random_state=42
        )

        y_train = encode_labels(y_train)
        y_test = encode_labels(y_test)

        self.current_dataset = name
        min_global, max_global = get_min_max(X)
        torch_tensor = to_tensor(X)

        encoders = [
            create_encoder(
                encoding_type,
                encoder_class,
                self.num_bits_thermometer,
                torch_tensor,
                min_global,
                max_global,
                self.num_slices,
                self.num_dimensions,
            )
            for encoding_type, encoder_class in self.encoder_definitions
        ]

        for encoder in encoders:
            logging.info(
                f"Starting evaluation for encoder: {encoder['encoding']} of dataset {name} with ID: {dataset_id}, num_slices: {self.num_slices}, num_dimensions: {self.num_dimensions}"
            )

            # X_bin = binarize(encoder, X)
            X_train_bin = binarize(encoder, X_train)
            X_test_bin = binarize(encoder, X_test)

            self.evaluate_model(X_train_bin, y_train, X_test_bin, y_test, encoder)

        logging.info(f"Finished processing dataset: {name} with ID: {dataset_id}")

    def evaluate_model(self, x_train, y_train, X_test, y_test, encoder):

        logging.info(
            f"Evaluating model with encoder: {encoder['encoding']}, num_slices: {self.num_slices}, num_dimensions: {self.num_dimensions}"
        )

        all_labels = torch.cat([y_train, y_test])

        num_classes = len(torch.unique(all_labels))

        for i in range(self.repeat_times):

            total_training_time = 0
            total_testing_time = 0

            model = nn.Sequential(
                dwn.LUTLayer(x_train.size(1), 64, n=6, mapping="learnable"),
                dwn.LUTLayer(64, 64, n=6),
                dwn.GroupSum(k=num_classes, tau=1 / 0.3),
            )

            model = model.cuda()
            optimizer = torch.optim.Adam(model.parameters(), lr=1e-2)
            scheduler = torch.optim.lr_scheduler.StepLR(
                optimizer, gamma=0.1, step_size=14
            )

            n_samples = x_train.shape[0]
            accuracies = []
            
            for epoch in range(self.epochs):

                training_time = time.time()
                model.train()
                elapsed_training_time = time.time() - training_time

                total_training_time += elapsed_training_time

                permutation = torch.randperm(n_samples)
                correct_train = 0
                total_train = 0

                for i in range(0, n_samples, self.batch_size):
                    optimizer.zero_grad()

                    indices = permutation[i : i + self.batch_size]
                    batch_x, batch_y = (
                        x_train[indices].cuda(self.device).float(),
                        y_train[indices].cuda(self.device),
                    )

                    outputs = model(batch_x)
                    loss = cross_entropy(outputs, batch_y)
                    loss.backward()
                    optimizer.step()

                    pred_train = outputs.argmax(dim=1)
                    correct_train += (pred_train == batch_y).sum().item()
                    total_train += batch_y.size(0)

                train_acc = correct_train / total_train
                scheduler.step()

                testing_time = time.time()
                test_acc = self.evaluate(model, X_test.float(), y_test.float())
                elapsed_testing_time = time.time() - testing_time
                total_testing_time += elapsed_testing_time

                accuracy = f"{test_acc:.4f}"
                accuracies.append(f"{test_acc:.4f}")

                logging.info(
                    f"Epoch {epoch + 1}/{self.epochs}, Train Loss: {loss.item():.4f}, Train Accuracy: {train_acc:.4f}, Test Accuracy: {test_acc:.4f}"
                )

            # avg_accuracy = sum([float(a) for a in accuracies]) / len(accuracies)

                if epoch == self.epochs - 1:
                    logging.info(
                        f"Final Test Accuracy after {self.epochs} epochs: {test_acc:.4f}"
                    ) 

                    new_row = pd.DataFrame(
                        {
                            "model": ["DWN"],
                            "time": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                            "training_time": [f"{total_training_time:.4f}"],
                            "testing_time": [f"{total_testing_time:.4f}"],
                            "delta_time": [f"{total_training_time + total_testing_time:.4f}"],
                            "dataset": [self.current_dataset],
                            "encoding": [encoder["encoding"]],
                            "num_slices": [
                                self.num_slices if encoder["encoding"] == "Scatter Code" else "0"
                            ],
                            "num_dimensions": [
                                (
                                    self.num_dimensions
                                    if encoder["encoding"] == "Scatter Code"
                                    else "0"
                                )
                            ],
                            "accuracy": [f"{test_acc:.4f}"],
                        },
                        columns=[
                            "model",
                            "time",
                            "training_time",
                            "testing_time",
                            "delta_time",
                            "dataset",
                            "encoding",
                            "num_slices",
                            "num_dimensions",
                            "accuracy",
                        ],
                    )

                    new_row.to_csv(
                        self.csv_file,
                        mode="a",
                        index=False,
                        header=add_header(self.csv_file),
                    )

    def evaluate(self, model, x_test, y_test, device="cuda"):
        model.eval()
        with torch.no_grad():
            pred = (model(x_test.cuda(device)).cpu()).argmax(dim=1).numpy()
            acc = (pred == y_test.numpy()).sum() / y_test.shape[0]
        return acc
