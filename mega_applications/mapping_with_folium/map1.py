import folium
import pandas

# variables
volcano_data = pandas.read_csv("Volcanoes.txt")
latitude = list(volcano_data["LAT"])
longitude = list(volcano_data["LON"])
elevation = list(volcano_data["ELEV"])
marker_name = volcano_data["LOCATION"]

# create base map
map = folium.Map(location=[ 38.58, -99.09], zoom_start=12, tiles="Mapbox Bright")
# utilize a feature group object to add multiple features
fg = folium.FeatureGroup(name="My Map")

# iterate over the data file and use location data
for lt, ln, el,nm in zip(latitude,longitude, elevation, marker_name):
    # add a each marker
    fg.add_child(folium.Marker(location=[lt,ln], popup=str(nm)+ "-"+str(el), icon=folium.Icon(color='green')))

map.add_child(fg)
# save genarated map
map.save("US_VOLCANOES.html")
