# Analysis Conclusions

## All Encoding Results per Dataset and Model

### DWN: All Encoding Results

| Dataset                                   | Encoding     |   Mean Accuracy |   Standard Deviation |
|:------------------------------------------|:-------------|----------------:|---------------------:|
| EEG Eye State                             | Distributive |        0.670838 |          0.168982    |
| EEG Eye State                             | Gaussian     |        0.531973 |          0.0652197   |
| EEG Eye State                             | Linear       |        0.468429 |          0.0173497   |
| EEG Eye State                             | Scatter Code |        0.391391 |          0.0418419   |
| Ecoli                                     | Gaussian     |        0.883766 |          0.0758519   |
| Ecoli                                     | Linear       |        0.88207  |          0.0712779   |
| Ecoli                                     | Distributive |        0.866831 |          0.0748097   |
| Ecoli                                     | Scatter Code |        0.81786  |          0.238126    |
| Glass Identification                      | Distributive |        0.672927 |          0.0686677   |
| Glass Identification                      | Linear       |        0.64802  |          0.0664212   |
| Glass Identification                      | Gaussian     |        0.646944 |          0.0623693   |
| Glass Identification                      | Scatter Code |        0.435502 |          0.143701    |
| Iris                                      | Scatter Code |        0.8901   |          0.0832809   |
| Iris                                      | Linear       |        0.889    |          0.0775964   |
| Iris                                      | Gaussian     |        0.8875   |          0.0682864   |
| Iris                                      | Distributive |        0.879592 |          0.0619596   |
| MAGIC Gamma Telescope                     | Distributive |        0.817833 |          0.0107853   |
| MAGIC Gamma Telescope                     | Gaussian     |        0.749429 |          0.0842627   |
| MAGIC Gamma Telescope                     | Linear       |        0.566879 |          0.125439    |
| MAGIC Gamma Telescope                     | Scatter Code |        0.507004 |          0.0357073   |
| Maternal Health Risk                      | Distributive |        0.699238 |          0.0308345   |
| Maternal Health Risk                      | Linear       |        0.68458  |          0.0554077   |
| Maternal Health Risk                      | Gaussian     |        0.66092  |          0.0350307   |
| Maternal Health Risk                      | Scatter Code |        0.577552 |          0.117772    |
| Optical Recognition of Handwritten Digits | Gaussian     |        0.961398 |          0.0115518   |
| Optical Recognition of Handwritten Digits | Distributive |        0.96056  |          0.0122283   |
| Optical Recognition of Handwritten Digits | Linear       |        0.931338 |          0.0683993   |
| Optical Recognition of Handwritten Digits | Scatter Code |        0.791796 |          0.228489    |
| Statlog (Vehicle Silhouettes)             | Distributive |        0.721667 |          0.0275394   |
| Statlog (Vehicle Silhouettes)             | Gaussian     |        0.718769 |          0.0451677   |
| Statlog (Vehicle Silhouettes)             | Linear       |        0.69772  |          0.055821    |
| Statlog (Vehicle Silhouettes)             | Scatter Code |        0.258224 |          0.0817246   |
| Wine Quality                              | Scatter Code |        0.823822 |          0.0291919   |
| Wine Quality                              | Distributive |        0.47345  |          0.000353553 |

### Wisard: All Encoding Results

| Dataset               | Encoding     |   Mean Accuracy |   Standard Deviation |
|:----------------------|:-------------|----------------:|---------------------:|
| EEG Eye State         | Distributive |         84.2366 |              10.7034 |
| EEG Eye State         | Gaussian     |         80.546  |              13.7543 |
| EEG Eye State         | Linear       |         75.4598 |              16.7882 |
| EEG Eye State         | Scatter Code |         66.787  |              24.5737 |
| MAGIC Gamma Telescope | Distributive |         84.052  |              10.8001 |
| MAGIC Gamma Telescope | Gaussian     |         80.5873 |              13.8657 |
| MAGIC Gamma Telescope | Linear       |         75.08   |              16.8023 |
| MAGIC Gamma Telescope | Scatter Code |         38.9011 |              15.2349 |
| Maternal Health Risk  | Distributive |         88.32   |             nan      |
| Wine Quality          | Distributive |         93.46   |               0      |

## Best Encodings per Dataset

### DWN: Best Encoding for Each Dataset

