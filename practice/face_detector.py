import cv2
import RPi.GPIO as GPIO
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    

        
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)
    
    
    cv2.imshow('img', img)
    if cv2.waitKey(40) == 27:
        break

cap.release()            