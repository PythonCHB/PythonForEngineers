#!/usr/bin/env python

"""
read_tide_data

This module contains a function that reads the csv version of data from the
German tide site:

 http://gezeiten-kalender.de:9099/calendar/month/1751.ics?y=2018&m=9&f=Webseite

The data are presented as a nice table on the website, but there does not seem to
be a way to download it as noce computer readable file.

So we will use Python to parse the file into a nicer format.
"""

# the built-in csv reader is very helpful
# https://docs.python.org/3/library/csv.html
import csv

from datetime import datetime


def parse_row(row):
    """
    parse a single row or data
    one for each day
    """
    # could use the datetime formatting:
    # datetime.datetime.strptime('20 September 2018', "%d %B %Y")
    # but it depends on the locale
    months = ['january',
              'february',
              'march',
              'april',
              'may',
              'june',
              'july',
              'august',
              'september',
              'october',
              'november']
    months = dict(zip(months, range(1, 13)))

    # some empty lists to accumulate the data in
    times = []
    heights = []
    # first cell is the month and year:
    # "September 2018"
    month, year = row[0].split()
    month = months[month.lower()]
    year = int(year)

    # next cell is the day and date:
    # 'Sun 30'
    day = int(row[1].split()[1])

    # the next five cells are time/height pairs:
    # 06:57 CEST / 0.26 m'
    # or sometimes no height
    # '21:12 CEST'
    for cell in row[2:7]:  # cells from 2 to 7
        # is there a height value?
        if len(cell.split('/')) != 2:
            # no height -- go to next one
            continue
        time, height = cell.split('/')
        # ignoring timezone for now
        time = time.split()[0]
        hour, minute = time.split(':')
        hour = int(hour)
        minute = int(minute)
        # assume meters!
        height = float(height.split()[0])

        # make a datetime object
        dt = datetime(year, month, day, hour, minute)

        # add them to the lists of data
        times.append(dt)
        heights.append(height)

    return times, heights


def read_data(filename):
    """
    read the data from the gezeiten-kalender.de site and return it as two lists:

    datetimes of the data
    predictied tidal heights
    """

    # first we need to open the file

    # using "with" ensures that the file will be properly closed
    # when we are done with it.
    times = []
    heights = []
    with open(filename) as infile:
        # skip the first row
        infile.readline()
        for row in csv.reader(infile, delimiter=","):
            # call the other function to parse out a full row
            t, h = parse_row(row)
            times.extend(t)
            heights.extend(h)

    return times, heights


# This code will run if this file is run as a "script":
#  python read_tide_data.py
#
# The code in this block will not run id the module is imported
#   for use in another script or notebook, or...
if __name__ == "__main__":

    # A test example
    infilename = "GezeitenkalenderHarlingen.csv"
    times, heights = read_data(infilename)

    # and make a simple plot
    import matplotlib.pyplot as plt

    # create a figure an axes object
    fig, ax = plt.subplots()

    # plot the data:
    ax.plot(times, heights, '-o')

    # show the plot:
    plt.show()


