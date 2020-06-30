import csv

with open('base_micro.csv', 'r', encoding='cp852') as data_base:
    csv_reader = csv.reader(data_base)

    for line in csv_reader:
        print(line)

