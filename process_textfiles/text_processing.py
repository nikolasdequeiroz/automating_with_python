import os
import requests

def process_text(base_dir):
    feedback_dict = {}
    keys = ['title', 'name', 'date', 'feedback']
    for filename in os.listdir(base_dir):
        with open(os.path.join(base_dir, filename), 'r') as file:
            for line in file.readlines():
                print(line.strip())




        file.close()




    return None


process_text(r"data/feedback")
