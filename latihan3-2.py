import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
img = cv2.imread("image/pohon.jpg")

# Cek apakah gambar ditemukan
if img is None:
    print("Gambar tidak ditemukan. Periksa jalur file!")
    exit()

# Ubah ke grayscale
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Tambah brightness dengan metode lebih cepat menggunakan NumPy
brightness = 50
img_bright = np.clip(img2 + brightness, 0, 255).astype(np.uint8)

# Tampilkan gambar menggunakan Matplotlib
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Gambar asli
axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0].set_title("Gambar Asli")
axs[0].axis("off")

# Gambar grayscale
axs[1].imshow(img2, cmap="gray")
axs[1].set_title("Grayscale")
axs[1].axis("off")

# Gambar setelah brightness ditambahkan
axs[2].imshow(img_bright, cmap="gray")
axs[2].set_title("Brightness +50")
axs[2].axis("off")

plt.show()
