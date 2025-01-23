from wisard import Wisard
import os
import logging

log_file = os.path.join(os.path.dirname(__file__), "wisard.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)

logging.info("Starting the script")

datasets_ids = [
    # 222,  # Bank Marketing ! error calculating min and max
    # 39,  # Ecoli
    53,  # Iris
    # 186,  # Wine Quality
    # 264,  # EEG Eye State
    # 159,  # MAGIC Gamma Telescope
    # # 2,  # Adult ! error calculating min and max
    # 149,  # Statlog (Vehicle Silhouettes)
    # 863,  # Maternal Health Risk
    # 42,  # Glass Identification
    # "mnist",  # MNIST
]

wisard = Wisard(
    num_slices=10,
    num_dimensions=20,
    address_size=10,
    ignore_zero=False,
    verbose=False,
    num_bits_thermometer=10,
    datasets_ids=datasets_ids,
)

wisard.run()

num_slices_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
num_dimensions_range = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]


for num_slices in num_slices_range:
    logging.info(f"Running Wisard with num_slices={num_slices}")
    for num_dimensions in num_dimensions_range:
        logging.info(f"Running Wisard with num_dimensions={num_dimensions}")
        wisard = Wisard(
            num_slices=num_slices,
            num_dimensions=num_dimensions,
            address_size=10,
            ignore_zero=False,
            verbose=False,
            num_bits_thermometer=10,
            datasets_ids=datasets_ids,
        )
        wisard.run()

