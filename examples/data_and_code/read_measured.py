#!/usr/bin/env python3

"""
read tide_measurements.py

read the csv file from the measured data
"""

import csv


def read_tide_measurements(filename):
    times = []
    heights = []
    with open(filename) as infile:
        # skip the first row
        infile.readline()
        for i, row in enumerate(csv.reader(infile, delimiter=";")):
            if i > 5: break
            # date is first cell, and time is the second
            dt_str = " ".join(row[0:2])
            # hieght is the fifth (4 in zero-index space)
            try:
                h = float(row[4])
            except ValueError:
                print(i, row[4])
                # if there is not valid data -- skip this row
                continue
            times.append(datetime.strptime(dt_str, "%d-%m-%Y %H:%M:%S"))
            heights.append(h)
    return times, heights
