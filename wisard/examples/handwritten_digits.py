import sys
import os
import numpy as np
import torch
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo
import wisardpkg as wp
from torchhd import embeddings
from torchwnn.encoding import DistributiveThermometer, GaussianThermometer
from datetime import datetime
import pandas as pd

handwritten_digits = fetch_ucirepo(id=80)
X = handwritten_digits.data.features
y = handwritten_digits.data.targets

num_features = X.shape[1]
print("Number of features:", num_features)

min_global = np.array(X.values).flatten().min()
max_global = np.array(X.values).flatten().max()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

csv_file = 'wisard/examples/handwritten_digits_metrics.csv'

torch_tensor = torch.tensor(X.values, dtype=torch.float32)

encoders = [
    {"encoding": "DISTRIBUTIVE", "encoder": DistributiveThermometer(10).fit(torch_tensor)},
    {"encoding": "GAUSSIAN", "encoder": GaussianThermometer(10).fit(torch_tensor)},
]

ADDRESS_SIZE = 10
IGNORE_ZERO = False
VERBOSE = False


def evaluate_model(x_train, x_test, X_bin, y_train, y_true, encoder):

    wsd = wp.Wisard(ADDRESS_SIZE, ignoreZero=IGNORE_ZERO, verbose=VERBOSE)
    flatten_y_train = np.array(y_train.values).flatten()
    flatten_y_train = np.array([str(label) for label in flatten_y_train])

    wsd.train(x_train.numpy(), flatten_y_train)
    predictions = wsd.classify(np.array(X_bin))
    
    y_true_str = np.array([str(label) for label in y_true.values.flatten()])

    precision = round(precision_score(y_true_str, predictions, average='macro') * 100, 2)
    recall = round(recall_score(y_true_str, predictions, average='macro') * 100, 2)
    accuracy = round(accuracy_score(y_true_str, predictions) * 100, 2)
    conf_matrix = confusion_matrix(y_true_str, predictions)

    new_row = pd.DataFrame({
        'time': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        'encoding': [encoder],
        'precision': [precision],
        'accuracy': [accuracy],
        'recall': [recall]
    })
    
    new_row.to_csv(csv_file, mode='a', index=False, header=not (os.path.isfile(csv_file)))

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"Accuracy: {accuracy}")
    print("Confusion Matrix:\n")
    print(conf_matrix)


for elem in encoders:
    print(f"\nEncoding: {elem['encoding']}\n")
    
    encoder = elem["encoder"]

    x_train = encoder.binarize(torch.tensor(X_train.values)).flatten(start_dim=1)
    x_test = encoder.binarize(torch.tensor(X_test.values)).flatten(start_dim=1)
    X_bin = encoder.binarize(torch.tensor(X.values)).flatten(start_dim=1)

    evaluate_model(x_train, x_test, X_bin, y_train, y, elem["encoding"])

print("\nEncoding: SCATTER\n")

emb = embeddings.Level(10, 20, "BSC", low=min_global, high=max_global, dtype=torch.uint8)

x_train = emb(torch.tensor(X_train.values)).flatten(start_dim=1)
x_test = emb(torch.tensor(X_test.values)).flatten(start_dim=1)
X_bin = emb(torch.tensor(X.values)).flatten(start_dim=1)

evaluate_model(x_train, x_test, X_bin, y_train, y, 'SCATTER')