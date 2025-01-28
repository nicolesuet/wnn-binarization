import os
import threading
import numpy as np
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
)
from sklearn.model_selection import train_test_split
import wisardpkg as wp
from torchwnn.encoding import DistributiveThermometer, GaussianThermometer, Thermometer
from datetime import datetime
import pandas as pd
from embeddings import ScatterCode
import logging
import time
from utils import (
    add_header,
    create_encoder,
    get_min_max,
    load_from_uci,
    load_mnist,
    binarize,
    to_tensor,
    to_int_list,
    to_list,
    prepare_labels,
    encode_labels,
)
import torch
from concurrent.futures import ThreadPoolExecutor, as_completed


class Wisard(object):

    num_slices: str
    num_dimensions: str
    address_size: str
    ignore_zero: str
    verbose: str
    num_bits_thermometer: str
    encoder_definitions: list
    datasets_ids: list
    csv_file: str
    epochs: int
    current_dataset: str
    current_dataset_id: str

    def __init__(
        self,
        num_slices,
        num_dimensions,
        address_size,
        ignore_zero,
        verbose,
        num_bits_thermometer,
        datasets_ids,
        epochs=1,
    ):
        self.num_slices = num_slices
        self.num_dimensions = num_dimensions
        self.address_size = address_size
        self.ignore_zero = ignore_zero
        self.verbose = verbose
        self.num_bits_thermometer = num_bits_thermometer
        self.datasets_ids = datasets_ids
        self.epochs = epochs

        self.encoder_definitions = [
            ("Distributive", DistributiveThermometer),
            ("Gaussian", GaussianThermometer),
            ("Linear", Thermometer),
            ("Scatter Code", ScatterCode),
        ]

        self.csv_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            f"metrics.csv",
        )

    def evaluate_model(self, x_train, X_bin, y_train, y_true, encoder):

        wsd = wp.Wisard(
            self.address_size, ignoreZero=self.ignore_zero, verbose=self.verbose
        )

        for i in range(self.epochs):

            logging.info(
                f"Epoch {i + 1}/{self.epochs} for {self.current_dataset}, num_slices: {self.num_slices}, num_dimensions: {self.num_dimensions}"
            )

            start_time = time.time()

            flatten_y_train = np.array(y_train).flatten().astype(str).tolist()
            x_train_int = to_int_list(x_train)

            wsd.train(x_train_int, flatten_y_train)

            X_bin_int = to_int_list(X_bin)
            predictions = wsd.classify(X_bin_int)
            y_true_list, predictions_list = prepare_labels(y_true, predictions)

            accuracy = round(accuracy_score(y_true_list, predictions_list) * 100, 2)
            conf_matrix = confusion_matrix(y_true_list, predictions_list)

            elapsed_time = time.time() - start_time

            new_row = pd.DataFrame(
                {
                    "model": ["Wisard"],
                    "time": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                    "delta_time": [f"{elapsed_time:.4f}"],
                    "dataset": [self.current_dataset],
                    "encoding": [encoder["encoding"]],
                    "num_slices": [
                        self.num_slices if encoder["encoding"] == "Scatter Code" else ""
                    ],
                    "num_dimensions": [
                        (
                            self.num_dimensions
                            if encoder["encoding"] == "Scatter Code"
                            else ""
                        )
                    ],
                    "accuracy": [accuracy],
                },
                columns=[
                    "model",
                    "time",
                    "delta_time",
                    "dataset",
                    "encoding",
                    "num_slices",
                    "num_dimensions",
                    "accuracy",
                ],
            )

            new_row.to_csv(
                self.csv_file, mode="a", index=False, header=add_header(self.csv_file)
            )

            logging.info(f"Accuracy: {accuracy}")
            logging.info(f"Confusion Matrix: \n{conf_matrix}")

    def execute_dataset(self, id):
        self.current_dataset_id = id

        logging.info(f"Processing dataset ID: {id}")

        if id == "mnist":
            X_train, X_test, y_train, y_test, name = load_mnist()
            y = torch.cat((y_train, y_test), dim=0)
            X = torch.cat((X_train, X_test), dim=0)
        else:
            X, y, name = load_from_uci(id)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )

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
                f"Starting evaluation for encoder: {encoder['encoding']}, dataset: {name}, ID: {id}, num_slices: {self.num_slices}, num_dimensions: {self.num_dimensions}"
            )

            X_bin = binarize(encoder, X)
            X_train_bin = binarize(encoder, X_train)

            self.evaluate_model(X_train_bin, X_bin, y_train, y, encoder)

        logging.info(
            f"Finished processing dataset: {name} with ID: {id}, num_slices: {self.num_slices}, num_dimensions: {self.num_dimensions}"
        )

    def run(self):
        # Limit the number of concurrent threads for dataset processing
        MAX_DATASET_THREADS = 1  # Adjust based on your system's capabilities

        with ThreadPoolExecutor(max_workers=MAX_DATASET_THREADS) as executor:
            futures = []
            for dataset_id in self.datasets_ids:
                future = executor.submit(self.execute_dataset, dataset_id)
                futures.append(future)

            for future in as_completed(futures):
                try:
                    future.result()  # Wait for each thread to complete
                except Exception as e:
                    logging.error(f"Dataset thread encountered an error: {e}")
