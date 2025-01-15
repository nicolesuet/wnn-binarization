import torch
from torch import nn
from torch.nn.functional import cross_entropy
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import torch_dwn as dwn
from sklearn.metrics import confusion_matrix, precision_score, recall_score, accuracy_score
from sklearn.model_selection import train_test_split
from ucimlrepo import fetch_ucirepo
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from torchhd import embeddings
import argparse
from datetime import datetime

def evaluate(model, x_test, y_test, device="cuda"):
    model.eval()
    with torch.no_grad():
        pred = (model(x_test.cuda(device)).cpu()).argmax(dim=1).numpy()
        acc = (pred == y_test.numpy()).sum() / y_test.shape[0]
    return acc


def train_and_evaluate(x_train, y_train, x_test, y_test, epochs, batch_size, device="cuda"):
        
    model = nn.Sequential(
        dwn.LUTLayer(x_train.size(1), 2000, n=6, mapping='learnable'),
        dwn.LUTLayer(2000, 1000, n=6),
        dwn.GroupSum(k=10, tau=1/0.3)
    )

    model = model.cuda()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-2)
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, gamma=0.1, step_size=14)

    n_samples = x_train.shape[0]
    accuracies = []

    for epoch in range(epochs):
        print(f"Epoch: {epoch}")

        model.train()

        permutation = torch.randperm(n_samples)
        correct_train = 0
        total_train = 0

        for i in range(0, n_samples, batch_size):
            optimizer.zero_grad()

            indices = permutation[i:i+batch_size]
            batch_x, batch_y = x_train[indices].cuda(device), y_train[indices].cuda(device)
            outputs = model(batch_x)
            loss = cross_entropy(outputs, batch_y)
            loss.backward()
            optimizer.step()

            pred_train = outputs.argmax(dim=1)
            correct_train += (pred_train == batch_y).sum().item()
            total_train += batch_y.size(0)

    train_acc = correct_train / total_train
    scheduler.step()
    test_acc = evaluate(model, x_test, y_test)
    accuracies.append(f"{test_acc:.4f}")
    
    print(f'Epoch {epoch + 1}/{epochs}, Train Loss: {loss.item():.4f}, Train Accuracy: {train_acc:.4f}, Test Accuracy: {test_acc:.4f}')
      
    return accuracies

def main(epochs, batch_size):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    csv_file = 'DWN/examples/iris_metrics.csv'

    iris = fetch_ucirepo(id=53)
    X = iris.data.features
    y = iris.data.targets

    min_global = np.array(X.values).flatten().min()
    max_global = np.array(X.values).flatten().max()

    print(f"Min global: {min_global}")
    print(f"Max global: {max_global}")

    # transformar label em int
    label_encoder = LabelEncoder()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    y_train = label_encoder.fit_transform(y_train.values.ravel())
    y_test = label_encoder.fit_transform(y_test.values.ravel())
    y_test_tensor = torch.tensor(y_test, dtype=torch.long)
    y_train_tensor = torch.tensor(y_train, dtype=torch.long)

    torch_tensor = torch.tensor(X.values)

    encoders = [
        {"encoding": "DISTRIBUTIVE", "encoder": dwn.DistributiveThermometer(10).fit(torch_tensor)},
        {"encoding": "GAUSSIAN", "encoder": dwn.GaussianThermometer(10).fit(torch_tensor)},
    ]

    for elem in encoders:
        
        encoder =  elem['encoder']
        
        x_train = encoder.binarize(torch.tensor(X_train.values)).flatten(start_dim=1)
        x_test = encoder.binarize(torch.tensor(X_test.values)).flatten(start_dim=1)

        print(f"\nEncoding: {elem['encoding']}\n")
        
        accuracies = train_and_evaluate(x_train, y_train_tensor, x_test, y_test_tensor, epochs, batch_size, device)
        
        for accuracy_score in accuracies:            
            new_row = pd.DataFrame({
                'time': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                'encoding': [elem['encoding']],
                'accuracy': [accuracy_score],
            })
            
            new_row.to_csv(csv_file, mode='a', index=False, header=not (os.path.isfile(csv_file)))


    print(f"\nEncoding: SCATTER\n")

    emb = embeddings.Level(10, 20, "BSC", low=min_global, high=max_global, dtype=torch.uint8)

    x_train = emb(torch.tensor(X_train.values)).flatten(start_dim=1).float()
    x_test = emb(torch.tensor(X_test.values)).flatten(start_dim=1).float()

    accuracies = train_and_evaluate(x_train, y_train_tensor, x_test, y_test_tensor, epochs, batch_size, device)
        
    for accuracy_score in accuracies:            
        new_row = pd.DataFrame({
            'time': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            'encoding': [elem['encoding']],
            'accuracy': [accuracy_score],
        })
    
        new_row.to_csv(csv_file, mode='a', index=False, header=not (os.path.isfile(csv_file)))

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Train and evaluate model on Iris dataset')
    parser.add_argument('--epochs', type=int, default=10, help='Number of epochs to train the model')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size')
    
    ARGS = parser.parse_args()
    
    main(ARGS.epochs, ARGS.batch_size)