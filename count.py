import csv
from collections import defaultdict

# Define the CSV file
file_name = 'metrics.csv'

# Initialize a dictionary to store the counts
model_dataset_encoding_counts = defaultdict(lambda: defaultdict(int))

# Read the CSV file and process the data
with open(file_name, mode='r') as file:
    reader = csv.reader(file)
    
    # Skip the header
    next(reader)
    
    for row in reader:
        model = row[0]
        dataset = row[3]
        encoding = row[4]
        
        # Skip rows with empty dataset or encoding
        if dataset and encoding:
            model_dataset_encoding_counts[model][f"{dataset} with {encoding} encoding"] += 1

# Print the results
print("Occurrences per model and dataset:")
print("-----------------------------------")
for model, dataset_encoding_counts in model_dataset_encoding_counts.items():
    print(f"Model: {model}")
    for dataset_encoding, count in dataset_encoding_counts.items():
        print(f"  Dataset: {dataset_encoding} -> {count} occurrences")
    print()