| Dataset                                   | Best Encoding   |   Mean Accuracy |   Standard Deviation |
|:------------------------------------------|:----------------|----------------:|---------------------:|
| EEG Eye State                             | Distributive    |        0.670838 |            0.168982  |
| Ecoli                                     | Gaussian        |        0.883766 |            0.0758519 |
| Glass Identification                      | Distributive    |        0.672927 |            0.0686677 |
| Iris                                      | Scatter Code    |        0.8901   |            0.0832809 |
| MAGIC Gamma Telescope                     | Distributive    |        0.817833 |            0.0107853 |
| Maternal Health Risk                      | Distributive    |        0.699238 |            0.0308345 |
| Optical Recognition of Handwritten Digits | Gaussian        |        0.961398 |            0.0115518 |
| Statlog (Vehicle Silhouettes)             | Distributive    |        0.721667 |            0.0275394 |
| Wine Quality                              | Scatter Code    |        0.823822 |            0.0291919 |

### Wisard: Best Encoding for Each Dataset

| Dataset               | Best Encoding   |   Mean Accuracy |   Standard Deviation |
|:----------------------|:----------------|----------------:|---------------------:|
| EEG Eye State         | Distributive    |         84.2366 |              10.7034 |
| MAGIC Gamma Telescope | Distributive    |         84.052  |              10.8001 |
| Maternal Health Risk  | Distributive    |         88.32   |             nan      |
| Wine Quality          | Distributive    |         93.46   |               0      |

## Optimal Scatter Code Configurations

### DWN

