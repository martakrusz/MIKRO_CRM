import sys
import csv


def parse(fn):
    with open(fn, 'r', encoding='cp852') as data_base:
        csv_reader = csv.reader(data_base)

    for line in csv_reader:
        print(line)

#if __name__ == "__main__":
#   parse(data_base)
