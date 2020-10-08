#!/usr/bin/env python3


import os
from PIL import Image

path = "supplier-data/images/"
size = (600, 400)

for filename in os.listdir(path):
    if filename.endswith('.tiff'):
        raw_filename, ext = os.path.splitext(filename)  # Getting the filename without the extension
        Image.open(path + filename).convert('RGB').resize(size).save(path + raw_filename + '.jpeg', 'JPEG')

