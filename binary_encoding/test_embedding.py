import torch
from embeddings import ScatterCode

coding = ScatterCode(5, 100, low=0.1, high=7.9, dtype=torch.uint8)
print(len(coding.weight))
print(coding.weight)


for i in range(len(coding.weight)-1):
    hv1 = coding.weight[i]
    for j in range(i+1, len(coding.weight)):
        hv2 = coding.weight[j]

        hd = torch.sum(torch.bitwise_xor(hv1, hv2)).item() # hamming distance        
        print("Hamming Distance (V", i, ", V", j, ") = ", hd)

print("Hyper-vector: ", coding(torch.tensor([5.0])))
