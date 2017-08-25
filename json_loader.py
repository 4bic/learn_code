import requests
import json

if __name__ == '__main__':
    # getinfo method from last.FM
    url =  'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=e8db6da46920346cd25bc04df44b8f9f&artist=Rihanna&album=Unapologetic&format=json'
    # call api using request library and load results into a dictionary
    data = requests.get(url).text
    # interpret strings into JSON objects
    data = json.loads(data)
    print type(data)
    print data
