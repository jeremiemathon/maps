#!/usr/bin/python
import json
def read_data_file(myfile):
	with open(myfile) as data_file:
		return json.load(data_file)

