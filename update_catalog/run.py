#! /usr/bin/env python3

import os
import requests

description_path = "supplier-data/descriptions/"
image_path = "supplier-data/images/"
url = "http://localhost/fruits/"
dict_keys = ['name', 'weight', 'description', 'image_name']
images_list = []


# Creating a list to store the images names
images_list = [image_name for image_name in os.listdir(image_path) if image_name.endswith('jpeg')]
img_itr = 0

# Iterating over all files in the descriptions directory
for filename in os.listdir(description_path):
    with open(description_path + filename, 'r') as file:
        fruits_dict = {}
        key_itr = 0
        for line in file.readlines():
            if 'lbs' in line:
                fruits_dict[dict_keys[key_itr]] = int(line.strip().split()[0])
                key_itr += 1
            else:
                fruits_dict[dict_keys[key_itr]] = line.strip()
                key_itr += 1

    # Attaching the corresponding image name iterating through image_names list
    fruits_dict['image_name'] = images_list[img_itr]
    img_itr += 1

    print(fruits_dict)
    file.close()
    # Posting the dictionary in the webpage using json format
    # response = requests.post(webpage_url, json=fruits_dict)



