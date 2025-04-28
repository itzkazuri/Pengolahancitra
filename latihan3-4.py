import cv2
from cv2 import waitKey
from matplotlib import pyplot as plt
import numpy as np
img1 = cv2.imread("image/bird.jpg")
img2 = cv2.imread("image/pohon.png")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
brightness = 10
h,w = img2.shape[:2]
#perulangan untuk melakukan proses pertambahan
# b=img2+img1
b=img1+100
        
cv2.imshow('Gambar Asli1', img1)
cv2.imshow('Gambar Asli2', img2)
cv2.imshow('Gambar Hasil', b)
cv2.waitKey()