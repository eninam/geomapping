import folium
import pandas

# reads the volanoes files
data = pandas.read_csv("Volcanoes.txt")
#put the lats and long , and elevations (collumns in file) into a list
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

#init
map = folium.Map(location=[38.58, -99.09], zoom_start=6,
tiles= "Stamen Terrain")
# changes the color of the icon based on the elevation
def color_producer(elev):
    if(elev < 1000):
        return "green"
    elif 1000 <= elev  < 3000:
        return "orange"
    else:
        return "red"

# an pbject to be added to map
fg = folium.FeatureGroup(name="My Map")

# loop over the lat, long and elevation an puts a marker on every
#location
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt,ln]
     , popup= str(el)+ " meters" ,

     icon=folium.Icon(color=color_producer(el), icon='cloud'
     )))
#added a layer that has lines around continents and coutries
fg.add_child(folium.GeoJson(
data=open('world.json','r', encoding='utf-8-sig').read(),
 style_function=lambda x: {'fillColor': 'yellow' if
 x['properties']['POP2005'] < 10000000 else 'orange'
 if 10000000 <= x['properties']['POP2005'] <20000000 else 'red'}))

map.add_child(fg)
map.save("Map1.html")
