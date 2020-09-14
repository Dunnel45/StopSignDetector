import urllib.request
import cv2
import numpy as np
import os


with open('links.txt') as f:
    lines = f.read().split('\n')
    pic_num = 235
    for i in lines:
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg")
            resized_image = cv2.resize(img, (100,100))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
        
        except Exception as e:
            print(str(e))