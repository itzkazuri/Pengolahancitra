import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. INTENSITY SLICING (PEMOTONGAN INTENSITAS)
# Membaca gambar dalam format grayscale (citra keabuan)
img = cv2.imread('image/image.jpg', 0)  # parameter 0 berarti grayscale

# Menentukan batas bawah dan batas atas intensitas yang ingin dipertahankan
lower, upper = 100, 200  # piksel dengan nilai 100-200 akan diubah menjadi putih (255)

# Melakukan pemotongan intensitas:
# - Jika nilai piksel berada di antara lower dan upper, maka diubah menjadi 255 (putih)
# - Jika di luar rentang tersebut, maka diubah menjadi 0 (hitam)
# - Hasilnya dikonversi ke tipe data uint8 (0-255)
sliced = np.where((img >= lower) & (img <= upper), 255, 0).astype(np.uint8)

# Menampilkan citra hasil pemotongan intensitas
plt.imshow(sliced, cmap='gray')
plt.title('Intensity Slicing')
plt.show()

# 2. BIT PLANE SLICING (PEMOTONGAN BIDANG BIT)
# Fungsi untuk melakukan pemotongan bidang bit
def bit_plane_slicing(img, bit):
    # Menggeser bit ke kanan sesuai dengan bit yang diinginkan
    # Kemudian mengambil bit paling kanan (LSB) dengan operasi AND 1
    # Hasil operasi dikalikan 255 untuk mendapatkan citra biner (0 atau 255)
    return ((img >> bit) & 1) * 255

# Membaca gambar dalam format grayscale
img = cv2.imread('gambar/image.jpg', 0)

# Ekstraksi bit plane ke-1 (dari 0-7, dengan 0 = LSB, 7 = MSB)
bit4 = bit_plane_slicing(img, 1)

# Menampilkan hasil bit plane slicing
plt.imshow(bit4, cmap='gray')
plt.title('Bit Plane 4')  # Catatan: variabel bernama bit4 tapi titlenya 'Bit Plane 4'
plt.show()

# 3. LOG TRANSFORMATION (TRANSFORMASI LOGARITMIK)
# Membaca gambar dalam format grayscale
img = cv2.imread('gambar/image.jpg', 0)

# Mengubah tipe data ke float32 untuk operasi matematika yang akurat
img_float = img.astype(np.float32)

# Menghitung faktor skala c = 255 / log(1 + nilai piksel maksimum)
# Ini untuk memastikan nilai output tetap dalam rentang 0-255
c = 255 / np.log(1 + np.max(img_float))

# Menerapkan transformasi logaritmik: s = c * log(1 + r)
# di mana r adalah nilai piksel input
# Transformasi ini memperluas nilai piksel gelap dan memampatkan nilai piksel terang
log_transformed = c * np.log(1 + img_float)

# Mengkonversi kembali ke tipe data uint8 untuk ditampilkan
log_transformed = np.array(log_transformed, dtype=np.uint8)

# Menampilkan hasil transformasi logaritmik
plt.imshow(log_transformed, cmap='gray')
plt.title('Log Range Compression')
plt.show()

# 4. HISTOGRAM EQUALIZATION (PENYAMAAN HISTOGRAM)
# Melakukan penyamaan histogram untuk meningkatkan kontras
# Metode ini mendistribusikan ulang nilai piksel agar histogram lebih merata
equalized = cv2.equalizeHist(img)

# Menampilkan hasil penyamaan histogram
plt.imshow(equalized, cmap='gray')
plt.title('Histogram Equalization')
plt.show()

# 5. CLAHE - CONTRAST LIMITED ADAPTIVE HISTOGRAM EQUALIZATION
# (PENYAMAAN HISTOGRAM ADAPTIF DENGAN BATASAN KONTRAS)
# Membuat objek CLAHE dengan batas klip 2.0 dan ukuran grid 8x8
# CLAHE bekerja pada area lokal (blok), tidak seluruh gambar
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# Menerapkan CLAHE pada gambar
# CLAHE mencegah penguatan noise yang berlebihan dibandingkan dengan equalizeHist biasa
adaptive_eq = clahe.apply(img)

# Menampilkan hasil CLAHE
plt.imshow(adaptive_eq, cmap='gray')
plt.title('Adaptive Histogram Equalization (CLAHE)')
plt.show()