from wisard import Wisard
import os
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from datasets import datasets

log_file = os.path.join(os.path.dirname(__file__), "wisard.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)

logging.info("Starting the script")

num_slices_range = [10, 50, 100] 
num_dimensions_range = [50, 100, 200]


# Function to run Wisard
def run_wisard(num_slices, num_dimensions, datasets):
    logging.info(
        f"Running Wisard with num_slices={num_slices}, num_dimensions={num_dimensions}"
    )

    wisard = Wisard(
        num_slices=num_slices,
        num_dimensions=num_dimensions,
        ignore_zero=False,
        verbose=False,
        datasets=datasets,
        epochs=10,
    )

    wisard.run()


MAX_THREADS = 2 

with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
    futures = []
    for num_slices in num_slices_range:
        for num_dimensions in num_dimensions_range:
            future = executor.submit(run_wisard, num_slices, num_dimensions, datasets)
            futures.append(future)

    for future in as_completed(futures):
        try:
            future.result() 
        except Exception as e:
            logging.error(f"Thread encountered an error: {e}", exc_info=True)

logging.info("Finishing the script")
