import numpy as np
import cv2

video_read = cv2.VideoCapture(0)

while True:
    ret, frame = video_read.read()
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

video_read.release()
cv2.destroyAllWindows()