import sys
from pandas import *
import pandas as pd
import numpy as np
import csv

if __name__ == '__main__':
    '''create pandas dataframe
    column names;'country_name', 'gold', 'silver' and 'bronze'
    '''
    # open csv file
with open('sochi_medals.csv', 'rb') as medals:
    # reader = csv.reader(medals)

    #create dataframe
    df = pd.read_csv(medals)
    # refence columns
    country_name = df['Country']
    gold = df['Gold']
    silver = df['Silver']
    bronze = df['Bronze']

    # example sets Countries with 3 or less silvers
    print "Countries with 3 or less silvers"
    print df[df['Silver'] <= 3]

    # Sample countries with no Gold
    print " "
    print "countries with no Gold"
    print df[df['Gold'] <1]
