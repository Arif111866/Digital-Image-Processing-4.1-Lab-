import cv2
import numpy as np
import matplotlib.pyplot as plt


def image_enhancement(image, x , y , value):
    height, width = image.shape
    for i in range(height):
        for j in range(width):
            if image[i][j] >= x and image[i][j] <= y:
                image[i][j] = max(image[i][j]+40 , 255)
    return image


image = cv2.imread("./Fractured Spine 746x976.tif", 0)
plt.subplot(2,1,1)
plt.imshow(image, cmap="gray")
plt.title("original image")
image = image_enhancement(image , 20 , 50 , 50)
plt.subplot(2,1,2)
plt.imshow(image , cmap = "gray")
plt.title("enhanched image")

plt.show()