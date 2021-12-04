import cv2
import numpy as np

photo = cv2.imread('images/download.jpg')
img = np.zeros(photo.shape[:2], dtype='uint8')

circle = cv2.circle(img.copy(), (100, 100), 120, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

img = cv2.bitwise_and(photo, photo, mask=square)
# img = cv2.bitwise_or(circle, square)
# img = cv2.bitwise_xor(circle, square)
# img = cv2.bitwise_not(circle, square)

cv2.imshow('result', img)
cv2.waitKey(0)
