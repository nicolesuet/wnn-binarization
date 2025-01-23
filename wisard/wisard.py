import os
import numpy as np
import torch
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
)


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

    def __init__(
        self,
        num_slices,
        num_dimensions,
        address_size,
        ignore_zero,
        verbose,
        num_bits_thermometer,
        datasets_ids,
        epochs=10,
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

    def evaluate_model(self, x_train, X_bin, y_train, y_true, encoder):

        for _ in range(self.epochs):
            
            start_time = time.time()

            wsd = wp.Wisard(
                self.address_size, ignoreZero=self.ignore_zero, verbose=self.verbose
            )
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
                    "num_slices": [self.num_slices if encoder["encoding"] == "Scatter Code" else ''],
                    "num_dimensions": [self.num_dimensions if encoder["encoding"] == "Scatter Code" else ''],
                    "accuracy": [accuracy],
                },
                columns=[
                    "model",
                    "time",
                    "delta_time",
                    "encoding",
                    "num_slices",
                    "num_dimensions",
                    "accuracy"
                ],
            )

            new_row.to_csv(
                self.csv_file, mode="a", index=False, header=add_header(self.csv_file)
            )

            logging.info(f"Accuracy: {accuracy}")
            logging.info(f"Confusion Matrix: \n{conf_matrix}")

    def run(self):
        for id in self.datasets_ids:

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
            
            self.csv_file = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), f"metrics/{csv_name}_metrics.csv"
            )

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )

            torch_tensor = torch.tensor(X.values)

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
                logging.info(f"Starting evaluation for encoder: {encoder['encoding']}")

                X_bin = binarize(encoder, X.values)
                X_train_bin = binarize(encoder, X_train.values)

                self.evaluate_model(X_train_bin, X_bin, y_train, y, encoder)

            logging.info(f"Finished processing dataset: {name} with ID: {id}")
