# Analysis Conclusions

## Best Encodings per Dataset

### DWN

| dataset                       | encoding     |    mean |          std |
|:------------------------------|:-------------|--------:|-------------:|
| EEG Eye State                 | Distributive | 0.6819  |   0.0356382  |
| EEG Eye State                 | Gaussian     | 0.65865 |   0.0533866  |
| EEG Eye State                 | Linear       | 0.65665 |   0.00431335 |
| EEG Eye State                 | Scatter Code | 0.30355 |   0.111086   |
| Statlog (Vehicle Silhouettes) | Distributive | 0.4713  | nan          |
| Statlog (Vehicle Silhouettes) | Gaussian     | 0.4559  | nan          |
| Wine Quality                  | Distributive | 0.4881  | nan          |

### Wisard

| dataset                       | encoding     |    mean |     std |
|:------------------------------|:-------------|--------:|--------:|
| EEG Eye State                 | Distributive | 82.4965 | 10.2331 |
| EEG Eye State                 | Gaussian     | 80.8473 | 13.0725 |
| Ecoli                         | Distributive | 82.15   | 10.1325 |
| Ecoli                         | Gaussian     | 78.8229 | 13.678  |
| Glass Identification          | Distributive | 82.4842 | 10.0853 |
| Glass Identification          | Gaussian     | 78.3351 | 14.0021 |
| Iris                          | Distributive | 82.4344 | 10.1905 |
| Iris                          | Gaussian     | 77.3808 | 11.7752 |
| MAGIC Gamma Telescope         | Distributive | 82.6409 | 10.2531 |
| MAGIC Gamma Telescope         | Gaussian     | 79.265  | 13.4495 |
| Maternal Health Risk          | Distributive | 82.4276 | 10.312  |
| Maternal Health Risk          | Gaussian     | 78.9056 | 13.2961 |
| Statlog (Vehicle Silhouettes) | Distributive | 82.6089 | 10.2281 |
| Statlog (Vehicle Silhouettes) | Gaussian     | 78.8867 | 14.9435 |
| Wine Quality                  | Distributive | 82.516  | 10.2226 |
| Wine Quality                  | Gaussian     | 82.1112 | 11.0922 |

## Optimal Scatter Code Configurations

### DWN

| dataset       |   num_dimensions |   num_slices |    mean |      std | model   |
|:--------------|-----------------:|-------------:|--------:|---------:|:--------|
| EEG Eye State |               40 |           60 | 0.30355 | 0.111086 | DWN     |

### Wisard

| dataset   | num_dimensions   | num_slices   | mean   | std   | model   |
|-----------|------------------|--------------|--------|-------|---------|

## Delta Time Comparisons

### DWN

| dataset                       | encoding     |     mean |        std | model   |
|:------------------------------|:-------------|---------:|-----------:|:--------|
| EEG Eye State                 | Distributive | 23.9568  |   0.235679 | DWN     |
| EEG Eye State                 | Gaussian     |  5.44145 |   1.52346  | DWN     |
| EEG Eye State                 | Linear       |  6.66445 |   2.13963  | DWN     |
| EEG Eye State                 | Scatter Code |  5.00805 |   0.41387  | DWN     |
| Statlog (Vehicle Silhouettes) | Distributive | 47.0263  | nan        | DWN     |
| Statlog (Vehicle Silhouettes) | Gaussian     | 55.2602  | nan        | DWN     |
| Wine Quality                  | Distributive | 93.33    | nan        | DWN     |

### Wisard

| dataset                       | encoding     |     mean |      std | model   |
|:------------------------------|:-------------|---------:|---------:|:--------|
| EEG Eye State                 | Distributive | 0.708839 | 1.02784  | Wisard  |
| EEG Eye State                 | Gaussian     | 0.70497  | 1.4661   | Wisard  |
| Ecoli                         | Distributive | 0.69762  | 0.878445 | Wisard  |
| Ecoli                         | Gaussian     | 0.715519 | 0.942143 | Wisard  |
| Glass Identification          | Distributive | 0.864558 | 1.15913  | Wisard  |
| Glass Identification          | Gaussian     | 1.36821  | 1.7167   | Wisard  |
| Iris                          | Distributive | 0.664968 | 0.928399 | Wisard  |
| Iris                          | Gaussian     | 1.39253  | 2.07199  | Wisard  |
| MAGIC Gamma Telescope         | Distributive | 0.781757 | 0.998082 | Wisard  |
| MAGIC Gamma Telescope         | Gaussian     | 0.859193 | 1.48066  | Wisard  |
| Maternal Health Risk          | Distributive | 0.672899 | 0.990172 | Wisard  |
| Maternal Health Risk          | Gaussian     | 0.830652 | 1.24621  | Wisard  |
| Statlog (Vehicle Silhouettes) | Distributive | 0.80483  | 1.11475  | Wisard  |
| Statlog (Vehicle Silhouettes) | Gaussian     | 1.06487  | 1.72962  | Wisard  |
| Wine Quality                  | Distributive | 0.72508  | 0.986449 | Wisard  |
| Wine Quality                  | Gaussian     | 0.740531 | 1.56547  | Wisard  |
