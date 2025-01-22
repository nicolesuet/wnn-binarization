import os
import numpy as np
import torch
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
)
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo
import wisardpkg as wp
from torchwnn.encoding import DistributiveThermometer, GaussianThermometer, Thermometer
from datetime import datetime
import pandas as pd
from embeddings import ScatterCode
import logging
import time
import torchvision
from torchvision import transforms

log_file = os.path.join(os.path.dirname(__file__), "wisard.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)

logging.info("Starting the script")


NUM_SLICES = 10
NUM_DIMENSIONS = 20
NUM_BITS_THEMOMETER = 10
ADDRESS_SIZE = 10
IGNORE_ZERO = False
VERBOSE = False

datasets_ids = [
    # 222,  # Bank Marketing ! error calculating min and max
    39,  # Ecoli
    53,  # Iris
    186,  # Wine Quality
    264,  # EEG Eye State
    159,  # MAGIC Gamma Telescope
    # 2,  # Adult ! error calculating min and max
    149,  # Statlog (Vehicle Silhouettes)
    863,  # Maternal Health Risk
    42,  # Glass Identification
    "mnist",  # MNIST
]

encoder_definitions = [
    ("Distributive", DistributiveThermometer),
    ("Gaussian", GaussianThermometer),
    ("Linear", Thermometer),
    ("Scatter Code", ScatterCode),
]


def add_header(csv_file):
    file_exists = os.path.isfile(csv_file)
    file_is_empty = os.path.getsize(csv_file) == 0 if file_exists else True

    return not file_exists or file_is_empty

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


def evaluate_model(x_train, X_bin, y_train, y_true, encoder, start_time):

    if not start_time:
        start_time = time.time()

    wsd = wp.Wisard(ADDRESS_SIZE, ignoreZero=IGNORE_ZERO, verbose=VERBOSE)
    flatten_y_train = np.array(y_train).flatten()
    wsd.train(x_train.numpy(), flatten_y_train)
    predictions = wsd.classify(np.array(X_bin))

    accuracy = round(accuracy_score(y_true.values, predictions) * 100, 2)
    conf_matrix = confusion_matrix(y_true.values, predictions)

    elapsed_time = time.time() - start_time

    new_row = pd.DataFrame(
        {
            "model": ["Wisard"],
            "time": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "delta_time": [f"{elapsed_time:.4f}"],
            "encoding": [encoder["encoding"]],
            "accuracy": [accuracy],
        },
        columns=["model", "time", "delta_time", "encoding", "accuracy"],
    )

    new_row.to_csv(csv_file, mode="a", index=False, header=add_header(csv_file))

    logging.info(f"Accuracy: {accuracy}")
    logging.info(f"Confusion Matrix: \n{conf_matrix}")


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

        X_bin = binarize(encoder, X.values)
        X_train_bin = binarize(encoder, X_train.values)
        X_test_bin = binarize(encoder, X_test.values)

        evaluate_model(X_train_bin, X_bin, y_train, y, encoder, start_time)

    logging.info(f"Finished processing dataset: {name} with ID: {id}")
