import numpy as np
import pandas as pd
from pandas import *
import scipy.stats

def normalize_features(features, mu, sigma):
    """
    Normalize features from the dataset
    """
    array_normalized = (array - array.mean())/array.std()
    mu = array.mean()
    sigma = array.std()


def compute_cost(features, values, theta):
    """
    Compute the cost function given a set of features / values of a theta
    """
    m = len(values)
    sum_of_square_errors = np.square(np.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2 * m)

    return cost

def gradient_descent(features, values, theta, aipha, num_iterations):
    '''
    Perform gradient_descent given a dataset with arbitrary number
    of features
    '''
    m = len(values)
    cost_history = []

    for i in range(num_iterations):
        predicted_values = np.dot(features, theta)
        theta = theta - alpha / m * np.dot((predicted_values - values), features)

        cost = compute_cost(features, values, theta)
        cost_history.append(cost)

        return theta, pd.Series(cost_history)

if __name__ == '__main__':
    # read data into pandas dataframe
    data = pd.read_csv('data/baseball.csv')

    # isolate values
    features = data[['height', 'weight']]
    values = data[['HR']]
    m = len(values)
    
    # Normalize features
    features, mu, sigma = normalize_features(features)
