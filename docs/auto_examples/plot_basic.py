# -*- coding: utf-8 -*-
r"""
Load a CSV file from the web and plot it
========================================

This example cover the following basic:
    
    - retrieve a csv file from the web and store it in a pandas DataFrame
    - manipulate date
    - deal with missing value
    - basic plot

"""

import pandas as pd

# Let's load the Mauna Loa monthly average CO2 concentration
csv_file = 'https://raw.githubusercontent.com/alignedleft/d3-book/master/chapter_11/mauna_loa_co2_monthly_averages.csv'
df = pd.read_csv(csv_file)

###############################################################################
# Let's have a look at what is inside
print(df.head())

###############################################################################
# Ok, we have a `year`, `month` and `average` column. We want a date as index and
# also remove the -99.99 value (no measure).

# Set the date as index
df['date'] = df[['year', 'month']].apply(lambda s: pd.datetime(*s, 1), axis=1)
df.set_index('date', inplace=True, drop=True)

# replace -99.99 values by NaN
df['average'].replace({-99.99: pd.np.nan}, inplace=True)

# and then finally plot it
ax = df['average'].plot()
ax.set_title("Mauna Loa station $CO_2$ concentration")
ax.set_ylabel("$CO_2$ (ppm)")

