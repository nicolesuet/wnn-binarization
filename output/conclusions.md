# Analysis Conclusions

## All Encoding Results per Dataset and Model

### DWN: All Encoding Results

| Dataset   | Encoding   | Mean Accuracy   | Standard Deviation   |
|-----------|------------|-----------------|----------------------|

### Wisard: All Encoding Results

| Dataset                                   | Encoding     |   Mean Accuracy |   Standard Deviation |
|:------------------------------------------|:-------------|----------------:|---------------------:|
| Ecoli                                     | Gaussian     |         84.68   |              0       |
| Ecoli                                     | Linear       |         84.68   |              0       |
| Ecoli                                     | Scatter Code |         82.2833 |             13.016   |
| Ecoli                                     | Distributive |         81.98   |              0       |
| Glass Identification                      | Gaussian     |         76.06   |              0       |
| Glass Identification                      | Distributive |         70.42   |              0       |
| Glass Identification                      | Linear       |         70.42   |              0       |
| Glass Identification                      | Scatter Code |         47.8856 |             13.6196  |
| Image Segmentation                        | Distributive |         84.29   |              0       |
| Image Segmentation                        | Gaussian     |         82.86   |              0       |
| Image Segmentation                        | Linear       |         82.86   |              0       |
| Image Segmentation                        | Scatter Code |         59.0478 |             21.3284  |
| Iris                                      | Gaussian     |         98      |              0       |
| Iris                                      | Linear       |         98      |              0       |
| Iris                                      | Scatter Code |         90.6667 |             21.599   |
| Iris                                      | Distributive |         88      |              0       |
| Maternal Health Risk                      | Distributive |         75.82   |              0       |
| Maternal Health Risk                      | Gaussian     |         74.93   |              0       |
| Maternal Health Risk                      | Linear       |         72.24   |              0       |
| Maternal Health Risk                      | Scatter Code |         62.4867 |              9.13355 |
| Optical Recognition of Handwritten Digits | Linear       |         97.41   |              0       |
| Optical Recognition of Handwritten Digits | Gaussian     |         96.71   |              0       |
| Optical Recognition of Handwritten Digits | Distributive |         95.74   |              0       |
| Optical Recognition of Handwritten Digits | Scatter Code |         88.0322 |             27.6369  |
| Statlog (Vehicle Silhouettes)             | Distributive |         72.14   |              0       |
| Statlog (Vehicle Silhouettes)             | Gaussian     |         68.21   |              0       |
| Statlog (Vehicle Silhouettes)             | Linear       |         62.5    |              0       |
| Statlog (Vehicle Silhouettes)             | Scatter Code |         20      |              0       |
| Wine Quality                              | Distributive |         61.54   |              0       |
| Wine Quality                              | Gaussian     |         59.81   |              0       |
| Wine Quality                              | Linear       |         49.04   |              0       |
| Wine Quality                              | Scatter Code |         42.4133 |              2.041   |

## Best Encodings per Dataset

### DWN: Best Encoding for Each Dataset

| Dataset   | Best Encoding   | Mean Accuracy   | Standard Deviation   |
|-----------|-----------------|-----------------|----------------------|

### Wisard: Best Encoding for Each Dataset

| Dataset                                   | Best Encoding   |   Mean Accuracy |   Standard Deviation |
|:------------------------------------------|:----------------|----------------:|---------------------:|
| Ecoli                                     | Gaussian        |           84.68 |                    0 |
| Glass Identification                      | Gaussian        |           76.06 |                    0 |
| Image Segmentation                        | Distributive    |           84.29 |                    0 |
| Iris                                      | Gaussian        |           98    |                    0 |
| Maternal Health Risk                      | Distributive    |           75.82 |                    0 |
| Optical Recognition of Handwritten Digits | Linear          |           97.41 |                    0 |
| Statlog (Vehicle Silhouettes)             | Distributive    |           72.14 |                    0 |
| Wine Quality                              | Distributive    |           61.54 |                    0 |

## Optimal Scatter Code Configurations

### DWN

| dataset   | num_dimensions   | num_slices   | mean   | std   | model   |
|-----------|------------------|--------------|--------|-------|---------|

### Wisard

