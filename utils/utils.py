import os
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo
import logging
import pandas as pd
import torch
import numpy as np
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

def add_header(csv_file):
    file_exists = os.path.isfile(csv_file)
    file_is_empty = os.path.getsize(csv_file) == 0 if file_exists else True
    return not file_exists or file_is_empty


def load_from_uci(id: int):
    
    logging.info(f"Fetching dataset with ID: {id}")
    df = fetch_ucirepo(id=id)
    if 'ID' in df.data.features.columns:
        df.data.features = df.data.features.drop(columns=['ID'])
    X = df.data.features
    y = df.data.targets

    if isinstance(y, pd.Series):
        y = y.astype(str)  
    elif isinstance(y, pd.DataFrame):
        y = y.iloc[:, 0].astype(str)  
    else:
        y = [str(value) for value in y]  

    name = df.metadata.name
    logging.info(f"Dataset fetched: {name}")
    return X, y, name


def get_min_max(X):
    logging.info("Calculating min and max values for the dataset")

    if isinstance(X, pd.DataFrame):
        X = X.to_numpy()
    elif isinstance(X, torch.Tensor):
        X = X.numpy()
    if not isinstance(X, np.ndarray):
        raise TypeError(
            "Input X must be a pandas DataFrame, PyTorch tensor, or NumPy array"
        )

    min_val = X.flatten().min()
    max_val = X.flatten().max()

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

    return {
        "encoding": encoding_type,
        "encoder": encoder_class(num_bits_thermometer).fit(data),
    }


import torch
import logging
from typing import Union

def binarize(
    encoder, 
    data,
    batch_size = 1024  # Process in batches to avoid memory overload
) -> torch.Tensor:

    try:
        logging.info(f"Binarizing data using encoder: {encoder['encoding']}")
        
        data_tensor = to_tensor(data)
        
        binarized_batches = []

        for i in range(0, len(data_tensor), batch_size):
            batch = data_tensor[i:i+batch_size]
            
            if encoder["encoding"] == "Scatter Code":
                binarized_batch = encoder["encoder"](batch)
            else:
                binarized_batch = encoder["encoder"].binarize(batch)
            
            binarized_batch = binarized_batch.flatten(start_dim=1)
            binarized_batches.append(binarized_batch)
        
        print("concat", i)
        res = torch.cat(binarized_batches, dim=0)
        print("finished")
        return res
    
    except Exception as e:
        logging.error(f"Error binarizing data: {e}")
        raise

# def load_mnist():
    
#     transform = transforms.Compose(
#         [transforms.ToTensor(), transforms.Lambda(lambda x: torch.flatten(x))]
#     )

#     root_dir = "data"
#     dataset_name = "MNIST"

#     dataset_path = os.path.join(root_dir, dataset_name)

#     if not os.path.exists(dataset_path):
#         download = True
#     else:
#         required_files = [
#             "train-images-idx3-ubyte",
#             "train-labels-idx1-ubyte",
#             "t10k-images-idx3-ubyte",
#             "t10k-labels-idx1-ubyte",
#         ]
#         downloaded_files = os.listdir(os.path.join(dataset_path, "raw"))
#         download = not all(file in downloaded_files for file in required_files)

#     train_dataset = datasets.MNIST(
#         root="./data", train=True, download=download, transform=transform
#     )
#     test_dataset = datasets.MNIST(
#         root="./data", train=False, download=download, transform=transform
#     )

#     train_loader = DataLoader(
#         dataset=train_dataset, batch_size=len(train_dataset), shuffle=True
#     )
#     test_loader = DataLoader(
#         dataset=test_dataset, batch_size=len(test_dataset), shuffle=False
#     )

#     X_train, y_train = next(iter(train_loader))
#     X_test, y_test = next(iter(test_loader))

#     return X_train, X_test, y_train, y_test, "MNIST"


def load_mnist():
    mnist = fetch_openml('mnist_784')
    X = mnist.data
    y = mnist.target
    
    return X, y, "MNIST"

def to_tensor(X):
    if isinstance(X, torch.Tensor):
        return X
    elif isinstance(X, (pd.DataFrame, pd.Series)):
        return torch.tensor(X.to_numpy().astype(float))
    elif isinstance(X, np.ndarray):
        return torch.tensor(X.astype(float))
    else:
        return torch.tensor(X)


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

    if y_true.dtype.kind in [
        "U",
        "O",
    ]: 
        unique_labels = np.unique(np.concatenate([y_true, y_pred]))
        label_mapping = {label: idx for idx, label in enumerate(unique_labels)}
        y_true = np.array([label_mapping[label] for label in y_true], dtype=np.uint8)
        y_pred = np.array([label_mapping[label] for label in y_pred], dtype=np.uint8)
    else:
        # Convert to uint8 if they are not already numeric
        y_true = y_true.astype(np.uint8)
        y_pred = y_pred.astype(np.uint8)

    return y_true, y_pred


def encode_labels(y):
    if isinstance(y, (pd.Series, pd.DataFrame)):
        y = y.astype(str).tolist()
    elif isinstance(y, torch.Tensor):
        y = y.numpy().astype(str).tolist()

    unique_labels = sorted(list(set(y)))
    mapping = {label: idx for idx, label in enumerate(unique_labels)}

    y_mapped = [mapping[label] for label in y]
    return torch.tensor(y_mapped, dtype=torch.long)


def get_features_by_type(dataset):

    non_target = dataset.variables[dataset.variables["role"] != "Target"]
    is_categorical = (
        non_target["type"].str.lower().str.contains("categorical|nominal", na=False)
    )

    categoricals = non_target[is_categorical]["name"].tolist()
    numerics = non_target[~is_categorical]["name"].tolist()

    return categoricals, numerics


def train_test_split_categorical(
    X,
    y,
    test_size=0.33,
    random_state=42,
    categorical_features=None,
    numeric_features=None,
):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    X_train_categorical = pd.get_dummies(
        X_train, columns=categorical_features, dtype=np.uint8
    )
    X_test_categorical = pd.get_dummies(
        X_test, columns=categorical_features, dtype=np.uint8
    )
    
    X_train_numeric = X_train[numeric_features]
    X_test_numeric = X_test[numeric_features]

    return X_train_categorical, X_test_categorical, X_train_numeric, X_test_numeric, y_train, y_test
