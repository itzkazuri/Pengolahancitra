import cv2
import numpy as np

# baca gambar input dengan format warna
image = cv2.imread("image/image.jpg")

# ubah menjadi citra grayscale
image_bw = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

equalized = cv2.equalizeHist(image_bw)

# Deklarasi CLAHE
# clipLimit -> Threshold for contrast limiting
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
final_img = clahe.apply(image_bw) + 30

# tampilkan citra hasil
cv2.imshow("Equalization Histogram", equalized)
cv2.imshow("Adaptive Histogram", final_img)
cv2.waitKey(0)