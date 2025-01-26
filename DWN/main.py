from dwn import DWN
import os
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import psutil

log_file = os.path.join(os.path.dirname(__file__), "dwn.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)

logging.info("Starting the script")

datasets_ids = [
    39,  # Ecoli
    53,  # Iris
    186,  # Wine Quality
    264,  # EEG Eye State
    159,  # MAGIC Gamma Telescope
    149,  # Statlog (Vehicle Silhouettes)
    863,  # Maternal Health Risk
    42,  # Glass Identification
    "mnist",  # MNIST
]

num_slices_range = [10, 50, 100]  # Reduced range
num_dimensions_range = [
    50, 
    100, 
    200
]  # Reduced range

def log_resource_usage():
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / 1024 ** 2  # Memory in MB
    cpu_usage = process.cpu_percent(interval=1.0)  # CPU usage in %
    logging.info(f"Memory usage: {memory_usage:.2f} MB, CPU usage: {cpu_usage:.2f}%")

def run_dwn(num_slices, num_dimensions, datasets_ids):
    logging.info(f"Running Wisard with num_slices={num_slices}, num_dimensions={num_dimensions}")
    log_resource_usage()

    dwn_obj = DWN(
        num_slices=num_slices,
        num_dimensions=num_dimensions,
        num_bits_thermometer=10,
        datasets_ids=datasets_ids,
        epochs=5,
        batch_size=32,
    )

    dwn_obj.run()
    log_resource_usage()

# Limit the number of concurrent threads
MAX_THREADS = 2

with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
    futures = []
    for num_slices in num_slices_range:
        for num_dimensions in num_dimensions_range:
            future = executor.submit(run_dwn, num_slices, num_dimensions, datasets_ids)
            futures.append(future)

    for future in as_completed(futures):
        try:
            future.result()  # Wait for each thread to complete
        except Exception as e:
            logging.error(f"Thread encountered an error: {e}")