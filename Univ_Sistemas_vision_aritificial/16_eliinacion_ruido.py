import cv2
import numpy as np

img = cv2.imread('perros_1.jpg',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations=1)
opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
cv2.imshow('Imagen original', img)
cv2.imshow('Erosion ruido', erosion)
cv2.imshow('Eliminacion de ruido', opening)
cv2.waitKey(0)
cv2.destroyAllWindows()