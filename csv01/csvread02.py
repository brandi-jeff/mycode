#!/usr/bin/python3
"""using csv from stndard library to acces csv files"""

import csv

def main():
    with open('superbirthday.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print('Column names are {}'.format(", ".join(row)))
                line_count += 1
            
            print('\t{} aka {} was born in {}.'.format(row["name"],row["heroname"],row["birthday month"]))
            line_count += 1

    print('Processed {} lines.'.format(line_count))


if __name__ == "__main__":
    main()