| dataset                                   |   num_dimensions |   num_slices |   mean |   std | model   |
|:------------------------------------------|-----------------:|-------------:|-------:|------:|:--------|
| Ecoli                                     |               50 |           10 |  87.39 |     0 | Wisard  |
| Ecoli                                     |               50 |           50 |  83.78 |     0 | Wisard  |
| Ecoli                                     |               50 |          100 |  45.95 |     0 | Wisard  |
| Ecoli                                     |              100 |           10 |  88.29 |     0 | Wisard  |
| Ecoli                                     |              100 |           50 |  87.39 |     0 | Wisard  |
| Ecoli                                     |              100 |          100 |  84.68 |     0 | Wisard  |
| Ecoli                                     |              200 |           10 |  89.19 |     0 | Wisard  |
| Ecoli                                     |              200 |           50 |  86.49 |     0 | Wisard  |
| Ecoli                                     |              200 |          100 |  87.39 |     0 | Wisard  |
| Glass Identification                      |               50 |           10 |  32.39 |     0 | Wisard  |
| Glass Identification                      |               50 |           50 |  54.93 |     0 | Wisard  |
| Glass Identification                      |               50 |          100 |  35.21 |     0 | Wisard  |
| Glass Identification                      |              100 |           10 |  32.39 |     0 | Wisard  |
| Glass Identification                      |              100 |           50 |  59.15 |     0 | Wisard  |
| Glass Identification                      |              100 |          100 |  66.2  |     0 | Wisard  |
| Glass Identification                      |              200 |           10 |  32.39 |     0 | Wisard  |
| Glass Identification                      |              200 |           50 |  57.75 |     0 | Wisard  |
| Glass Identification                      |              200 |          100 |  60.56 |     0 | Wisard  |
| Image Segmentation                        |               50 |           10 |  51.43 |     0 | Wisard  |
| Image Segmentation                        |               50 |           50 |  68.57 |     0 | Wisard  |
| Image Segmentation                        |               50 |          100 |  10    |     0 | Wisard  |
| Image Segmentation                        |              100 |           10 |  51.43 |     0 | Wisard  |
| Image Segmentation                        |              100 |           50 |  75.71 |     0 | Wisard  |
| Image Segmentation                        |              100 |          100 |  74.29 |     0 | Wisard  |
| Image Segmentation                        |              200 |           10 |  44.29 |     0 | Wisard  |
| Image Segmentation                        |              200 |           50 |  77.14 |     0 | Wisard  |
| Image Segmentation                        |              200 |          100 |  78.57 |     0 | Wisard  |
| Iris                                      |               50 |           10 |  98    |     0 | Wisard  |
| Iris                                      |               50 |           50 |  98    |     0 | Wisard  |
| Iris                                      |               50 |          100 |  30    |     0 | Wisard  |
| Iris                                      |              100 |           10 |  98    |     0 | Wisard  |
| Iris                                      |              100 |           50 | 100    |     0 | Wisard  |
| Iris                                      |              100 |          100 |  98    |     0 | Wisard  |
| Iris                                      |              200 |           10 | 100    |     0 | Wisard  |
| Iris                                      |              200 |           50 |  96    |     0 | Wisard  |
| Iris                                      |              200 |          100 |  98    |     0 | Wisard  |
| Maternal Health Risk                      |               50 |           10 |  60.3  |     0 | Wisard  |
| Maternal Health Risk                      |               50 |           50 |  65.67 |     0 | Wisard  |
| Maternal Health Risk                      |               50 |          100 |  38.21 |     0 | Wisard  |
| Maternal Health Risk                      |              100 |           10 |  63.88 |     0 | Wisard  |
| Maternal Health Risk                      |              100 |           50 |  65.67 |     0 | Wisard  |
| Maternal Health Risk                      |              100 |          100 |  67.16 |     0 | Wisard  |
| Maternal Health Risk                      |              200 |           10 |  62.09 |     0 | Wisard  |
| Maternal Health Risk                      |              200 |           50 |  69.85 |     0 | Wisard  |
| Maternal Health Risk                      |              200 |          100 |  69.55 |     0 | Wisard  |
| Optical Recognition of Handwritten Digits |               50 |           10 |  97.79 |     0 | Wisard  |
| Optical Recognition of Handwritten Digits |               50 |           50 |  97.68 |     0 | Wisard  |
| Optical Recognition of Handwritten Digits |               50 |          100 |  10.3  |     0 | Wisard  |
| Optical Recognition of Handwritten Digits |              100 |           10 |  97.52 |     0 | Wisard  |
| Optical Recognition of Handwritten Digits |              100 |           50 |  97.84 |     0 | Wisard  |
| Optical Recognition of Handwritten Digits |              100 |          100 |  97.95 |     0 | Wisard  |
| Optical Recognition of Handwritten Digits |              200 |           10 |  97.47 |     0 | Wisard  |
| Optical Recognition of Handwritten Digits |              200 |           50 |  97.9  |     0 | Wisard  |
| Optical Recognition of Handwritten Digits |              200 |          100 |  97.84 |     0 | Wisard  |
| Statlog (Vehicle Silhouettes)             |               50 |           10 |  20    |     0 | Wisard  |
| Statlog (Vehicle Silhouettes)             |               50 |           50 |  20    |     0 | Wisard  |
| Statlog (Vehicle Silhouettes)             |               50 |          100 |  20    |     0 | Wisard  |
| Statlog (Vehicle Silhouettes)             |              100 |           10 |  20    |     0 | Wisard  |
| Statlog (Vehicle Silhouettes)             |              100 |           50 |  20    |     0 | Wisard  |
| Statlog (Vehicle Silhouettes)             |              100 |          100 |  20    |     0 | Wisard  |
| Statlog (Vehicle Silhouettes)             |              200 |           10 |  20    |     0 | Wisard  |
| Statlog (Vehicle Silhouettes)             |              200 |           50 |  20    |     0 | Wisard  |
| Statlog (Vehicle Silhouettes)             |              200 |          100 |  20    |     0 | Wisard  |
| Wine Quality                              |               50 |           10 |  40.09 |     0 | Wisard  |
| Wine Quality                              |               50 |           50 |  41.72 |     0 | Wisard  |
| Wine Quality                              |               50 |          100 |  45.55 |     0 | Wisard  |
| Wine Quality                              |              100 |           10 |  42.8  |     0 | Wisard  |
| Wine Quality                              |              100 |           50 |  40    |     0 | Wisard  |
| Wine Quality                              |              100 |          100 |  44.52 |     0 | Wisard  |
| Wine Quality                              |              200 |           10 |  44.2  |     0 | Wisard  |
| Wine Quality                              |              200 |           50 |  39.72 |     0 | Wisard  |
| Wine Quality                              |              200 |          100 |  43.12 |     0 | Wisard  |

