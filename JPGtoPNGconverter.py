import sys
import os
from PIL import Image

path = sys.argv[1]
directory = sys.argv[2]

if not os.path.exists(directory):
    os.makedirs(directory)

for filename in os.listdir(path):
    if filename.endswith(".jpg"):
        img = Image.open(os.path.join(path, filename))
        img.save(os.path.join(directory, filename.replace(".jpg", ".png")))
    print('all done!')
