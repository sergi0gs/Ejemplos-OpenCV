import numpy as np
import cv2

img = cv2.imread('Univ_Sistemas_vision_aritificial\perros_4.jpg',0)
kernel = np.ones((3,3), np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('Eliminacion de ruido', gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
