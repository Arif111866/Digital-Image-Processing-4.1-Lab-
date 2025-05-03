import cv2
import numpy as np
import matplotlib.pyplot as plt


def histrogram(image, subplot_index):
    hist = np.zeros(256, dtype=np.int32)
    height, width = image.shape
    for i in range(height):
        for j in range(width):
            hist[image[i, j]] += 1
    plt.subplot(2, 4, subplot_index)
    plt.bar(range(256), hist, color='black')
    plt.title('Histogram')

def segmentation(image, threshold, subplot_index):
    height, width = image.shape
    new_image = image.copy()
    for r in range(height):
        for c in range(width):
            if image[r, c] < threshold:
                new_image[r, c] = 0
            else:
                new_image[r, c] = 255
    plt.subplot(2, 4, subplot_index)
    plt.imshow(new_image, cmap='gray')
    plt.title('Segmented ' + str(threshold))
    histrogram(new_image, subplot_index + 4)


image = cv2.imread('./cards.tif' , 0)
plt.subplot(2,4,1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
histrogram(image, 5)

segmentation(image , 50 , 2)
segmentation(image , 100 , 3)
segmentation(image , 150 , 4)

plt.show()
