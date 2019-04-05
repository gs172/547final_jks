"""
File name: final_client.py
Authors: Evan Jelly, Wesley Kendall, Ge Song
Assignment:  Image Processor Final Project
Due Date: 04/26/2019 23:59

Function: client
"""

import requests

local = "http://127.0.0.1:5000"
vcm = "http://vcm-9103.vm.duke.edu:5000"
host = local  # allows server location to be easily changed

''' Check to see if server is on '''
print("-------------------------(GET: /)---------------------------")
print("Checking if server is on by accessing '/' route")
r = requests.get(host + "/")
print("'r' type is {}".format(type(r)))
print("'r' = {}".format(r))
print("'r.text' type is {}".format(type(r.text)))
print("'r.text' = {}".format(r.text))
