#! /usr/bin/env python3

import os
import requests

description_path = "supplier-data/descriptions/"
image_path = "supplier-data/images/"
webpage_url = "http://localhost/fruits/"
dict_keys = ['name', 'weight', 'description', 'image_name']


# Iterating over all files in the descriptions directory
for filename in os.listdir(description_path):
    with open(description_path + filename, 'r') as file:
        with open(description_path + filename, 'r') as f:
            fruit_name = os.path.splitext(filename)[0]
            data = f.read()
            data = data.split('\n')
            fruits_dict = {"name": data[0], "weight": int(data[1].split()[0]), "description": data[2],
                           "image_name": fruit_name + ".jpeg"}

            response = requests.post(webpage_url, json=fruits_dict)

    print(fruits_dict)
    file.close()
    # Posting the dictionary in the webpage using json format
    # response = requests.post(webpage_url, json=fruits_dict)
