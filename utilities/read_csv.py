import csv
import os


def read_data(filename):
    test_data_directory = "../test_data/"
    relative_directory = test_data_directory + filename
    current_directory = os.path.dirname(__file__)
    destination_directory = os.path.join(current_directory, relative_directory)
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    destination_file = os.path.join(current_directory, relative_directory)

    rows = []
    data_file = open(destination_file, 'r')
    reader = csv.reader(data_file)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows
