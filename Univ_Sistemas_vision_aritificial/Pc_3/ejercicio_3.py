import numpy as np
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'<C:\Program Files\Tesseract-OCR\tesseract>'

img = cv2.imread("dni.png",0)
crop = img[50:500, 200:700]
texto = pytesseract.image_to_string(img)
cv2.imshow('imagen', img)
print(texto)

cv2.waitKey(0)
cv2.destroyAllWindows()

