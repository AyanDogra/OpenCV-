import cv2

cap = cv2.VideoCapture(0)
pt1=(0,0)
pt2=(0,0)
Rbottom_clicked=False
Ltop_clicked=False

def draw_rectangle(event,x,y,flags,params):
    global pt1,pt2,Rbottom_clicked,Ltop_clicked
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if Ltop_clicked == True and Rbottom_clicked == True:
            Ltop_clicked = False
            Rbottom_clicked = False
            pt1 = (0,0)
            pt2 = (0,0)

        if Ltop_clicked == False:
            pt1 = (x,y)
            Ltop_clicked = True
            
        elif Rbottom_clicked == False:
            pt2 = (x,y)
            Rbottom_clicked = True



cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rectangle)

while True:
    
    ret,frame = cap.read()
    if Ltop_clicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0,0,255), thickness=-1)
        
    if Ltop_clicked and Rbottom_clicked:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 2)
    
    cv2.imshow('Test',frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

