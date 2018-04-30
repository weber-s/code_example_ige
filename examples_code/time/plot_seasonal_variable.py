# -*- coding: utf-8 -*-
r"""
Add season DataFrame and categorical plot
=========================================

Add season (DJF, MAM, JJA, SON) to an existing dataframe then use seaborn to
plot distribution of value grouping by season.
"""

################################################################################
#This example cover the following basic:
#    
#    - group a dataframe by season
#    - plot seasonal distribution of a variable
#

import pandas as pd

# Load some atmospheric PM concentration at Grenoble Les Frenes from 2007 to 2018
csv_file = 'https://gist.githubusercontent.com/weber-s/4451562bb408fbfafc7b80520faa0773/raw/1989bcbc19894aad99feeb0f12dd1b36b8380960/PM_GRE-fr'
df = pd.read_csv(csv_file)

# Let's have a look at what is inside
print(df.head())

###############################################################################
# We want "date" as a date. So we convert it to datetime object

df["date"] = pd.to_datetime(df["date"])

# Set the date as index
df.set_index('date', inplace=True, drop=True)

###############################################################################
# Now, we wan't to group it by season: DJF, MAM, JJA, SON. Even if a date object
# has a lot of attribut (.day, .month, .year, etc), it does have a .season.
# Mostly because what we call "season" change from people to people and place to
# place. We then have to construct it ourself.
#
# This function is copy-pastable, so some extra work are done (check for index,
# type of date, etc).

def add_season(df):
    """
    Add a season column to the DataFrame df.

    parameters
    ----------
    
    df: Pandas DataFrame.
        The DataFrame to work with.

    return
    ------

    dfnew: a new pandas DataFrame with a 'season' columns.
    
    """
    
    month_to_season = {1:'DJF', 2:'DJF', 3:'MAM', 4:'MAM', 5:'MAM', 6:'JJA',
                       7:'JJA', 8:'JJA', 9:'SON', 10:'SON', 11:'SON', 12:'DJF'}
    
    dfnew = df.copy()

    # ensure we have date in index
    if isinstance(dfnew.index, pd.DatetimeIndex):
        dfnew["date"] = dfnew.index        
    elif 'date' in dfnew.columns:
        dfnew["date"] = pd.to_datetime(dfnew["date"])
    else:
        print("No date given")
        return
    
    # add a new column with the number of the month (Jan=1, etc)
    dfnew["month"] = dfnew.date.apply(lambda x: x.month)
    # sort it. This is not mandatory.
    dfnew.sort_values(by="month", inplace=True)

    # add the season base on the month number
    dfnew["season"] = dfnew["month"].replace(month_to_season)

    # and return the new dataframe
    return dfnew

###############################################################################
# Now we can use this function to add a 'season' and 'month' column to our
# dataframe.

df = add_season(df)

print(df.head())

###############################################################################
# Note that now, our dataframe has 2 new columns: 'month' and 'season'.
# We then use the `seaborn` library to plot categorical data, for instance the
# boxplot per season of PM.

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=df, x='season', y='PMrecons')

plt.show()

