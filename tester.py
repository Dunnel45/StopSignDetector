import cv2
import RPi.GPIO as GPIO
from time import ctime
import os

def talker(sentence):
    cmd = 'flite -voice kal16 -t "' + sentence + '"'
    os.system(cmd)

def detecter():
    stop_cascade = cv2.CascadeClassifier('work.xml')
    cap = cv2.VideoCapture('test.mp4')
    found = False

    while cap.isOpened():
        ret, img = cap.read()
    
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        signs = stop_cascade.detectMultiScale(gray, 30, 30)
    
        for (x, y, w, h) in signs:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 255), 3)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'stop sign', (x-w, y-h), font, 0.5, (255,255,0), 2, cv2.LINE_AA)
            cv2.putText(img, "Status: {}".format('Detected'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            f = open('log.txt', 'w')
            f.write('Stop sign detected at '+ctime() +'\n')
            f.close()
        
        if not found:
            talker('Stop sign detected ahead, stop before the sign')
            found = True
    
    
        cv2.imshow('img', img)
        if cv2.waitKey(40) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    print('beginning detection')
    detecter()

if __name__ == '__main__':
    main()