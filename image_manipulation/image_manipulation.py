from PIL import Image
import os


def image_manipulation(origin_folder, destination_folder, size=(128, 128), rotation_angle=270):

    for root, dirs, files in os.walk(origin_folder):
        try:
            for filename in files:
                raw_filename, ext = os.path.splitext(filename)
                im = Image.open(origin_folder + "/" + filename).convert('RGB')
                im.thumbnail(size)
                new_filename = raw_filename + ".jpeg"
                im.rotate(rotation_angle).save(destination_folder + "/" + new_filename)
                im.close()

        except OSError:
            print("Error: aborting the script...")
    return None



my_folder = r"C:\Users\Nikolas\Pycharm Projects\Google IT Automation\Course 6\Week 1\images"
my_destination_folder = r"C:\Users\Nikolas\Pycharm Projects\Google IT Automation\Course 6\Week 1\opt\icons"
image_manipulation(my_folder, my_destination_folder)


"""

import os, sys
from PIL import Image

size = (128, 128)


for filename in os.listdir():
    outfile = os.path.splitext(filename)[0]
    try:
        with Image.open(filename).convert('RGB') as im:
            im.thumbnail(size)
            im.rotate(270).save("/opt/icons/" + outfile, "JPEG")
    except OSError:
        pass

"""


