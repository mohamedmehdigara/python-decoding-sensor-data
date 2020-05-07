import os
import glob
import csv

# Set file(s) path
sensor_files = glob.glob(os.path.join(os.getcwd(), 'datasets', '*.csv'))
sensor_files.sort()

# create a list to store data
sensor_data = []

# Loop over list of files
for sensor_file in sensor_files:
    with open (sensor_file) as data_file:
        # Create a csv.DictReader
        data_reader = csv.DictReader(data_file, delimiter=',')
        # Loop over each row dictionary
        for row in data_reader: 
            # Create a list of dictionaries
            sensor_data.append(row)

print(f"Loaded records {len(sensor_data)}")