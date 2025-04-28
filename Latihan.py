import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar
img = cv2.imread("image/download.jpg")

# Periksa apakah gambar berhasil dimuat
if img is None:
    print("Error: Gambar tidak ditemukan!")
    exit()

# Konversi dari BGR ke HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Memisahkan channel Hue, Saturation, dan Value
h, s, v = cv2.split(hsv)

# Menampilkan semua channel secara berdampingan
hsv_combined = np.hstack((h, s, v))

# Menampilkan hasil
cv2.imshow('Original Image', img)
cv2.imshow('Hue Channel', h)
cv2.imshow('Saturation Channel', s)
cv2.imshow('Value Channel', v)
cv2.imshow('HSV Channels Combined', hsv_combined)

# Menampilkan histogram dari channel Hue
plt.figure(figsize=(6, 4))
plt.hist(h.ravel(), bins=180, range=[0, 180], color='orange', alpha=0.7)
plt.title('Histogram of Hue Channel')
plt.xlabel('Hue Value')
plt.ylabel('Frequency')
plt.grid()
plt.show()

# Menyimpan hasil konversi
cv2.imwrite("output/hue_channel.jpg", h)
cv2.imwrite("output/saturation_channel.jpg", s)
cv2.imwrite("output/value_channel.jpg", v)

# Menunggu input tombol sebelum keluar
cv2.waitKey(0)
cv2.destroyAllWindows()
