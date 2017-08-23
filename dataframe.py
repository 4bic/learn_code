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

    print "Average  bronze count for countries with at least one gold"
    bronze_one_gold = bronze[df['Gold'] >=1]
    avg_bronze_one_gold = np.mean(bronze_one_gold)
    print (avg_bronze_one_gold)

    print "Average medal count for countries with atleast one medal"
    avg_medal_count = df[['Gold','Silver', 'Bronze']].apply(np.mean)

    print avg_medal_count

    print "Countries with 3 or less silvers"
    print df[df['Silver'] <= 3]

    print "countries with atleats one Gold"
    print df[df['Gold'] >=1]
