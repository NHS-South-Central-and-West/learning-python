"""
When importing into your script:

from package_folder.ordered_monthly_line_chart import monthly_line_chart as mlc 

This has been written to be agnostic of which library has been used to create your
dataframe: Pandas or Polars. You will need to ensure that your date column has been 
converted to thedatetime datatype. Example using Pandas:

df = pd.read_csv('data.csv')
df['Month'] = pd.to_datetime(df['Month'], dayfirst= True)

"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import datetime
from typing import Optional
import pandas as pd
from pandas import DataFrame
import polars as pl
from polars import DataFrame

def monthly_line_chart(data: DataFrame, x: str, y: str, hue: Optional[str]= None, chart_title: Optional[str]= None):

    sns.set_style('darkgrid')               # Set the Seaborn style to shaded background with white gridlines
   
    if not isinstance(data, DataFrame):
        raise TypeError('The data parameter must be a Pandas or Polars DataFrame')

    if x not in data.columns:
        raise ValueError(f'Column {x} is not present in the DataFrame')
    
    if y not in data.columns:
        raise ValueError(f'Column {y} is not present in the DataFrame')
    
    if hue and hue not in data.columns:
        raise ValueError(f'Column {hue} is not present in the DataFrame')
    
    if not all(isinstance(value,datetime.datetime) or value is None for value in data[x]):   # Check whether all the x values are datetime
        raise TypeError(f'Your date column must only contain datetime values')

    plt.figure(figsize=(16,6))
    plt.grid(True, which= 'both')
    ax = sns.lineplot(data= data, x= x, y= y, hue= hue)

    # Firstly, label the primary x-axis. You need to do this for the major and minor ticks to ensure that all labels get formatted the same way.
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b')) # %b is the short month format e.g. 'Oct' for October
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))
    ax.tick_params(labelsize = 10, which='both') # Set the label font size and apply the formatting to the major and minor ticks.

    # Add a secondary x-axis displaying the years just below the months
    sec_xaxis = ax.secondary_xaxis(-0.1) # the argument relates to each label's vertical position.
    sec_xaxis.xaxis.set_major_locator(mdates.YearLocator())
    sec_xaxis.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    sec_xaxis.spines['bottom'].set_visible(False) # Remove the spines to reduce clutter
    sec_xaxis.tick_params(length = 0, labelsize = 10)

    # Rotate the short month labels in the primary x-axis.
    for label in ax.get_xticklabels(which='both'):
        label.set(rotation = 90, horizontalalignment='center')

    # If you wanted to also rotate the secondary x-axis labels, you would replace "ax" with "sec_xaxis", i.e. the variable name for the secondary axis labels.

    # Add the title and axis labels, and plot the chart.
    plt.xlabel(f'{x.name.replace("_"," ").title()}')
    plt.ylabel(f'{y.name.replace("_"," ").title()}')

    # If a chart title has not been provided, create one from the y-axis field, removing underscores
    # and converting it to title case.
    if chart_title == None:
        plt.title(f'{y.name.replace("_"," ").title()} by Month')
    else: plt.title(chart_title)
    
    plt.show()


