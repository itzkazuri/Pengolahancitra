import cv2
import numpy as np

# Load gambar
image = cv2.imread('image/pohon.jpg')

# Filter mean manual (konvolusi kernel 3x3)
kernel = np.ones((3,3), np.float32)/9
processed_image = cv2.filter2D(image, -1, kernel)

# Filter Mean Blur built-in OpenCV
mean_blur = cv2.blur(image, (5,5))

# Gaussian Blur built-in OpenCV
gaussian_blur = cv2.GaussianBlur(image, (5,5), 0)

# Tampilkan hasil
cv2.imshow('Original', image)
cv2.imshow('Mean Manual', processed_image)
cv2.imshow('Mean Blur', mean_blur)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
