import numpy as np
import cv2
import matplotlib.pyplot as plt

def image_decress(image):
    height = image.shape[0] // 2
    width = image.shape[1] // 2
    new_image = np.zeros((height, width))
    for i in range (height):
        for j in range(width):
            new_image[i][j] = image[i * 2][j * 2]
    return new_image

image = cv2.imread("./Rose 1024x1024.tif" , cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (512, 512))
# original image
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
# decressed image by 2
image = image_decress(image)
plt.subplot(2, 2, 2)
plt.imshow(image, cmap='gray')
plt.title('Decressed Image by 2')
# 

plt.subplot(2, 2, 3)
image = image_decress(image)
plt.imshow(image, cmap='gray')
plt.title('Decressed Image by 4')

# decressed image by 8
image = image_decress(image)
plt.subplot(2, 2, 4)
plt.imshow(image, cmap='gray')
plt.title('Decressed Image by 8')

plt.show()


