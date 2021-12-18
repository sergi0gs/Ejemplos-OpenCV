import cv2 
import numpy as np

# Umbral binario
gray = cv2.imread('../zapatillas_1.jpg', 0)

t, dst = cv2.threshold(gray, 170, 255, cv2.THRESH_TRUNC)

cv2.imshow('umbral', gray)
cv2.imshow('result', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()