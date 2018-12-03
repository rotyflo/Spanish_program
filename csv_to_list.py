import csv

def csv_to_list(csv_file):
    with open(csv_file, 'rt') as file:
        reader = csv.reader(file)
        return list(reader)