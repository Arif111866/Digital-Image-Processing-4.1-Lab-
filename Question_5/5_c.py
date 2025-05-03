import cv2
import numpy as np
import matplotlib.pyplot as plt

def adaptive_threshold(image, max_itaration = 100, elipson = 0.5):
    T = np.mean(image)
    for i in range(max_itaration):
        G1 = image[image < T]
        G2 = image[image >= T]
        new_T = (np.mean(G1) + np.mean(G2)) / 2
        if abs(new_T - T) < elipson:
            break
        T = new_T
    return T
def histrogram(image, k):
    height = image.shape[0]
    width = image.shape[1]
    hist = np.zeros((256))
    for i in range(height):
        for j in range(width):
            hist[image[i][j]] += 1
    plt.subplot(2, 2, k)
    plt.bar(range(256), hist, width=1, color='black')
    plt.title("Histogram")

image = cv2.imread('./cards.tif', 0)
plt.subplot(2 , 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
histrogram(image, 3)

Theshold = adaptive_threshold(image)
new_image = image.copy()
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j] < Theshold:
            new_image[i][j] = 0
        else:
            new_image[i][j] = 255
plt.subplot(2 , 2, 2)
plt.imshow(new_image, cmap='gray')
plt.title('Adaptive Thresholded Image')
histrogram(new_image, 4)

plt.show()


    