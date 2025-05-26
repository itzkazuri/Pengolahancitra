import cv2
import numpy as np
from matplotlib import pyplot as plt

# Baca gambar dan ubah ke grayscale
img = cv2.imread('image/download.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Tampilkan gambar grayscale
cv2.imshow('Gambar Bunga Grayscale', gray_img)

# Tampilkan histogram grayscale
histr = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
plt.plot(histr)
plt.title('Histogram Grayscale')
plt.show()

# Proses Negasi
h, w = gray_img.shape[:2]
max_intensity = 255
neg_img = np.zeros_like(gray_img)

for i in range(h):
    for j in range(w):
        a = gray_img.item(i, j)
        b = max_intensity - a
        neg_img.itemset((i, j), b)

# Tampilkan gambar hasil negasi
cv2.imshow('Gambar Negasi', neg_img)

# Histogram hasil negasi
histr_neg = cv2.calcHist([neg_img], [0], None, [256], [0, 256])
plt.plot(histr_neg)
plt.title('Histogram Citra Negasi')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
