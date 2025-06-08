# Analysis Conclusions

## All Encoding Results per Dataset and Model

### DWN: All Encoding Results

| Dataset   | Encoding   | Num Dimensions   | Num Slices   | Mean Accuracy   | Standard Deviation   |
|-----------|------------|------------------|--------------|-----------------|----------------------|

### Wisard: All Encoding Results

| Dataset                       | Encoding     |   Num Dimensions |   Num Slices |   Mean Accuracy |   Standard Deviation |
|:------------------------------|:-------------|-----------------:|-------------:|----------------:|---------------------:|
| Ecoli                         | Gaussian     |                1 |            1 |         83.603  |           2.28062    |
| Ecoli                         | Linear       |                1 |            1 |         83.333  |           2.33667    |
| Ecoli                         | Distributive |                1 |            1 |         81.442  |           2.6934     |
| Glass Identification          | Distributive |                1 |            1 |         77.886  |           2.30331    |
| Glass Identification          | Gaussian     |                1 |            1 |         76.057  |           2.57065    |
| Glass Identification          | Linear       |                1 |            1 |         71.689  |           4.61879    |
| Iris                          | Distributive |                1 |            1 |         97.4    |           1.64655    |
| Iris                          | Linear       |                1 |            1 |         96.4    |           2.63312    |
| Iris                          | Gaussian     |                1 |            1 |         93.8    |           2.20101    |
| MNIST                         | Distributive |                1 |            1 |         95.38   |           0.0264575  |
| Maternal Health Risk          | Distributive |                1 |            1 |         76.387  |           1.14638    |
| Maternal Health Risk          | Gaussian     |                1 |            1 |         73.672  |           1.22541    |
| Maternal Health Risk          | Linear       |                1 |            1 |         71.523  |           1.51511    |
| Statlog (Shuttle)             | Gaussian     |                1 |            1 |         99.835  |           0.00527046 |
| Statlog (Shuttle)             | Distributive |                1 |            1 |         99.8107 |           0.00730046 |
| Statlog (Shuttle)             | Linear       |                1 |            1 |         97.109  |           1.53592    |
| Statlog (Vehicle Silhouettes) | Distributive |                1 |            1 |         71.679  |           1.86015    |
| Statlog (Vehicle Silhouettes) | Gaussian     |                1 |            1 |         70.499  |           1.66697    |
| Statlog (Vehicle Silhouettes) | Linear       |                1 |            1 |         64.287  |           3.25538    |
| Wine Quality                  | Distributive |                1 |            1 |         62.661  |           0.831016   |
| Wine Quality                  | Gaussian     |                1 |            1 |         61.959  |           1.36706    |
| Wine Quality                  | Linear       |                1 |            1 |         48.849  |           1.53648    |

## Best Encodings per Dataset

### DWN: Best Encoding for Each Dataset

| Dataset   | Best Encoding   | Num Dimensions   | Num Slices   | Mean Accuracy   | Standard Deviation   |
|-----------|-----------------|------------------|--------------|-----------------|----------------------|

### Wisard: Best Encoding for Each Dataset

| Dataset                       | Best Encoding   |   Num Dimensions |   Num Slices |   Mean Accuracy |   Standard Deviation |
|:------------------------------|:----------------|-----------------:|-------------:|----------------:|---------------------:|
| Ecoli                         | Gaussian        |                1 |            1 |          83.603 |           2.28062    |
| Glass Identification          | Distributive    |                1 |            1 |          77.886 |           2.30331    |
| Iris                          | Distributive    |                1 |            1 |          97.4   |           1.64655    |
| MNIST                         | Distributive    |                1 |            1 |          95.38  |           0.0264575  |
| Maternal Health Risk          | Distributive    |                1 |            1 |          76.387 |           1.14638    |
| Statlog (Shuttle)             | Gaussian        |                1 |            1 |          99.835 |           0.00527046 |
| Statlog (Vehicle Silhouettes) | Distributive    |                1 |            1 |          71.679 |           1.86015    |
| Wine Quality                  | Distributive    |                1 |            1 |          62.661 |           0.831016   |

## Optimal Scatter Code Configurations

### DWN

| dataset   | num_dimensions   | num_slices   | mean   | std   | model   |
|-----------|------------------|--------------|--------|-------|---------|

### Wisard

| dataset   | num_dimensions   | num_slices   | mean   | std   | model   |
|-----------|------------------|--------------|--------|-------|---------|

## Delta Time Comparisons

### DWN

| dataset   | encoding   | num_dimensions   | num_slices   | mean   | std   |
|-----------|------------|------------------|--------------|--------|-------|

### Wisard

| dataset                       | encoding     |   num_dimensions |   num_slices |      mean |         std |
|:------------------------------|:-------------|-----------------:|-------------:|----------:|------------:|
| Ecoli                         | Distributive |                1 |            1 |  0.00141  | 0.000246982 |
| Ecoli                         | Gaussian     |                1 |            1 |  0.00119  | 0.000218327 |
| Ecoli                         | Linear       |                1 |            1 |  0.00112  | 4.21637e-05 |
| Glass Identification          | Distributive |                1 |            1 |  0.00625  | 0.00190977  |
| Glass Identification          | Gaussian     |                1 |            1 |  0.00482  | 0.000345768 |
| Glass Identification          | Linear       |                1 |            1 |  0.00472  | 0.00010328  |
| Iris                          | Distributive |                1 |            1 |  0.00049  | 0.000566569 |
| Iris                          | Gaussian     |                1 |            1 |  0.0003   | 0           |
| Iris                          | Linear       |                1 |            1 |  0.0003   | 0           |
| MNIST                         | Distributive |                1 |            1 | 52.0069   | 0.835104    |
| Maternal Health Risk          | Distributive |                1 |            1 |  0.00298  | 0.000706792 |
| Maternal Health Risk          | Gaussian     |                1 |            1 |  0.0022   | 0           |
| Maternal Health Risk          | Linear       |                1 |            1 |  0.00224  | 9.66092e-05 |
| Statlog (Shuttle)             | Distributive |                1 |            1 |  0.917371 | 0.0258906   |
| Statlog (Shuttle)             | Gaussian     |                1 |            1 |  0.94845  | 0.0188687   |
| Statlog (Shuttle)             | Linear       |                1 |            1 |  1.89994  | 0.358516    |
| Statlog (Vehicle Silhouettes) | Distributive |                1 |            1 |  0.00656  | 0.00103944  |
| Statlog (Vehicle Silhouettes) | Gaussian     |                1 |            1 |  0.00597  | 0.000262679 |
| Statlog (Vehicle Silhouettes) | Linear       |                1 |            1 |  0.00566  | 0.000267499 |
| Wine Quality                  | Distributive |                1 |            1 |  0.03419  | 0.0017483   |
| Wine Quality                  | Gaussian     |                1 |            1 |  0.03442  | 0.00231363  |
| Wine Quality                  | Linear       |                1 |            1 |  0.04883  | 0.00297547  |
## Scatter Code Accuracy by Dataset

### DWN: Mean Accuracy and Standard Deviation for Scatter Code Configurations

| Dataset   | Num Slices   | Num Dimensions   | Mean Accuracy   | Standard Deviation   |
|-----------|--------------|------------------|-----------------|----------------------|

### Wisard: Mean Accuracy and Standard Deviation for Scatter Code Configurations

| Dataset   | Num Slices   | Num Dimensions   | Mean Accuracy   | Standard Deviation   |
|-----------|--------------|------------------|-----------------|----------------------|

