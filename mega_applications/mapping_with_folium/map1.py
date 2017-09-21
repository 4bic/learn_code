import folium

map = folium.Map(location=[ 36.728103, -1.285834], zoom_start=6, tiles="Mapbox Bright")

map.save("Nairobi.html")
