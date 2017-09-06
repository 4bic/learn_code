import sys
from pandas import *
import pandas as pd
import numpy as np
import csv
if __name__ == '__main__':
    '''create pandas dataframe '''

    # read csv
    data_df =  pandas.read_csv('data/PitchingPost.csv')
    # extract only the columns that we need
    year = data_df['yearID']
    hr = data_df['HR']
    hr_year = data_df[['yearID', 'HR']]
    # write to csv
    hr_year.to_csv('data/hr_year.csv')
