import urllib.request
import cv2
import numpy as np
import os


file = 'work.jpg'
img = cv2.imread(file)
resized_image = cv2.resize(img, (150,150))
cv2.imwrite(file,resized_image)
        