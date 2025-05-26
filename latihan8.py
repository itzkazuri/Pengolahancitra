import cv2
import numpy as np
from cv2 import waitKey

# Baca gambar
img = cv2.imread('image/bird.jpg')  # Ganti dengan path gambar Anda
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Definisikan kernel berbagai ukuran
kernels = {
    '3x3': cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)),
    '5x5': cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)),
    '7x7': cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7)),
    '9x9': cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
}

# Lakukan thickening dengan masing-masing kernel
results = {}
for name, kernel in kernels.items():
    dilated = cv2.dilate(binary, kernel, iterations=1)
    results[name] = dilated

# Tampilkan semua hasil
cv2.imshow("Citra Biner", binary)
for name, result in results.items():
    cv2.imshow(f"Thickening {name}", result)

waitKey(0)
cv2.destroyAllWindows()