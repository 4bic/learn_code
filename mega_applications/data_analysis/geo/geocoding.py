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
    df = pd.read_csv('supermarkets.csv')
    # combine columns with addresses within the dataframe i.e city, state, Country and address
    df["Address"] = df["Address"]+", "+df["City"]+", "+df["State"]+", "+df["Country"]
    # geocode the "Address" column
    df["Coordinates"] = df["Address"].apply(nom.geocode)
    # fetch latitude and longitude value from the dataframe and add as columns
    #Latitude
    df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
    #Longitude
    df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)

    # write to csv
    df.to_csv('geocoded.csv')
    
if __name__ == '__main__':
    geocoder()
