import csv

filename = 'metrics.csv'
output_file = 'new_metrics.csv'

with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    epoch = 0
    for row in reader:
        if row[0] == 'epoch':
            continue
        