| dataset                                   |   num_dimensions |   num_slices |     mean |         std | model   |
|:------------------------------------------|-----------------:|-------------:|---------:|------------:|:--------|
| EEG Eye State                             |               50 |           10 | 0.39228  | 0.0497562   | DWN     |
| EEG Eye State                             |               50 |           50 | 0.39264  | 0.0351055   | DWN     |
| EEG Eye State                             |               50 |          100 | 0.39862  | 0.0778861   | DWN     |
| EEG Eye State                             |              100 |           10 | 0.36988  | 0.0417887   | DWN     |
| EEG Eye State                             |              100 |           50 | 0.37352  | 0.0204551   | DWN     |
| EEG Eye State                             |              100 |          100 | 0.41298  | 0.0395531   | DWN     |
| EEG Eye State                             |              200 |           10 | 0.37446  | 0.0378118   | DWN     |
| EEG Eye State                             |              200 |           50 | 0.3825   | 0.0231161   | DWN     |
| EEG Eye State                             |              200 |          100 | 0.42564  | 0.0154515   | DWN     |
| Ecoli                                     |               50 |           10 | 0.88951  | 0.0717762   | DWN     |
| Ecoli                                     |               50 |          100 | 0.31295  | 0.124479    | DWN     |
| Ecoli                                     |              100 |           10 | 0.89341  | 0.0648675   | DWN     |
| Ecoli                                     |              100 |           50 | 0.8993   | 0.0827105   | DWN     |
| Ecoli                                     |              100 |          100 | 0.949967 | 0.0642682   | DWN     |
| Ecoli                                     |              200 |           10 | 0.9018   | 0.101847    | DWN     |
| Ecoli                                     |              200 |           50 | 0.96     | 0.034641    | DWN     |
| Ecoli                                     |              200 |          100 | 0.968    | 0.0303315   | DWN     |
| Glass Identification                      |               50 |           10 | 0.40935  | 0.161843    | DWN     |
| Glass Identification                      |               50 |           50 | 0.51832  | 0.044988    | DWN     |
| Glass Identification                      |               50 |          100 | 0.2845   | 0.12887     | DWN     |
| Glass Identification                      |              100 |           10 | 0.32954  | 0.00772289  | DWN     |
| Glass Identification                      |              100 |           50 | 0.50138  | 0.0830696   | DWN     |
| Glass Identification                      |              100 |          100 | 0.58308  | 0.074897    | DWN     |
| Glass Identification                      |              200 |           10 | 0.25352  | 0.115716    | DWN     |
| Glass Identification                      |              200 |           50 | 0.5183   | 0.0720901   | DWN     |
| Glass Identification                      |              200 |          100 | 0.52676  | 0.067981    | DWN     |
| Iris                                      |               50 |           50 | 0.8901   | 0.0832809   | DWN     |
| MAGIC Gamma Telescope                     |               50 |           10 | 0.496533 | 0.0500824   | DWN     |
| MAGIC Gamma Telescope                     |               50 |           50 | 0.49312  | 0.0375008   | DWN     |
| MAGIC Gamma Telescope                     |               50 |          100 | 0.50688  | 0.0376833   | DWN     |
| MAGIC Gamma Telescope                     |              100 |           10 | 0.53428  | 0.000109545 | DWN     |
| MAGIC Gamma Telescope                     |              100 |           50 | 0.50684  | 0.0375557   | DWN     |
| MAGIC Gamma Telescope                     |              100 |          100 | 0.47944  | 0.0307237   | DWN     |
| MAGIC Gamma Telescope                     |              200 |           10 | 0.5206   | 0.0306343   | DWN     |
| MAGIC Gamma Telescope                     |              200 |           50 | 0.50688  | 0.0375008   | DWN     |
| MAGIC Gamma Telescope                     |              200 |          100 | 0.52056  | 0.0306119   | DWN     |
| Maternal Health Risk                      |               50 |           10 | 0.564757 | 0.0955427   | DWN     |
| Maternal Health Risk                      |               50 |           50 | 0.6036   | 0.0471238   | DWN     |
| Maternal Health Risk                      |               50 |          100 | 0.2979   | 0.0605233   | DWN     |
| Maternal Health Risk                      |              100 |           10 | 0.53436  | 0.0415246   | DWN     |
| Maternal Health Risk                      |              100 |           50 | 0.6394   | 0.038908    | DWN     |
| Maternal Health Risk                      |              100 |          100 | 0.6567   | 0.0209036   | DWN     |
| Maternal Health Risk                      |              200 |           10 | 0.57492  | 0.0343947   | DWN     |
| Maternal Health Risk                      |              200 |           50 | 0.6579   | 0.00622093  | DWN     |
| Maternal Health Risk                      |              200 |          100 | 0.65755  | 0.074781    | DWN     |
| Optical Recognition of Handwritten Digits |               50 |           10 | 0.96304  | 0.0117249   | DWN     |
| Optical Recognition of Handwritten Digits |               50 |           50 | 0.85806  | 0.112295    | DWN     |
| Optical Recognition of Handwritten Digits |               50 |          100 | 0.31402  | 0.251983    | DWN     |
| Optical Recognition of Handwritten Digits |              100 |           10 | 0.80038  | 0.188073    | DWN     |
| Optical Recognition of Handwritten Digits |              100 |           50 | 0.86093  | 0.109666    | DWN     |
| Optical Recognition of Handwritten Digits |              100 |          100 | 0.87364  | 0.0938735   | DWN     |
| Optical Recognition of Handwritten Digits |              200 |           10 | 0.81649  | 0.163981    | DWN     |
| Optical Recognition of Handwritten Digits |              200 |           50 | 0.85612  | 0.112626    | DWN     |
| Optical Recognition of Handwritten Digits |              200 |          100 | 0.8777   | 0.101855    | DWN     |
| Statlog (Vehicle Silhouettes)             |               50 |           10 | 0.297567 | 0.214843    | DWN     |
| Statlog (Vehicle Silhouettes)             |               50 |           50 | 0.25858  | 0.0432092   | DWN     |
| Statlog (Vehicle Silhouettes)             |               50 |          100 | 0.245    | 0.0402983   | DWN     |
| Statlog (Vehicle Silhouettes)             |              100 |           10 | 0.27     | 0.039502    | DWN     |
| Statlog (Vehicle Silhouettes)             |              100 |           50 | 0.22858  | 0.0380668   | DWN     |
| Statlog (Vehicle Silhouettes)             |              100 |          100 | 0.27068  | 0.0255359   | DWN     |
| Statlog (Vehicle Silhouettes)             |              200 |           10 | 0.245    | 0.0402983   | DWN     |
| Statlog (Vehicle Silhouettes)             |              200 |           50 | 0.25858  | 0.0432092   | DWN     |
| Statlog (Vehicle Silhouettes)             |              200 |          100 | 0.24216  | 0.0474302   | DWN     |
| Wine Quality                              |              100 |           50 | 0.84235  | 0.0446184   | DWN     |
| Wine Quality                              |              100 |          100 | 0.82885  | 0.0382388   | DWN     |
| Wine Quality                              |              200 |           10 | 0.8243   | 0.0190919   | DWN     |
| Wine Quality                              |              200 |           50 | 0.83242  | 0.0197591   | DWN     |
| Wine Quality                              |              200 |          100 | 0.8036   | 0.0272984   | DWN     |

