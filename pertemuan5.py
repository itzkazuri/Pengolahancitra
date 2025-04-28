# Import library yang dibutuhin
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Baca gambar dari folder yang udah ditentukan
img = cv2.imread('image/bird.jpg')

# Cek dulu, takutnya gambarnya ngga kebaca
if img is None:
    print("⚠️ Gambar tidak ditemukan. Cek lagi path atau nama file-nya.")
else:
    # Kalau gambar kebaca, lanjut gas pol
    color = ('b', 'g', 'r')  # BGR sesuai OpenCV

    for i, col in enumerate(color):
        # Hitung histogram untuk masing-masing channel
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])

    # Tampilkan histogram
    plt.title('Histogram Citra Bunga')
    plt.xlabel('Intensitas Pixel')
    plt.ylabel('Jumlah Pixel')
    plt.show()
