import cv2
import numpy as np

# Load the image, nilai 0 berarti image dibaca dalam format greyscale
img = cv2.imread('image/bird.jpg', 0) 
cv2.imshow('Original image', img)

# Cari nilai height dan width
row, column = img.shape

# Buat zeros array untuk menyimpan slice image
img1 = np.zeros((row, column), dtype='uint8')

# Tentukan nilai batas min and max
min_range = 75
max_range = 150

# Perulangan sejumlah input dan jika nilai pixel memenuhi kondisi set ke 0 dan jika tidak set nilai pixel yang asli
for i in range(row):
    for j in range(column):
        if img[i, j] > min_range and img[i, j] < max_range:
            img1[i, j] = 0
        else:
            img1[i, j] = img[i, j]

# Tampilkan image
cv2.imshow('sliced image', img1)
cv2.waitKey(0)