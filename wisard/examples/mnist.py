from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score
import wisardpkg as wp
from ucimlrepo import fetch_ucirepo 
import torch
from sklearn.model_selection import train_test_split
from sklearn import datasets
import numpy as np
import sys
import os
from torchhd import embeddings
from torchwnn.encoding import DistributiveThermometer, GaussianThermometer

datasets = [
    {
        "name": "iris", "dataset": datasets.load_iris()
    },
    {
        "name": "MNIST", "dataset": datasets.load_digits()
    }
]

for elem in datasets:

    print(f"\n=====================Dataset: {elem['name']} =====================\n")

    dataset = elem["dataset"]
    
    X = dataset.data
    min_global = np.array(X).flatten().min()
    max_global = np.array(X).flatten().max()
    target_names = dataset.target_names
    y = dataset.target
    
    print(f"Target names: {target_names}")

    mapping = {}   

    for i, name in enumerate(target_names):
        mapping[i] = str(name)

    print(f"Mapping: {mapping}")

    y = [str(value) for value in dataset.target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=42)

    torch_tensor = torch.tensor(X)
    # print(torch_tensor[:5])

    thermometers = [
        {
            "name": "dist", "thermometer": DistributiveThermometer(100).fit(torch_tensor)
        },
        {
            "name": "gauss", "thermometer": GaussianThermometer(100).fit(torch_tensor)
        }
    ]

    for elem in thermometers:

        print(f"\n=> Thermometer: {elem['name']}\n")

        thermometer = elem["thermometer"]

        x_train = thermometer.binarize(torch.tensor(X_train)).flatten(start_dim=1)
        x_test = thermometer.binarize(torch.tensor(X_test)).flatten(start_dim=1)
        X_bin = thermometer.binarize(torch.tensor(X)).flatten(start_dim=1)

        addressSize = 16 
        ignoreZero  = False
        verbose = False

        wsd = wp.Wisard(addressSize, ignoreZero=ignoreZero, verbose=verbose)
        flatten_y_train = np.array(y_train).flatten()
        wsd.train(x_train.numpy(), flatten_y_train)
        out = wsd.classify(np.array(X_bin))
        
        precision = round(precision_score(y, out, average='macro') * 100, 2)
        recall = round(recall_score(y, out, average='macro') * 100, 2)
        accuracy = round(accuracy_score(y, out) * 100, 2)

        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
        print(f"Accuracy: {accuracy}")
        print(f"Confusion Matrix:\n")
        print(confusion_matrix(y, out))

        # for i,d in enumerate(X):
        #     if(out[i] != y[i]):
        #         print(out[i],d, y[i])            


    print(f"\n=> Thermometer: scatter\n")

    emb = embeddings.Level(10, 100, "BSC", low=min_global, high=max_global, dtype = torch.uint8)

    x_train = emb(torch.tensor(X_train)).flatten(start_dim=1)
    x_test = emb(torch.tensor(X_test)).flatten(start_dim=1)
    X_bin = emb(torch.tensor(X)).flatten(start_dim=1)

    addressSize = 10 
    ignoreZero  = False
    verbose = False

    wsd = wp.Wisard(addressSize, ignoreZero=ignoreZero, verbose=verbose)
    flatten_y_train = np.array(y_train).flatten()
    wsd.train(x_train.numpy(), flatten_y_train)
    out = wsd.classify(np.array(X_bin))

    precision = round(precision_score(y, out, average='macro') * 100, 2)
    recall = round(recall_score(y, out, average='macro') * 100, 2)
    accuracy = round(accuracy_score(y, out) * 100, 2)

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"Accuracy: {accuracy}")
    print(f"Confusion Matrix:\n")
    print(confusion_matrix(y, out))

