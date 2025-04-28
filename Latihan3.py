import cv2
from matplotlib import pyplot as plt
import numpy as np

# Load image
img = cv2.imread("image/pohon.jpg")

# Cek apakah gambar ditemukan
if img is None:
    print("Gambar tidak ditemukan. Periksa jalur file!")
    exit()

# Konversi ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Plot gambar
fig = plt.figure()
fig.add_subplot(211)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # Konversi ke RGB untuk plt.imshow()
plt.axis('off')

fig.add_subplot(212)
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.show()
