import cv2

cap=cv2.VideoCapture(0)

def draw_circle(event,x,y,flags,params):
    global draw,pt
    
    if event==cv2.EVENT_LBUTTONDOWN:
        
        draw=True
        pt=(x,y)
        
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

draw=False
pt=(-1,-1)

cv2.namedWindow(winname='Test')
cv2.setMouseCallback('Test',draw_circle)

while True:
    
    ret,frame=cap.read()
    
    if draw==True and ret==True:
        
        cv2.circle(frame,pt,radius=50,color=(255,0,0),thickness=5)
        

    cv2.imshow('Test',frame)
        
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()