### Wisard

| dataset               |   num_dimensions |   num_slices |    mean |     std | model   |
|:----------------------|-----------------:|-------------:|--------:|--------:|:--------|
| EEG Eye State         |               50 |           10 | 64.2493 | 25.3507 | Wisard  |
| EEG Eye State         |               50 |           50 | 67.2769 | 24.1698 | Wisard  |
| EEG Eye State         |              100 |           10 | 65.0391 | 25.5338 | Wisard  |
| EEG Eye State         |              100 |           50 | 67.512  | 24.5092 | Wisard  |
| EEG Eye State         |              100 |          100 | 68.3231 | 24.0081 | Wisard  |
| EEG Eye State         |              200 |           10 | 65.3567 | 25.7517 | Wisard  |
| EEG Eye State         |              200 |           50 | 67.8911 | 24.4775 | Wisard  |
| EEG Eye State         |              200 |          100 | 68.648  | 24.2698 | Wisard  |
| MAGIC Gamma Telescope |               50 |          100 | 38.9011 | 15.2349 | Wisard  |

## Delta Time Comparisons

### DWN

| dataset                                   | encoding     |      mean |        std | model   |
|:------------------------------------------|:-------------|----------:|-----------:|:--------|
| EEG Eye State                             | Distributive | 2.53559   | 1.3813     | DWN     |
| EEG Eye State                             | Gaussian     | 2.21718   | 1.59004    | DWN     |
| EEG Eye State                             | Linear       | 1.35563   | 0.376545   | DWN     |
| EEG Eye State                             | Scatter Code | 1.84046   | 0.519888   | DWN     |
| Ecoli                                     | Distributive | 0.113467  | 0.195339   | DWN     |
| Ecoli                                     | Gaussian     | 0.0645825 | 0.0406741  | DWN     |
| Ecoli                                     | Linear       | 0.04835   | 0.0185671  | DWN     |
| Ecoli                                     | Scatter Code | 0.0504081 | 0.0151289  | DWN     |
| Glass Identification                      | Distributive | 0.0598711 | 0.01968    | DWN     |
| Glass Identification                      | Gaussian     | 0.05608   | 0.0158095  | DWN     |
| Glass Identification                      | Linear       | 0.32632   | 0.913121   | DWN     |
| Glass Identification                      | Scatter Code | 0.176093  | 0.680753   | DWN     |
| Iris                                      | Distributive | 0.056875  | 0.0219791  | DWN     |
| Iris                                      | Gaussian     | 0.06253   | 0.0185407  | DWN     |
| Iris                                      | Linear       | 0.05956   | 0.0147264  | DWN     |
| Iris                                      | Scatter Code | 0.05626   | 0.00991343 | DWN     |
| MAGIC Gamma Telescope                     | Distributive | 4.33384   | 2.46773    | DWN     |
| MAGIC Gamma Telescope                     | Gaussian     | 4.57106   | 2.4018     | DWN     |
| MAGIC Gamma Telescope                     | Linear       | 3.7014    | 1.6476     | DWN     |
| MAGIC Gamma Telescope                     | Scatter Code | 4.73667   | 2.08317    | DWN     |
| Maternal Health Risk                      | Distributive | 0.203769  | 0.083458   | DWN     |
| Maternal Health Risk                      | Gaussian     | 0.289617  | 0.554003   | DWN     |
| Maternal Health Risk                      | Linear       | 0.855398  | 1.81928    | DWN     |
| Maternal Health Risk                      | Scatter Code | 0.544627  | 1.06897    | DWN     |
| Optical Recognition of Handwritten Digits | Distributive | 1.47547   | 0.599556   | DWN     |
| Optical Recognition of Handwritten Digits | Gaussian     | 1.33334   | 0.443013   | DWN     |
| Optical Recognition of Handwritten Digits | Linear       | 1.67349   | 1.00618    | DWN     |
| Optical Recognition of Handwritten Digits | Scatter Code | 4.64285   | 2.72112    | DWN     |
| Statlog (Vehicle Silhouettes)             | Distributive | 0.251982  | 0.283948   | DWN     |
| Statlog (Vehicle Silhouettes)             | Gaussian     | 0.451169  | 0.84443    | DWN     |
| Statlog (Vehicle Silhouettes)             | Linear       | 1.02427   | 2.85216    | DWN     |
| Statlog (Vehicle Silhouettes)             | Scatter Code | 0.433513  | 0.643369   | DWN     |
| Wine Quality                              | Distributive | 0.79585   | 0.333684   | DWN     |
| Wine Quality                              | Scatter Code | 0.109     | 0.0269812  | DWN     |

