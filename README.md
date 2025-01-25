# Weightless Neural Networks Binarization

This repository contains implementations of different binarization/encoding methods for weightless neural networks (WNN), specifically DWN and WiSARD.

## Purpose

The purpose of this project is to explore and compare various binarization techniques applied to weightless neural networks. This includes evaluating their performance and efficiency.

## Installation

To install the necessary dependencies, please run the following command:

```bash
pip install -r requirements.txt
```

## Running the Program

To run the program, use the following command in the folder of the WNN model you wish to test:

```bash
python main.py
```

This will execute the binarization methods on the weightless neural networks and output the results.

## Running Metrics

To evaluate the metrics after running the program, use the following command:

```bash
python analyse_expriments.py
```

This will process the logs and generate a detailed report of the performance metrics, which will be saved in the `ouput` directory in the root directory.

## Logs and Metrics

Logs and metrics generated during the execution of the program are stored in specific directories. For example, the log for WiSARD is in `wisard/wisard.log` and for DWN is in `DWN/dwn.log`. The metrics are stored in the `metrics.csv` file in the root directory. You can find detailed information about the performance and behavior of the binarization methods in these files.

## Contributing

We welcome contributions to this project. If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request. Make sure to follow the contribution guidelines outlined in `CONTRIBUTING.md`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.