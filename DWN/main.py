import os
import numpy as np
import torch
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo
from torchwnn.encoding import DistributiveThermometer, GaussianThermometer, Thermometer
from datetime import datetime
import pandas as pd
from embeddings import ScatterCode
import logging
import time
import torchvision
from sklearn.preprocessing import LabelEncoder
import torch_dwn as dwn
from torch.nn.functional import cross_entropy
from torchhd import embeddings
from torch import nn

log_file = os.path.join(os.path.dirname(__file__), "wisard.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)

logging.info("Starting the script")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

NUM_SLICES = 10
NUM_DIMENSIONS = 20
NUM_BITS_THEMOMETER = 10
ADDRESS_SIZE = 10
IGNORE_ZERO = False
VERBOSE = False
EPOCHS = 10
BATCH_SIZE = 32

datasets_ids = [
    # 222,  # Bank Marketing ! error calculating min and max
    39,  # Ecoli
    # 53,  # Iris
    # 186,  # Wine Quality
    # 264,  # EEG Eye State
    # 159,  # MAGIC Gamma Telescope
    # # 2,  # Adult ! error calculating min and max
    # 149,  # Statlog (Vehicle Silhouettes)
    # 863,  # Maternal Health Risk
    # 42,  # Glass Identification
    # "mnist",  # MNIST
]

encoder_definitions = [
    ("Distributive", DistributiveThermometer),
    ("Gaussian", GaussianThermometer),
    ("Linear", Thermometer),
    ("Scatter Code", ScatterCode),
]


def create_encoder(encoding_type, encoder_class, bins, data, min, max):

    logging.info(f"Creating encoder of type: {encoding_type}")

    if encoding_type == "Scatter Code":
        return {
            "encoding": encoding_type,
            "encoder": encoder_class(NUM_SLICES, NUM_DIMENSIONS, min, max),
        }

    return {"encoding": encoding_type, "encoder": encoder_class(bins).fit(data)}


def load_from_uci(id: int):
    logging.info(f"Fetching dataset with ID: {id}")
    dataset = fetch_ucirepo(id=id)
    X = dataset.data.features
    y = dataset.data.targets

    if isinstance(y, pd.Series):
        y = y.astype(str)  # For pandas Series
    elif isinstance(y, pd.DataFrame):
        y = y.iloc[:, 0].astype(str)  # Convert the first column if it's a DataFrame
    else:
        y = [str(value) for value in y]  # Fallback for other types

    name = dataset.metadata.name
    logging.info(f"Dataset fetched: {name}")
    return X, y, name


def load_mnist():
    logging.info("Fetching MNIST dataset without transformation (raw)")

    # MNIST dataset with no transformation (raw images)
    train_dataset = torchvision.datasets.MNIST(
        root="./data", train=True, download=True, transform=None
    )
    test_dataset = torchvision.datasets.MNIST(
        root="./data", train=False, download=True, transform=None
    )

    # Flatten the images into 1D vectors (28x28 pixels -> 784 features per image)
    X_train = torch.stack(
        [torch.tensor(np.array(x[0]).flatten()) for x in train_dataset]
    )  # Flatten images to 1D vector
    y_train = torch.tensor([x[1] for x in train_dataset])

    X_test = torch.stack(
        [torch.tensor(np.array(x[0]).flatten()) for x in test_dataset]
    )  # Flatten images to 1D vector
    y_test = torch.tensor([x[1] for x in test_dataset])

    return X_train, X_test, y_train, y_test, "MNIST"


def get_min_max(X):
    logging.info("Calculating min and max values for the dataset")
    min = np.array(X.values).flatten().min()
    max = np.array(X.values).flatten().max()
    logging.info(f"Min value: {min}, Max value: {max}")
    return min, max


def binarize(encoder, data):
    logging.info(f"Binarizing data using encoder: {encoder['encoding']}")

    if encoder["encoding"] == "Scatter Code":
        return encoder["encoder"](torch.tensor(data)).flatten(start_dim=1)

    return encoder["encoder"].binarize(torch.tensor(data)).flatten(start_dim=1)


def evaluate(model, x_test, y_test, device="cuda"):
    model.eval()
    with torch.no_grad():
        pred = (model(x_test.cuda(device)).cpu()).argmax(dim=1).numpy()
        acc = (pred == y_test.numpy()).sum() / y_test.shape[0]
    return acc


def evaluate_model(x_train, y_train, X_test, y_test, encoder, start_time):

    if not start_time:
        start_time = time.time()

    model = nn.Sequential(
        dwn.LUTLayer(x_train.size(1), 2000, n=6, mapping="learnable"),
        dwn.LUTLayer(2000, 1000, n=6),
        dwn.GroupSum(k=10, tau=1 / 0.3),
    )

    model = model.cuda()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-2)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, gamma=0.1, step_size=14)

    n_samples = x_train.shape[0]
    accuracies = []

    for epoch in range(EPOCHS):
        model.train()

        permutation = torch.randperm(n_samples)
        correct_train = 0
        total_train = 0

        for i in range(0, n_samples, BATCH_SIZE):
            optimizer.zero_grad()

            indices = permutation[i : i + BATCH_SIZE]
            batch_x, batch_y = (
                x_train[indices].cuda(device).float(),
                y_train[indices].cuda(device).float(),
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
        test_acc = evaluate(model, X_test, y_test)
        accuracy = f"{test_acc:.4f}"
        accuracies.append(f"{test_acc:.4f}")

        new_row = pd.DataFrame(
            {
                "model": ["Wisard"],
                "time": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                "encoding": [encoder["encoding"]],
                "accuracy": [accuracy],
                "delta_time": [f"{elapsed_time:.4f}"],
            }
        )

        new_row.to_csv(
            csv_file, mode="a", index=False, header=not (os.path.isfile(csv_file))
        )

        logging.info(
            f"Epoch {epoch + 1}/{EPOCHS}, Train Loss: {loss.item():.4f}, Train Accuracy: {train_acc:.4f}, Test Accuracy: {test_acc:.4f}"
        )

    elapsed_time = time.time() - start_time


for id in datasets_ids:

    logging.info(f"Processing dataset ID: {id}")

    if id == "mnist":
        X_train, X_test, y_train, y_test, name = load_mnist()
    else:
        X, y, name = load_from_uci(id)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.33, random_state=42
        )

    min_global, max_global = get_min_max(X)

    label_encoder = LabelEncoder()

    y_train = label_encoder.fit_transform(y_train.values.ravel())
    y_test = label_encoder.fit_transform(y_test.values.ravel())
    y_test_tensor = torch.tensor(y_test, dtype=torch.long)
    y_train_tensor = torch.tensor(y_train, dtype=torch.long)

    csv_name = name.lower().replace(" ", "_")
    csv_file = os.path.join(
        os.path.dirname(__file__), f"metrics/{csv_name}_metrics.csv"
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=42
    )

    torch_tensor = torch.tensor(X.values)

    encoders = [
        create_encoder(
            encoding_type,
            encoder_class,
            NUM_BITS_THEMOMETER,
            torch_tensor,
            min_global,
            max_global,
        )
        for encoding_type, encoder_class in encoder_definitions
    ]

    for encoder in encoders:
        logging.info(f"Starting evaluation for encoder: {encoder['encoding']}")

        start_time = time.time()

        X_train_bin = binarize(encoder, X_train.values)
        X_test_bin = binarize(encoder, X_test.values)

        evaluate_model(
            X_train_bin, y_train_tensor, X_test_bin, y_test_tensor, encoder, start_time
        )

    logging.info(f"Finished processing dataset: {name} with ID: {id}")
