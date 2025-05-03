import cv2
import numpy as np
import matplotlib.pyplot as plt


def power_laws(image , gama):
    new_image = image.copy() 
    hight = image.shape[0]
    widht = image.shape[1]
    for i in range(hight):
        for j in range(widht):
            new_image[i][j] = 255 * (float(image[i][j] / 255) ** gama)
    return np.uint8(new_image)

def inverse_logarithm(image):
    new_image = image.copy()
    hight = image.shape[0]
    widht = image.shape[1]
    c = 255 / np.log(1 + 255)
    for i in range(hight):
        for j in range(widht):
            new_image[i][j] = np.exp(image[i][j] / c) - 1
    return np.uint8(new_image)

gamas = [0.5 , 0.75 ,  1  , 5]
image = cv2.imread("./Aerial Image 765x769.tif" , cv2.IMREAD_GRAYSCALE)

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
for i in range(4):
    new_image = power_laws(image , gamas[i])
    plt.subplot(2, 3, i+2)
    plt.imshow(new_image, cmap='gray')
    plt.title(f'Power Law with gama = {gamas[i]}')

new_image = inverse_logarithm(image)
plt.subplot(2, 3, 6)
plt.imshow(new_image, cmap='gray')
plt.title('Inverse Logarithm')
plt.show()