import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_decress(image, bit):
    height = image.shape[0]
    width = image.shape[1]
    new_image = np.zeros((height, width))
    step = 255 / (2**bit - 1)
    for i in range(height):
        for j in range(width):
            new_image[i][j] = round(image[i][j] / step) * step
    return new_image.astype(np.uint8)  # Convert to uint8

image = cv2.imread("./Skull 374x452.tif", 0)
# image = cv2.imread("./Rose 1024x1024.tif" , cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (512, 512))

for i in range(1, 9):
    plt.subplot(2, 4, i)
    new_image = image_decress(image, i)
    plt.imshow(new_image, cmap='gray')
    plt.title(f"image show in {i}")

plt.show()