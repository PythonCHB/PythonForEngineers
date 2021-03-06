==================
Tide Data Analysis
==================

Some day that tides are "**The** geophysical success story". That is, tides are the only geophysical phenomenon that can be well predicted weeks, months, even years in advance. That is because the tides are driven by astronomical forcing (Mostly the gravitational pull of the sun and the moon) that is periodic and very regular and predictable.  The bathymetry and shoreline greatly influence the tidal flow, but the resulting flow is always made up of individual components that reflect this underlying forcing -- that is, have specific frequencies that match the astronomical phenomena.

Because of this, if the tide is measured at a given location for a fairly short duration, we can compute the magnitude and phase of each of these components, and then use those to predict the tides into the future with great accuracy.


Meteorological Tides
--------------------

However, despite this success, there are complications.  In the Wadden Sea, and many regions with shallow waters and strong winds, the winds can raise or lower the water level substantially. These are often referred to as "meteorological tides". These can result in a substantial difference in water level from the astronomical tide forecasts.

In this exercise, we will examine and plot both the predicted tides and measured water levels for a location on the Wadden Sea, so we can learn about the effects of winds on the tide in that region.

This will give you an example of:

* Reading and parsing (messy) text files to extract the data.
* Simple plotting of data
* Basic interpolation and data Analysis

The Data
--------

Here we have two data files:

Measured Data: :download:`NVT_WATHTE_HARL.csv <data_and_code/NVT_WATHTE_HARL.csv>`

Tidal Predictions as an Excel Spreadsheet: :download:`GezeitenkalenderHarlingen.xlsx <data_and_code/GezeitenkalenderHarlingen.xlsx>`
Tidal Predictions as a CSV file: :download:`GezeitenkalenderHarlingen.csv <data_and_code/GezeitenkalenderHarlingen.csv>`

(This data from: http://gezeiten-kalender.de)

The Excel file makes it easier to see the data, but it is easier to read the data from a csv file.

Download these files to your machine, and we can work on reading them.


Parsing the Gezeiten-Kalender Data
----------------------------------

This data is designed to make a nice table for people to read, so is a bit
"messy" for a computer to read. But it is consistently structured, and python provided nice tools for text manipulation -- so we can parse out the CSV file.

Take a look at that now:

:download:`read_tide_data.py <data_and_code/read_tide_data.py>`

That file is a python "module" -- it can be run as a script by itself, or "imported" into other python code, and the functions defined in it will be available to use.

You can run it on the command line with::

  python3 read_tide_data.py

Or in `iPython` with::

  run read_tide_data.py

Reading the measured data
-------------------------

Reading the measured data is much easier -- it is a nicely formatted CSV file.

In fact, the `Pandas data analysis library <https://pandas.pydata.org/>`_
has a CSV File reader that can read it out of the box.

So we can immediately work with the data in a Jupyter Notebook.








