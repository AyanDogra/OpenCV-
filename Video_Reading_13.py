import cv2
import time

cap=cv2.VideoCapture('myvid.mp4')

if cap.isOpened()==False:
    print('File path incorrect')
    
while cap.isOpened():
    
    ret,frame = cap.read()
    
    if ret:
        
        time.sleep(1/20)
        cv2.imshow('frame',framd)
        
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()