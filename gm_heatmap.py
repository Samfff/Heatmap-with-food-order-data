import gm_write_heatmap
from json_parse import lats_lngs

# Parameters are latitutes and longitudes returned from the function made in json_parse.py

# takes in a latitude and longitude and the zoom of the map
# The map is designed to center at the middle of Helsinki, while zooming to an optimal height

google_map = gm_write_heatmap.GoogleMaps_HeatMap(60.165076, 24.929868, 15)
google_map.heatmap(lats_lngs[0], lats_lngs[1])
google_map.draw("mymap.html")
