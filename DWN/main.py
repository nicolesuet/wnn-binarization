from dwn import DWN
import os
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import psutil
from datasets import datasets

log_file = os.path.join(os.path.dirname(__file__), "dwn.log")
logging.basicConfig(
    level=logging.INFO,
    format="[DW] - %(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)

logging.info("Starting the script")

num_slices_range = [10, 50, 100]  # Reduced range
num_dimensions_range = [50]  # Reduced range

def log_resource_usage():
    process = psutil.Process(os.getpid())
    memory_usage = process.memory_info().rss / 1024**2  # Memory in MB
    cpu_usage = process.cpu_percent(interval=1.0)  # CPU usage in %
    logging.info(f"Memory usage: {memory_usage:.2f} MB, CPU usage: {cpu_usage:.2f}%")


def run_dwn(num_slices, num_dimensions, datasets, scatter_code):
    logging.info(
        f"Running DWN with num_slices={num_slices}, num_dimensions={num_dimensions}"
    )
    log_resource_usage()

    dwn_obj = DWN(
        num_slices=num_slices,
        num_dimensions=num_dimensions,
        num_bits_thermometer=10,
        datasets=datasets,
        epochs=100,
        times=10,
        batch_size=32,
        scatter_code=scatter_code,
    )

    dwn_obj.run()
    log_resource_usage()


run_dwn(
    0, 0, datasets, scatter_code=False
)  # Run with no slices and dimensions

for num_slices in num_slices_range:
    for num_dimensions in num_dimensions_range:
        run_dwn(
            num_slices, num_dimensions, datasets, scatter_code=True
        )
