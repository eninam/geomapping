import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
map = folium.Map(location=[38.58, -99.09], zoom_start=6,
tiles= "Stamen Terrain")
# how to add other layers and add objects
def color_producer(elev):
    if(elev < 1000):
        return "green"
    elif 1000 <= elev  < 3000:
        return "orange"
    else:
        return "red"


fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt,ln]
     , popup= str(el)+ " meters" ,

     icon=folium.Icon(color=color_producer(el), icon='cloud'
     )))


map.add_child(fg)
map.save("Map1.html")
