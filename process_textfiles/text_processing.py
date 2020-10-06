import os
import requests


def process_text(base_dir):
    feedback_dict = {}
    n = 0
    keys = ['title', 'name', 'date', 'feedback']
    for filename in os.listdir(base_dir):
        n += 1
        feedback_dict['id' + str(n)] = {}
        with open(os.path.join(base_dir, filename), 'r') as file:
            i = 0
            for line in file.readlines():
                feedback_dict['id' + str(n)][keys[i]] = line.strip()
                i += 1
        file.close()


    # print(feedback_dict)

    return None


process_text(r"data/feedback")