## Delta Time Comparisons

### DWN

| dataset   | encoding   | mean   | std   | model   |
|-----------|------------|--------|-------|---------|

### Wisard

| dataset                                   | encoding     |        mean |          std | model   |
|:------------------------------------------|:-------------|------------:|-------------:|:--------|
| Ecoli                                     | Distributive |  0.00376    |  0.000374759 | Wisard  |
| Ecoli                                     | Gaussian     |  0.00357    |  0.0003093   | Wisard  |
| Ecoli                                     | Linear       |  0.00382    |  0.00110935  | Wisard  |
| Ecoli                                     | Scatter Code |  0.0148178  |  0.0125427   | Wisard  |
| Glass Identification                      | Distributive |  0.00364    |  0.000271621 | Wisard  |
| Glass Identification                      | Gaussian     |  0.00322    |  0.000248551 | Wisard  |
| Glass Identification                      | Linear       |  0.00343    |  0.000340098 | Wisard  |
| Glass Identification                      | Scatter Code |  0.0260311  |  0.0212795   | Wisard  |
| Image Segmentation                        | Distributive |  0.0045     |  0.000266667 | Wisard  |
| Image Segmentation                        | Gaussian     |  0.00494    |  0.000688315 | Wisard  |
| Image Segmentation                        | Linear       |  0.0046     |  0.000249444 | Wisard  |
| Image Segmentation                        | Scatter Code |  0.02751    |  0.0174722   | Wisard  |
| Iris                                      | Distributive |  0.00205    |  9.71825e-05 | Wisard  |
| Iris                                      | Gaussian     |  0.00203    |  0.000205751 | Wisard  |
| Iris                                      | Linear       |  0.0022     |  0.000188562 | Wisard  |
| Iris                                      | Scatter Code |  0.00429889 |  0.00165899  | Wisard  |
| Maternal Health Risk                      | Distributive |  0.00725    |  0.000715309 | Wisard  |
| Maternal Health Risk                      | Gaussian     |  0.00774    |  0.00118434  | Wisard  |
| Maternal Health Risk                      | Linear       |  0.00769    |  0.00119206  | Wisard  |
| Maternal Health Risk                      | Scatter Code |  0.0636911  |  0.0759833   | Wisard  |
| Optical Recognition of Handwritten Digits | Distributive |  0.45922    |  0.0693184   | Wisard  |
| Optical Recognition of Handwritten Digits | Gaussian     |  0.34811    |  0.0127333   | Wisard  |
| Optical Recognition of Handwritten Digits | Linear       |  0.37047    |  0.0749708   | Wisard  |
| Optical Recognition of Handwritten Digits | Scatter Code | 14.1097     | 33.0073      | Wisard  |
| Statlog (Vehicle Silhouettes)             | Distributive |  0.01259    |  0.000747514 | Wisard  |
| Statlog (Vehicle Silhouettes)             | Gaussian     |  0.0121     |  0.000946338 | Wisard  |
| Statlog (Vehicle Silhouettes)             | Linear       |  0.01283    |  0.000535516 | Wisard  |
| Statlog (Vehicle Silhouettes)             | Scatter Code |  1.38447    |  1.0485      | Wisard  |
| Wine Quality                              | Distributive |  0.06923    |  0.00513659  | Wisard  |
| Wine Quality                              | Gaussian     |  0.08184    |  0.0528082   | Wisard  |
| Wine Quality                              | Linear       |  0.13471    |  0.0414216   | Wisard  |
| Wine Quality                              | Scatter Code | 10.3949     |  9.02004     | Wisard  |
## Scatter Code Accuracy by Dataset

