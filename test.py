import cv2
import RPi.GPIO as GPIO
import time
import os

stop_cascade = cv2.CascadeClassifier('work.xml')
img = cv2.imread('stop.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sign = stop_cascade.detectMultiScale(gray, 1.1, 4)

for(x, y, w, h) in sign:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 255), 3)

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()