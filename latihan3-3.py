import cv2
from cv2 import waitKey
from matplotlib import pyplot as plt
import numpy as np

img1 = cv2.imread("image/bird.jpg")
img2 = cv2.imread("image/pohon.jpg")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
op_and=cv2.bitwise_and(img1,img2)
op_or=cv2.bitwise_or(img1,img2)
op_xor=cv2.bitwise_xor(img1,img2)
cv2.imshow('Image 1', img1)
waitKey(0)
cv2.imshow('Image 2', img2)
waitKey(0)
cv2.imshow('And', op_and)
waitKey(0)
cv2.imshow('OR', op_or)
waitKey(0)
cv2.imshow('XOR', op_xor)
waitKey(0)