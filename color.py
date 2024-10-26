import cv2
from util import get_limits
from PIL import Image

yellow =[0,255,255] #yellow in the BRG colorspace
cap = cv2.VideoCapture(0)

while True:
    ret, frame =cap.read()

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=yellow)

    mask =cv2.inRange(hsv_img,lowerLimit,upperLimit)
    mask_ = Image.fromarray(mask)
    
    bbox = mask_.getbbox()
    if bbox is not None:
        x1,y1,x2,y2 = bbox
        frame = cv2.rectangle(frame, (x1,y1),(x2,y2),(255,0,0),5)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()