import numpy as np
import cv2
import pytesseract

img = cv2.imread("../gareca_dni.png",0)
crop_primer_apellido = img[55:97, 200:373]
crop_prenombres = img[182:227, 207:544]

texto_primer_apellido = pytesseract.image_to_string(crop_primer_apellido)
texto_prenombres = pytesseract.image_to_string(crop_prenombres)

cv2.imshow('Primer Apellido', crop_primer_apellido)
cv2.imshow('Pre nombres', crop_prenombres)

print(f'Primer Apellido: {texto_primer_apellido}')
print(f'Pre nombres: {texto_prenombres}')

cv2.waitKey(0)
cv2.destroyAllWindows()
