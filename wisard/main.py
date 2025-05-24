from wisard import Wisard
import os
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from datasets import datasets

log_file = os.path.join(os.path.dirname(__file__), "wisard.log")
logging.basicConfig(
    level=logging.INFO,
    format="[WISARD] - %(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(log_file), logging.StreamHandler()],
)

logging.info("Starting the script")

num_slices_range = [10, 50, 100]
num_dimensions_range = [50]

# Function to run Wisard
def run_wisard(num_slices, num_dimensions, datasets, scatter_code):
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
        scatter_code=scatter_code,
    )

    wisard.run()

run_wisard(0, 0, datasets, scatter_code=False)

for num_slices in num_slices_range:
    for num_dimensions in num_dimensions_range:
        run_wisard(num_slices, num_dimensions, datasets, scatter_code=True)
            
            
