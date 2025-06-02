import cv2 as cv 
import matplotlib.pyplot as plt 

img = cv.imread('image/image.jpg', cv.COLOR_BGR2GRAY) 
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB) 

grayImage = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 

dst = cv.Laplacian(grayImage, cv.CV_16S, ksize=3) 
Laplacian = cv.convertScaleAbs(dst) 

titles = ['Original image', 'the Laplacian operator'] 
images = [rgb_img, Laplacian] 

for i in range(2): 
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray') 
    plt.title(titles[i]) 
    plt.xticks([]), plt.yticks([]) 
plt.show()
