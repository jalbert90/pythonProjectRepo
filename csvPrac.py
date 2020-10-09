#!/usr/bin/python3

import csv

with open('/home/jacob/positions.csv', 'r') as fileHandle:
    csv_reader = csv.reader(fileHandle)

    next(csv_reader)
    next(csv_reader) 
    next(csv_reader)

    with open('positionTransposition.csv', 'w') as fileHandle2:
        csv_writer = csv.writer(fileHandle2)

        for row in csv_reader:
            csv_writer.writerow(row)
