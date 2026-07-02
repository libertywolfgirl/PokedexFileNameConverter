import sys
import os
from PIL import Image

image_folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for filename in os.listdir(image_folder):
    if filename.endswith(".jpg"):
        img = Image.open(os.path.join(image_folder, filename))
        img.save(os.path.join(new_folder, filename.replace(".jpg", ".png")))
    print('all done!')
