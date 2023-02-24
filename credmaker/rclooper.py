#!/usr/bin/env python3
"""RZFeeser@alta3.com | Alta3 Research
   Using the CSV library to work with CSV data."""

import csv

with open("csv_users.txt", "r") as csvfile:
    i = 0
    #this loop will call the csv import to read the csvfile and python will handle separation at the comma delimiter
    for row in csv.reader(csvfile):
        i = i + 1
        filename = f"admin.rc{i}" # this f string says "fill in the value of i"

        with open(filename, "w") as rcfile:
            print("export OS_AUTH_URL=" + row[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
            print("export OS_USERNAME=" + row[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
            print("export OS_PASSWORD=" + row[5], file=rcfile)

#once looping is over
print("admin.rc files created!")

