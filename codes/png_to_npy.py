"""
project:      NIH Chest XRay dataset
date:         04/01/2018
developed by: Debanjan Paul
filename:     png_to_npy.py
version:      0.1
description:  Converts png images contained in a directory to numpy
dependencies:	NumPy
                PIL
		
"""

# Imports

import numpy as np
import os
from PIL import Image

# Capture directory of images
images_dir = "/path/to/your/location/NIHChestXRayDataSample/images"

# Change to images_dir
os.chdir(images_dir)

#Load Images into one numpy matrix
for i in os.listdir():
  # Convert images to grayscale with Image.convert(mode='L')
  # http://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.Image.convert
  image = Image.open(i).convert('L')
  try:
    image_array = np.dstack((image_array,np.array(image)))
  except:
    image_array = np.array(image)

np.save("../datasets/nih_chest_xray_sample.npy", image_array)
