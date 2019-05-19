import Dependencies.matlib as matlib
import csv

with open('./Data/nacimientos.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["granja"]} had {row["partos"]} parts, and were born {row["nacidos_vivos"]} pigs.')
        line_count += 1
    print(f'Processed {line_count} lines.')