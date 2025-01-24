import os
from sklearn.datasets import fetch_openml
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


def get_min_max(X):
    logging.info("Calculating min and max values for the dataset")
    
    if hasattr(X, 'values'):
        X = X.values
    
    min_val = np.array(X).flatten().min()
    max_val = np.array(X).flatten().max()
    
    logging.info(f"Min value: {min_val}, Max value: {max_val}")
    return min_val, max_val

def create_encoder(
    encoding_type,
    encoder_class,
    num_bits_thermometer,
    data,
    min,
    max,
    num_slices,
    num_dimensions,
):

    logging.info(f"Creating encoder of type: {encoding_type}")

    if data.dtype == torch.long:  # Check if the dtype is integer
        data = data.float()  # Convert to floating-point dtype

    if encoding_type == "Scatter Code":
        return {
            "encoding": encoding_type,
            "encoder": encoder_class(num_slices, num_dimensions, min, max),
        }

    return {"encoding": encoding_type, "encoder": encoder_class(num_bits_thermometer).fit(data)}


def binarize(encoder, data):
    logging.info(f"Binarizing data using encoder: {encoder['encoding']}")

    data = to_tensor(data)

    if encoder["encoding"] == "Scatter Code":
        return encoder["encoder"](data).flatten(start_dim=1)

    return encoder["encoder"].binarize(data).flatten(start_dim=1)

def load_mnist():
    logging.info("Fetching MNIST dataset")

    mnist = fetch_openml('mnist_784', version=1, as_frame=False)
    X, y = mnist.data, mnist.target
    y = y.astype(np.uint8)
    
    return X[:1000], y[:1000], "MNIST"

def to_tensor(X):
    return torch.tensor(X.values) if hasattr(X, 'values') else torch.tensor(X)

def to_int_list(data):
    if isinstance(data, np.ndarray):
        return data.astype(int).tolist()
    elif isinstance(data, pd.DataFrame):
        return data.values.astype(int).tolist()
    elif isinstance(data, torch.Tensor):
        return data.numpy().astype(int).tolist()
    else:
        raise TypeError(
            f"Data must be a NumPy array, Pandas DataFrame, or PyTorch Tensor, but got {type(data)}"
        )

def to_list(data):
    if isinstance(data, list):
        data = np.array(data)
    return data

def prepare_labels(y_true, y_pred):

    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    # If y_true or y_pred contains strings, map them to integers
    if y_true.dtype.kind in ['U', 'O']:  # 'U' for Unicode strings, 'O' for object (mixed types)
        unique_labels = np.unique(np.concatenate([y_true, y_pred]))
        label_mapping = {label: idx for idx, label in enumerate(unique_labels)}
        y_true = np.array([label_mapping[label] for label in y_true], dtype=np.uint8)
        y_pred = np.array([label_mapping[label] for label in y_pred], dtype=np.uint8)
    else:
        # Convert to uint8 if they are not already numeric
        y_true = y_true.astype(np.uint8)
        y_pred = y_pred.astype(np.uint8)
    
    return y_true, y_pred