from wisard import Wisard
import os
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

# Set up logging
log_file = os.path.join(os.path.dirname(__file__), "wisard.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)

logging.info("Starting the script")

# Define dataset IDs
datasets_ids = [
    # 39,  # Ecoli
    # 53,  # Iris
    # 186,  # Wine Quality
    # 264,  # EEG Eye State
    # 159,  # MAGIC Gamma Telescope
    # 149,  # Statlog (Vehicle Silhouettes)
    # 863,  # Maternal Health Risk
    # 42,  # Glass Identification
    "mnist",  # MNIST
    # 80,  # Letter Recognition
]

# Define ranges for num_slices and num_dimensions
num_slices_range = [10, 50, 100]  # Reduced range
num_dimensions_range = [50, 100, 200]  # Reduced range


# Function to run Wisard
def run_wisard(num_slices, num_dimensions, datasets_ids):
    logging.info(
        f"Running Wisard with num_slices={num_slices}, num_dimensions={num_dimensions}"
    )

    # Initialize Wisard
    wisard = Wisard(
        num_slices=num_slices,
        num_dimensions=num_dimensions,
        address_size=10,
        ignore_zero=False,
        verbose=False,
        num_bits_thermometer=10,
        datasets_ids=datasets_ids,
        epochs=1,
    )

    # Run Wisard
    wisard.run()


# Limit the number of concurrent threads
MAX_THREADS = 1  # Adjust this based on your system's capabilities

# Use ThreadPoolExecutor to manage threads
with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
    futures = []
    for num_slices in num_slices_range:
        for num_dimensions in num_dimensions_range:
            # Submit tasks to the executor
            future = executor.submit(
                run_wisard, num_slices, num_dimensions, datasets_ids
            )
            futures.append(future)

    # Wait for all tasks to complete
    for future in as_completed(futures):
        try:
            future.result()  # Wait for each thread to complete
        except Exception as e:
            logging.error(f"Thread encountered an error: {e}")
