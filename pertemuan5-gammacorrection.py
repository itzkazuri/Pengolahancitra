import cv2
import numpy as np

# Fungsi gamma correction
def gammaCorrection(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

# Baca gambar
img = cv2.imread('image/download.jpg')

# Lakukan gamma correction
gamma_value = 2.2  # ganti sesuai kebutuhan, misal 0.5, 1.5, dll
gamma_corrected_img = gammaCorrection(img, gamma_value)

# Tampilkan gambar asli dan hasil gamma correction
cv2.imshow('Gambar Asli', img)
cv2.imshow(f'Gamma Corrected (gamma={gamma_value})', gamma_corrected_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
