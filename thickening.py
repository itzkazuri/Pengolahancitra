import cv2
import numpy as np
from cv2 import waitKey

# Baca gambar
img = cv2.imread('image/bravo.png')  # Ganti dengan path gambar Anda

# Konversi ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding untuk jadikan citra biner
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Elemen struktur
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# Operasi dilasi sebagai thickening
thickened = cv2.dilate(binary, kernel, iterations=1)

# Tampilkan hasil
cv2.imshow('Citra Asli', img)
cv2.imshow('Setelah Threshold', binary)
cv2.imshow('Hasil Thickening', thickened)

waitKey(0)
cv2.destroyAllWindows()