import urllib.request
import cv2
import numpy as np
import os


    
for img in os.listdir('postives'):
    path = '/home/pi/car-project/postives/'
    if len(str(img)) > 8:
        path += str(img)
        os.remove(path)