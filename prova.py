import cv2
import numpy as np

cap = cv2.VideoCapture("rtsp://192.168.1.6:8554/live.sdp")

while(True):
    ret, frame = cap.read()
    cv2.imshow('VIDEO', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
