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
    medals_df = pd.read_csv(medals)
    # refence columns
    country_name = medals_df['Country']
    gold = medals_df['Gold']
    silver = medals_df['Silver']
    bronze = medals_df['Bronze']

    print "Average  bronze count for countries with at least one gold"
    bronze_one_gold = bronze[medals_df['Gold'] >=1]
    avg_bronze_one_gold = np.mean(bronze_one_gold)
    print (avg_bronze_one_gold)

    print "Average medal count for countries with atleast one medal"
    avg_medal_count = medals_df[['Gold','Silver', 'Bronze']].apply(np.mean)

    print avg_medal_count

    print "Countries with 3 or less silvers"
    print medals_df[df['Silver'] <= 3]

    print "countries with atleats one Gold"
    print medals_df[df['Gold'] >=1]

    print "Point for countries if Gold = 4, Silver = 3 , Bronze = 1"
    medal_count = medals_df[["Gold", "Silver", "Bronze"]]
    points = np.dot(medal_count, [4,2,1])

    olympic_points = {'Country': Series(medals_df['Country']),'points': Series(points)}
    olympic_df = DataFrame(olympic_points)

    print olympic_df
