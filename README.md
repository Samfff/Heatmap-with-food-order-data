# Heatmap-with-food-order-data
A heat map created with the help of Google Maps API and food order data, provided by Wolt 

If you want to see how it works yourself:

1) clone/download zip, 
2) remove everything from .html file
3) in terminal: python gm_heatmap.py

Wolt has provided the orders.json data, and it was created as a challengeset for developers to: 
"Make something cool"

What the .py-files do:

main.py:
- gathers the relevant data from json_parse and functions from gm_write_heatmap and runs them

json_parse.py: 
- Used to open the json file and parse the relevant data to be fed into the heatmap writer

gm_write_heatmap.py:
- Provides the functions for creating the heatmap points, circles, and ultimately writing on the .html file
