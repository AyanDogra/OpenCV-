import cv2 
import numpy as np

face_cascade = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_frontalface_default.xml')

def face_detection(img):
    face_img=img.copy()
    face_reacts=face_cascade.detectMultiScale(face_img)
    for (x,y,w,h) in face_reacts:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)
    return face_img

cap=cv2.VideoCapture(0)

while True:
    
    ret,frame=cap.read()
    
    frame=face_detection(frame)
    
    cv2.imshow('Face',frame)
    
    k=cv2.waitKey(1)
    
    if k==27:
        break
    
    
cap.release()
cv2.destroyAllWindows()