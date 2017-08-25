import requests
import json

if __name__ == '__main__':
    # getinfo method from last.FM
    # url =  'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=e8db6da46920346cd25bc04df44b8f9f&artist=Rihanna&album=Unapologetic&format=json'
    url =  'http://ws.audioscrobbler.com/2.0/?method==geo.gettopartists&country=kenya&api_key=e8db6da46920346cd25bc04df44b8f9f&format=json
    # call api using request library and load results into a dictionary
    data = requests.get(url).text
    # interpret strings into JSON objects
    data = json.loads(data)
    # print out the name of the Top artist in country
    print data['topartist']['artist'][0]['name']
