import folium
# create map
map = folium.Map(location=[ -1.285834, 36.728103], zoom_start=6, tiles="Mapbox Bright")
map.add_child(folium.Marker(location=[-1.29, 36.73], popup="Hi, this is my Home Marker", icon=folium.Icon(color='green')))
# save genarated map
map.save("Nairobi.html")
