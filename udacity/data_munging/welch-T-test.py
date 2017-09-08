import numpy as np
import pandas as pd
import scipy.stats

# perfome t-test on two sets of data (left handed / righ handed hitters)
def compare_averages():
    # read data into pandas
    baseball_data = pd.read_csv('data/baseball.csv')
    # split data into 2 dataframes
    lefthand_data = baseball_data[baseball_data['bats'] == 'L']
    righthand_data = baseball_data[baseball_data['bats'] == 'R']

    # perform welch T test
    result = scipy.stats.ttest_ind(lefthand_data['weight'], righthand_data['weight'], equal_var=False)

    # produce desired results
    if result[1] <= 0.5:
        return (False, result)
    else:
        return (True, result)

if __name__ == '__main__':
    result = compare_averages()
    print result
