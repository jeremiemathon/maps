#!/usr/bin/python3

import googlemaps
from pprint import pprint
from load_file import read_data_file
from datetime import datetime


def get_direction(gmaps, origin, destination):
	directions = gmaps.directions(origin, destination, language='fr', units='metric', alternatives='true')
	return directions

def print_direction(directions):
	for direction in directions:
		for leg in direction['legs']:
			print(str(leg['duration']['text']))
	
data_file = read_data_file("directions.json")
gmaps = googlemaps.Client(key='AIzaSyCCuEmWD6wBnBXlb5TVBguBB7DZQZAqGCo')

for data in data_file['directions']:
	origin = data['origin'] 
	destination = data['destination']
	name = data['name']
	print(str(name))
	print_direction(get_direction(gmaps,origin,destination))

