import numpy as np
import cv2

#read image as it is
img = cv2.imread('src/opencv_learn/test.jpg', -1)

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)
# cv2.waitKey(0)

blue, green, red = cv2.split(img)

# cv2.namedWindow("blue", cv2.WINDOW_NORMAL)
# cv2.imshow('blue', blue)
# cv2.waitKey(0)

# cv2.namedWindow("green", cv2.WINDOW_NORMAL)
# cv2.imshow('green', green)
# cv2.waitKey(0)

# cv2.namedWindow("red", cv2.WINDOW_NORMAL)
# cv2.imshow('red', red)

# hue, saturation, value color encoding

# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(hsv)
# hsv_image = np.concatenate((h,s,v), axis=1)
# cv2.namedWindow("Hue, Saturation, Value Image", cv2.WINDOW_NORMAL)
# cv2.imshow('Hue, Saturation, Value Image', hsv_image)

# Gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Gray Image", cv2.WINDOW_NORMAL)
# cv2.moveWindow("Gray Image", 0, 0)
cv2.imshow('Gray Image', gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()