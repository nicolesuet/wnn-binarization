import os
from ucimlrepo import fetch_ucirepo
import logging
import pandas as pd
import torchvision
import torch
import numpy as np

def add_header(csv_file):
    file_exists = os.path.isfile(csv_file)
    file_is_empty = os.path.getsize(csv_file) == 0 if file_exists else True
    return not file_exists or file_is_empty


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


def create_encoder(
    encoding_type,
    encoder_class,
    bins,
    data,
    min,
    max,
    num_slices,
    num_dimensions,
):

    logging.info(f"Creating encoder of type: {encoding_type}")

    if encoding_type == "Scatter Code":
        return {
            "encoding": encoding_type,
            "encoder": encoder_class(num_slices, num_dimensions, min, max),
        }

    return {"encoding": encoding_type, "encoder": encoder_class(bins).fit(data)}


def binarize(encoder, data):
    logging.info(f"Binarizing data using encoder: {encoder['encoding']}")

    if encoder["encoding"] == "Scatter Code":
        return encoder["encoder"](torch.tensor(data)).flatten(start_dim=1)

    return encoder["encoder"].binarize(torch.tensor(data)).flatten(start_dim=1)
