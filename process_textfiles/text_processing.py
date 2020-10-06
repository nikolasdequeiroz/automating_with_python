import os
import requests


def process_text(base_dir, webpage_url):
    feedback_dict = {}
    n = 0  # Initializing the variable to iterate over the IDs
    keys = ['title', 'name', 'date', 'feedback']
    for filename in os.listdir(base_dir):
        n += 1
        feedback_dict = {}
        with open(os.path.join(base_dir, filename), 'r') as file:
            i = 0  # Initializing the variable to iterate over the keys
            for line in file.readlines():
                feedback_dict[keys[i]] = line.strip()
                i += 1
        file.close()
        response = requests.post(webpage_url, json=feedback_dict)

        if response.status_code == 201:
            print("Information correctly sent. Status code {}".format(response.status_code))
        else:
            print("Error {}. Information not sent".format(response.status_code))


process_text("/data/feedback/", 'http://serve_ip/feedback/')


# Example of a function call
process_text(r"data/feedback", webpage_url=r'http://104.154.70.226/feedback')
