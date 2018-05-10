'''
Created on Feb 20, 2018

@author: SamSihvonen
'''

import json

with open('orders.json', 'r') as f:
    orders = json.load(f)

# Orders are made between 8.1.-14.1.2018.
# Following functions parse the json file to find order 
# latitudes and longitudes. They are gathered into a list,
# where lats and longs are within their own lists so they can imported
# into the heatmap functions.

def locations_to_list(dictionary):
    list = []
    # Adds locations from customer item
    for order in orders:
        list.append(order["customer"]["location"].values())
    return list

def parse_lat_lon(list):
    return zip(*list)

# Uses the function in json_parse.py to get two lists, 
# first one includes latitutes and second one longitudes.

lats_lngs = parse_lat_lon(locations_to_list(orders))
