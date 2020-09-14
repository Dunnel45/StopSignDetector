import urllib.request
import cv2
import numpy as np
import os

i = 103
for file in os.listdir():
    print(file)
    img = cv2.imread(file)
    resized_image = cv2.resize(img, (50,50))
    cv2.imwrite(str(i),resized_image)
    i+=1