### Wisard

| dataset               | encoding     |       mean |          std | model   |
|:----------------------|:-------------|-----------:|-------------:|:--------|
| EEG Eye State         | Distributive |   0.323578 |   0.393822   | Wisard  |
| EEG Eye State         | Gaussian     |   0.427809 |   0.567728   | Wisard  |
| EEG Eye State         | Linear       |   4.40309  |   9.03771    | Wisard  |
| EEG Eye State         | Scatter Code | 118.855    | 191.875      | Wisard  |
| MAGIC Gamma Telescope | Distributive |   0.364198 |   0.470017   | Wisard  |
| MAGIC Gamma Telescope | Gaussian     |   0.457798 |   0.555169   | Wisard  |
| MAGIC Gamma Telescope | Linear       |   7.17956  |  13.1012     | Wisard  |
| MAGIC Gamma Telescope | Scatter Code | 114.144    | 158.119      | Wisard  |
| Maternal Health Risk  | Distributive |   0.0172   | nan          | Wisard  |
| Wine Quality          | Distributive |   0.01695  |   0.00770746 | Wisard  |
## Scatter Code Accuracy by Dataset

### DWN: Mean Accuracy and Standard Deviation for Scatter Code Configurations

| Dataset                                   |   Num Slices |   Num Dimensions |   Mean Accuracy |   Standard Deviation |
|:------------------------------------------|-------------:|-----------------:|----------------:|---------------------:|
| EEG Eye State                             |           10 |               50 |           0.392 |                0.05  |
| EEG Eye State                             |           50 |               50 |           0.393 |                0.035 |
| EEG Eye State                             |          100 |               50 |           0.399 |                0.078 |
| EEG Eye State                             |           10 |              100 |           0.37  |                0.042 |
| EEG Eye State                             |           50 |              100 |           0.374 |                0.02  |
| EEG Eye State                             |          100 |              100 |           0.413 |                0.04  |
| EEG Eye State                             |           10 |              200 |           0.374 |                0.038 |
| EEG Eye State                             |           50 |              200 |           0.382 |                0.023 |
| EEG Eye State                             |          100 |              200 |           0.426 |                0.015 |
| Ecoli                                     |           10 |               50 |           0.89  |                0.072 |
| Ecoli                                     |          100 |               50 |           0.313 |                0.124 |
| Ecoli                                     |           10 |              100 |           0.893 |                0.065 |
| Ecoli                                     |           50 |              100 |           0.899 |                0.083 |
| Ecoli                                     |          100 |              100 |           0.95  |                0.064 |
| Ecoli                                     |           10 |              200 |           0.902 |                0.102 |
| Ecoli                                     |           50 |              200 |           0.96  |                0.035 |
| Ecoli                                     |          100 |              200 |           0.968 |                0.03  |
| Glass Identification                      |           10 |               50 |           0.409 |                0.162 |
| Glass Identification                      |           50 |               50 |           0.518 |                0.045 |
| Glass Identification                      |          100 |               50 |           0.285 |                0.129 |
| Glass Identification                      |           10 |              100 |           0.33  |                0.008 |
| Glass Identification                      |           50 |              100 |           0.501 |                0.083 |
| Glass Identification                      |          100 |              100 |           0.583 |                0.075 |
| Glass Identification                      |           10 |              200 |           0.254 |                0.116 |
| Glass Identification                      |           50 |              200 |           0.518 |                0.072 |
| Glass Identification                      |          100 |              200 |           0.527 |                0.068 |
| Iris                                      |           50 |               50 |           0.89  |                0.083 |
| MAGIC Gamma Telescope                     |           10 |               50 |           0.497 |                0.05  |
| MAGIC Gamma Telescope                     |           50 |               50 |           0.493 |                0.038 |
| MAGIC Gamma Telescope                     |          100 |               50 |           0.507 |                0.038 |
| MAGIC Gamma Telescope                     |           10 |              100 |           0.534 |                0     |
| MAGIC Gamma Telescope                     |           50 |              100 |           0.507 |                0.038 |
| MAGIC Gamma Telescope                     |          100 |              100 |           0.479 |                0.031 |
| MAGIC Gamma Telescope                     |           10 |              200 |           0.521 |                0.031 |
| MAGIC Gamma Telescope                     |           50 |              200 |           0.507 |                0.038 |
| MAGIC Gamma Telescope                     |          100 |              200 |           0.521 |                0.031 |
| Maternal Health Risk                      |           10 |               50 |           0.565 |                0.096 |
| Maternal Health Risk                      |           50 |               50 |           0.604 |                0.047 |
| Maternal Health Risk                      |          100 |               50 |           0.298 |                0.061 |
| Maternal Health Risk                      |           10 |              100 |           0.534 |                0.042 |
| Maternal Health Risk                      |           50 |              100 |           0.639 |                0.039 |
| Maternal Health Risk                      |          100 |              100 |           0.657 |                0.021 |
| Maternal Health Risk                      |           10 |              200 |           0.575 |                0.034 |
| Maternal Health Risk                      |           50 |              200 |           0.658 |                0.006 |
| Maternal Health Risk                      |          100 |              200 |           0.658 |                0.075 |
| Optical Recognition of Handwritten Digits |           10 |               50 |           0.963 |                0.012 |
| Optical Recognition of Handwritten Digits |           50 |               50 |           0.858 |                0.112 |
| Optical Recognition of Handwritten Digits |          100 |               50 |           0.314 |                0.252 |
| Optical Recognition of Handwritten Digits |           10 |              100 |           0.8   |                0.188 |
| Optical Recognition of Handwritten Digits |           50 |              100 |           0.861 |                0.11  |
| Optical Recognition of Handwritten Digits |          100 |              100 |           0.874 |                0.094 |
| Optical Recognition of Handwritten Digits |           10 |              200 |           0.816 |                0.164 |
| Optical Recognition of Handwritten Digits |           50 |              200 |           0.856 |                0.113 |
| Optical Recognition of Handwritten Digits |          100 |              200 |           0.878 |                0.102 |
| Statlog (Vehicle Silhouettes)             |           10 |               50 |           0.298 |                0.215 |
| Statlog (Vehicle Silhouettes)             |           50 |               50 |           0.259 |                0.043 |
| Statlog (Vehicle Silhouettes)             |          100 |               50 |           0.245 |                0.04  |
| Statlog (Vehicle Silhouettes)             |           10 |              100 |           0.27  |                0.04  |
| Statlog (Vehicle Silhouettes)             |           50 |              100 |           0.229 |                0.038 |
| Statlog (Vehicle Silhouettes)             |          100 |              100 |           0.271 |                0.026 |
| Statlog (Vehicle Silhouettes)             |           10 |              200 |           0.245 |                0.04  |
| Statlog (Vehicle Silhouettes)             |           50 |              200 |           0.259 |                0.043 |
| Statlog (Vehicle Silhouettes)             |          100 |              200 |           0.242 |                0.047 |
| Wine Quality                              |           50 |              100 |           0.842 |                0.045 |
| Wine Quality                              |          100 |              100 |           0.829 |                0.038 |
| Wine Quality                              |           10 |              200 |           0.824 |                0.019 |
| Wine Quality                              |           50 |              200 |           0.832 |                0.02  |
| Wine Quality                              |          100 |              200 |           0.804 |                0.027 |

### Wisard: Mean Accuracy and Standard Deviation for Scatter Code Configurations

| Dataset               |   Num Slices |   Num Dimensions |   Mean Accuracy |   Standard Deviation |
|:----------------------|-------------:|-----------------:|----------------:|---------------------:|
| EEG Eye State         |           10 |               50 |          64.249 |               25.351 |
| EEG Eye State         |           50 |               50 |          67.277 |               24.17  |
| EEG Eye State         |           10 |              100 |          65.039 |               25.534 |
| EEG Eye State         |           50 |              100 |          67.512 |               24.509 |
| EEG Eye State         |          100 |              100 |          68.323 |               24.008 |
| EEG Eye State         |           10 |              200 |          65.357 |               25.752 |
| EEG Eye State         |           50 |              200 |          67.891 |               24.478 |
| EEG Eye State         |          100 |              200 |          68.648 |               24.27  |
| MAGIC Gamma Telescope |          100 |               50 |          38.901 |               15.235 |

