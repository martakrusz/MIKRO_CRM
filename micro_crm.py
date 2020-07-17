import csv
from datetime import datetime


def main():
    with open('base_micro.csv', 'r', encoding='cp852') as data_base:
        csv_reader = csv.DictReader(data_base, delimiter=';')

        for row in csv_reader:
            if not any(row.values()):
                continue
            print(row)
print(main())
if __name__ == "__main__":
    main()