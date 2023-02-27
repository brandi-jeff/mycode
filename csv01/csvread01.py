#!/usr/bin/env python3

'''Use standard library to access csv files'''

import csv

def main():

    with open('superbirthday.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            #if on the first line in the file (index 0)
            if line_count == 0:
                print('Column names are {}'.format(", ".join(row)))
                line_count += 1
            else:
                print('\t{} aka {}, was born in {}.'.format(row[0],row[1],row[2]))
                line_count += 1

        print('Processed {} lines.'.format(line_count))


if __name__ == "__main__":
    main()
