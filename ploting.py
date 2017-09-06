import pandas as pd
import ggplot
from pandas import *
from ggplot import *

def lineplot():
    # collect the csv data
    hr_year = pd.read_csv('data/hr_year.csv')
    # plot the data with number of homeruns per year
    print ggplot(hr_year, aes('yearID', 'HR')) + geom_point(color='red')+ geom_line(color='red')+ ggtitle('Total HRs by Year') + xlab('Year')+ ylab('Home_Runs')

if __name__ == '__main__':
    lineplot()
