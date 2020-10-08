#!/usr/bin/env python3

import os
import requests

path = "supplier-data/images/"
webpage_url = "linux-instance-IP-Address/media/images/"


for filename in os.listdir(path):
    if filename.endswith('.jpeg'):
        response = requests.post(webpage_url, file={'file': filename})
