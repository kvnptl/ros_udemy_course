import numpy as np
import cv2

#read image as it is
img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0,0), (511, 511), (255,255,255), 5)
cv2.rectangle(img, (384,0), (512,128), (255,255,0), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'ROS OpenCV course', (10, 500), font, 2, (255,255,255), 2, cv2.LINE_AA)

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()