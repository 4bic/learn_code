import pandas as pd
import ggplot
from pandas import *
from ggplot import *

def lineplot():
    # collect the csv data
    hr_year = pd.read_csv('data/hr_year.csv')
    # plot the data with number of homeruns per year
    print ggplot(hr_year, aes('yearID', 'HR')) + geom_point(color='red')+ geom_line(color='red')+ ggtitle('Total HRs by Year') + xlab('Year')+ ylab('Home_Runs')


# the generated plot is at ('plots / hr_year.png')

def lineplot_compare():
    hr_by_team = pd.read_csv('data/hr_by_team_year_sln_lan.csv')
    # plot the data with number of homeruns per year
    print ggplot(hr_by_team, aes('yearID', 'HR', color='teamID')) + geom_point()+ geom_line()+ ggtitle('Total SLN & LAN HRs by Year') + xlab('Year')+ ylab('Home_Runs')

if __name__ == '__main__':
    #lineplot()
    lineplot_compare() # the generated plot is at ('plots / hr_by_team.png')
