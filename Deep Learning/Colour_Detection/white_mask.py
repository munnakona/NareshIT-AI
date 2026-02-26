# Only Red color detection
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # white color
    low_white = np.array([0, 42, 0]) # lowest hue would be - 0,0,200( how do i found this i tested before and found this) 
    high_white = np.array([180, 255, 255])
    #mask = cv2.inRange(hsv_frame, low_red, high_red) 
        
    white_mask = cv2.inRange(hsv_frame, low_white, high_white) #we create maskk on hsv frame and then low red or high red
    white = cv2.bitwise_and(frame, frame, mask=white_mask)
    cv2.imshow("Frame", frame) 
    #cv2.imshow('Red mask', mask) 
    cv2.imshow('White', white)
   
    key = cv2.waitKey(1)
    if key ==27:
        break
