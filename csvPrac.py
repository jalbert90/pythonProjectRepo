#!/usr/bin/python3

import csv

with open('2020-10-05-AccountStatement.csv', 'r') as fileHandle:
    csv_reader = csv.reader(fileHandle)

    for line in csv_reader:
        print(line)
