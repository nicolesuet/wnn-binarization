import torch
from embeddings import ScatterCode
from pandas import read_csv

# Load dataset
url = "dataset/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
features_minmax = {}
dataset = read_csv(url, names=names)
minGlobal = 1<<31
maxGlobal = 0
features_num = len(names) - 1
num_slices = 5
dimension = 100
num_classes = 3
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

for i in range(features_num): 
  minVal = min(dataset[names[i]])
  maxVal = max(dataset[names[i]])
  features_minmax[names[i]] = {'min': minVal, 'max': maxVal}

  if minVal < minGlobal:
    minGlobal = minVal

  if maxVal > maxGlobal:
    maxGlobal = maxVal

print(minGlobal, maxGlobal)
coding = ScatterCode(num_slices, dimension, low=minGlobal, high=maxGlobal)

X = dataset[names[:-1]]
y = dataset[names[-1]]

with torch.no_grad():
  samples = torch.tensor(X.values).to(device)
  bin_X = coding(samples)
  print(bin_X, bin_X.shape)
  bin_X = torch.flatten(bin_X, start_dim=1)
  print(bin_X, bin_X.shape)
