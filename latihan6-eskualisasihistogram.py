import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image/image.jpg', 0)
cv2.imshow('Citra Asli', img)

histo_asli = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(histo_asli)
plt.show()

img_ekual = cv2.equalizeHist(img)
cv2.imshow('Hasil Ekualisasi Citra', img_ekual)

histo_hasil = cv2.calcHist([img_ekual], [0], None, [256], [0, 256])
plt.plot(histo_hasil)
plt.show()

cv2.waitKey(0)