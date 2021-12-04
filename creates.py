import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')

# RGB - стандартный формат
# BGR - формат opencv

# photo[10:150, 200:280] = 110, 72, 15
cv2.rectangle(photo, (50, 70), (100, 100), (110, 72, 15), thickness=cv2.FILLED)  # создание квадрата

cv2.line(photo, (0, photo.shape[0]//2), (photo.shape[1], photo.shape[1]//2), (110, 72, 15), thickness=3)  # создание линии

cv2.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 100, (110, 72, 15), thickness=1)  # создание круга

cv2.putText(photo, 'ItProger', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (250, 0, 0), thickness=1)  # создание текста

cv2.imshow('Photo', photo)
cv2.waitKey(0)
