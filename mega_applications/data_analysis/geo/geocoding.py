import os
import pandas as pd
import geopy
from geopy.geocoders import Nominatim

nom = Nominatim()
# test how geocode works
# n = nom.geocode("3995 23rd St,San Francisco,CA 94114")
# print n

def geocoder():
    # open file
    df_4 = pd.read_csv('supermarkets.csv')
    # combine columns with addresses within the dataframe i.e city, state, Country and address
    df_4["Address"] = df_4["Address"]+", "+df_4["City"]+", "+df_4["State"]+", "+df_4["Country"]
    # geocode the "Address" column
    df_4["Coordinates"] = df_4["Address"].apply(nom.geocode)

    return df_4