### DWN: Mean Accuracy and Standard Deviation for Scatter Code Configurations

| Dataset   | Num Slices   | Num Dimensions   | Mean Accuracy   | Standard Deviation   |
|-----------|--------------|------------------|-----------------|----------------------|

### Wisard: Mean Accuracy and Standard Deviation for Scatter Code Configurations

| Dataset                                   |   Num Slices |   Num Dimensions |   Mean Accuracy |   Standard Deviation |
|:------------------------------------------|-------------:|-----------------:|----------------:|---------------------:|
| Ecoli                                     |           10 |               50 |           87.39 |                    0 |
| Ecoli                                     |           50 |               50 |           83.78 |                    0 |
| Ecoli                                     |          100 |               50 |           45.95 |                    0 |
| Ecoli                                     |           10 |              100 |           88.29 |                    0 |
| Ecoli                                     |           50 |              100 |           87.39 |                    0 |
| Ecoli                                     |          100 |              100 |           84.68 |                    0 |
| Ecoli                                     |           10 |              200 |           89.19 |                    0 |
| Ecoli                                     |           50 |              200 |           86.49 |                    0 |
| Ecoli                                     |          100 |              200 |           87.39 |                    0 |
| Glass Identification                      |           10 |               50 |           32.39 |                    0 |
| Glass Identification                      |           50 |               50 |           54.93 |                    0 |
| Glass Identification                      |          100 |               50 |           35.21 |                    0 |
| Glass Identification                      |           10 |              100 |           32.39 |                    0 |
| Glass Identification                      |           50 |              100 |           59.15 |                    0 |
| Glass Identification                      |          100 |              100 |           66.2  |                    0 |
| Glass Identification                      |           10 |              200 |           32.39 |                    0 |
| Glass Identification                      |           50 |              200 |           57.75 |                    0 |
| Glass Identification                      |          100 |              200 |           60.56 |                    0 |
| Image Segmentation                        |           10 |               50 |           51.43 |                    0 |
| Image Segmentation                        |           50 |               50 |           68.57 |                    0 |
| Image Segmentation                        |          100 |               50 |           10    |                    0 |
| Image Segmentation                        |           10 |              100 |           51.43 |                    0 |
| Image Segmentation                        |           50 |              100 |           75.71 |                    0 |
| Image Segmentation                        |          100 |              100 |           74.29 |                    0 |
| Image Segmentation                        |           10 |              200 |           44.29 |                    0 |
| Image Segmentation                        |           50 |              200 |           77.14 |                    0 |
| Image Segmentation                        |          100 |              200 |           78.57 |                    0 |
| Iris                                      |           10 |               50 |           98    |                    0 |
| Iris                                      |           50 |               50 |           98    |                    0 |
| Iris                                      |          100 |               50 |           30    |                    0 |
| Iris                                      |           10 |              100 |           98    |                    0 |
| Iris                                      |           50 |              100 |          100    |                    0 |
| Iris                                      |          100 |              100 |           98    |                    0 |
| Iris                                      |           10 |              200 |          100    |                    0 |
| Iris                                      |           50 |              200 |           96    |                    0 |
| Iris                                      |          100 |              200 |           98    |                    0 |
| Maternal Health Risk                      |           10 |               50 |           60.3  |                    0 |
| Maternal Health Risk                      |           50 |               50 |           65.67 |                    0 |
| Maternal Health Risk                      |          100 |               50 |           38.21 |                    0 |
| Maternal Health Risk                      |           10 |              100 |           63.88 |                    0 |
| Maternal Health Risk                      |           50 |              100 |           65.67 |                    0 |
| Maternal Health Risk                      |          100 |              100 |           67.16 |                    0 |
| Maternal Health Risk                      |           10 |              200 |           62.09 |                    0 |
| Maternal Health Risk                      |           50 |              200 |           69.85 |                    0 |
| Maternal Health Risk                      |          100 |              200 |           69.55 |                    0 |
| Optical Recognition of Handwritten Digits |           10 |               50 |           97.79 |                    0 |
| Optical Recognition of Handwritten Digits |           50 |               50 |           97.68 |                    0 |
| Optical Recognition of Handwritten Digits |          100 |               50 |           10.3  |                    0 |
| Optical Recognition of Handwritten Digits |           10 |              100 |           97.52 |                    0 |
| Optical Recognition of Handwritten Digits |           50 |              100 |           97.84 |                    0 |
| Optical Recognition of Handwritten Digits |          100 |              100 |           97.95 |                    0 |
| Optical Recognition of Handwritten Digits |           10 |              200 |           97.47 |                    0 |
| Optical Recognition of Handwritten Digits |           50 |              200 |           97.9  |                    0 |
| Optical Recognition of Handwritten Digits |          100 |              200 |           97.84 |                    0 |
| Statlog (Vehicle Silhouettes)             |           10 |               50 |           20    |                    0 |
| Statlog (Vehicle Silhouettes)             |           50 |               50 |           20    |                    0 |
| Statlog (Vehicle Silhouettes)             |          100 |               50 |           20    |                    0 |
| Statlog (Vehicle Silhouettes)             |           10 |              100 |           20    |                    0 |
| Statlog (Vehicle Silhouettes)             |           50 |              100 |           20    |                    0 |
| Statlog (Vehicle Silhouettes)             |          100 |              100 |           20    |                    0 |
| Statlog (Vehicle Silhouettes)             |           10 |              200 |           20    |                    0 |
| Statlog (Vehicle Silhouettes)             |           50 |              200 |           20    |                    0 |
| Statlog (Vehicle Silhouettes)             |          100 |              200 |           20    |                    0 |
| Wine Quality                              |           10 |               50 |           40.09 |                    0 |
| Wine Quality                              |           50 |               50 |           41.72 |                    0 |
| Wine Quality                              |          100 |               50 |           45.55 |                    0 |
| Wine Quality                              |           10 |              100 |           42.8  |                    0 |
| Wine Quality                              |           50 |              100 |           40    |                    0 |
| Wine Quality                              |          100 |              100 |           44.52 |                    0 |
| Wine Quality                              |           10 |              200 |           44.2  |                    0 |
| Wine Quality                              |           50 |              200 |           39.72 |                    0 |
| Wine Quality                              |          100 |              200 |           43.12 |                    0 |

