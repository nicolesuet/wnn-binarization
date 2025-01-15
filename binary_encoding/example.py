import torch
from embeddings import ScatterCode

# setup ScatterCode parameters
min_val = 1
max_val = 10
num_slices = 5
dimension = 10

coding = ScatterCode(num_slices, dimension, low=min_val, high=max_val)
print(coding.weight)

# encoding examples
number = torch.tensor(5)
print(coding(number))

for i in range(min_val, max_val + 1):
    number = torch.tensor(i)
    print(i, " => ", coding(number))
