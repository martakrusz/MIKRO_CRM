import csv
from datetime import datetime
import pandas as pd


def main():
    with open('base_micro.csv', 'r', encoding='cp852') as data_base:
        csv_reader = csv.DictReader(data_base, delimiter=';')

        with open('new_base_micro.csv', 'w', encoding='utf8') as new_data:
            fieldnames = ['ID', 'MEETING_DATE', 'FIRST_NAME', 'LAST_NAME', 'CITY', 'STREET', 'HOME_NUMBER', 'POST_CODE', 'POST_CITY', 'PHONE', 'COMMUNITY', 'COUNTY', 'OFFER', 'WYPOSAŻENIE', 'CENA', 'SPOSÓB ZAKUPU', 'STATUS ', 'RAITING','MEETING_DESCRIPTION', 'NEXT_MEETING' ]
            csv_writer= csv.DictWriter(new_data, fieldnames=fieldnames, delimiter='\t')
            csv_writer.writeheader()

            for row in csv_reader:
                if not any(row.values()):
                    continue
                csv_writer.writerow(row)



if __name__ == "__main__":
    main()
