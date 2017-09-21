import folium
import pandas

# variables
volcano_data = pandas.read_csv("Volcanoes.txt")
latitude = list(volcano_data["LAT"])
longitude = list(volcano_data["LON"])
elevation = list(volcano_data["ELEV"])
marker_name = volcano_data["LOCATION"]

def elevate_color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 < elevation < 3000:
        return 'orange'
    else:
        return 'red'

# create base map
map = folium.Map(location=[ 38.58, -99.09], zoom_start=3, tiles="Mapbox Bright")
# utilize a feature group object to add multiple features
fg = folium.FeatureGroup(name="US Volcanoes")

# iterate over the data file and use location data
for lt, ln, el,nm in zip(latitude,longitude, elevation, marker_name):
    # add a each marker
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
    fill_color=elevate_color(el), color = 'grey', fill_opacity=0.7))


fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding="utf-8-sig"),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)

# save genarated map
map.save("volcanoes.html")
