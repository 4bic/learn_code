from pandas import *
import numpy as np

if __name__ == '__main__':
    # read csv
    mca = pandas.read_csv('mca_data.csv')
    # fill missing gender fields with 'Male'
    mca['gender'] = mca['gender'].fillna('Male')
    # export to a new csv file named 'filled_Garissa.csv'
    mca.to_csv('filled_Garissa.csv')
