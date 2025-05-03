import cv2
import numpy as np
import matplotlib.pyplot as plt

def histrogram(image, k):
    height = image.shape[0]
    width = image.shape[1]
    hist = np.zeros((256))
    for i in range(height):
        for j in range(width):
            hist[image[i][j]] += 1
    plt.subplot(2, 4, k)
    plt.bar(range(256), hist, width=1, color='black')
    plt.title("Histogram")

image = cv2.imread("./Skeleton 750x1482.tif", cv2.IMREAD_GRAYSCALE)
plt.subplot(2, 4, 2)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
histrogram(image, 1)

threshold = 50
new_image = np.zeros(image.shape, dtype=np.uint8)
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j] > threshold:
            new_image[i][j] = 255
        else:
            new_image[i][j] = 0
plt.subplot(2, 4, 3)
plt.imshow(new_image, cmap='gray')
plt.title("Thresholded Image")

histrogram(new_image, 4)

plt.show()