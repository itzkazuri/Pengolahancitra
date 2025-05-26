import cv2
import numpy as np
from cv2 import waitKey

# Baca gambar
img = cv2.imread('image/images.jpeg')  # Ganti dengan path gambar Anda
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding untuk membuat citra biner
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Menampilkan citra threshold
cv2.imshow('Citra Biner', thresh)

# Elemen struktur untuk transformasi hit-or-miss
kernel = np.array((
    [1, 1, 1],
    [0, 1, -1],
    [0, 1, -1]), dtype="int")

# Operasi Hit-or-Miss
hitmiss = cv2.morphologyEx(thresh, cv2.MORPH_HITMISS, kernel)

# Tampilkan hasil
cv2.imshow('Citra Asli', img)
cv2.imshow('Hit-or-Miss Result', hitmiss)

waitKey(0)
cv2.destroyAllWindows()