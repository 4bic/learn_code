import sys
from pandas import *
import pandas as pd
import numpy as np
import csv
if __name__ == '__main__':
    '''create pandas dataframe '''

    # read csv
    mca_data =  pandas.read_csv('mca_data.csv')
    #create dataframe
    mca_df = pandas.DataFrame(mca_data)
    # combine surname and other name into Full Name
    mca_data['fullName'] = mca_data['Surname'] + ' ' + mca_data['Other_Names']
    # write to csv
    mca_data.to_csv('mca_data_with_fullName.csv')

    # print mca_df[mca_df['Ward_Code'] <= 50]
