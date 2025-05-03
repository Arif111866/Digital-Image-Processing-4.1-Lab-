import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("./Dollar 1192x500.tif" , cv2.IMREAD_GRAYSCALE)
plt.subplot(3, 1, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

mask = '11100000'
new_image = image & int(mask, 2)
plt.subplot(3, 1, 2)
plt.imshow(new_image, cmap='gray')
plt.title('Masked Image')

diff = cv2.absdiff(np.array(image), np.array(new_image))
plt.subplot(3, 1, 3)
plt.imshow(diff, cmap='gray')
plt.title('Difference Image')
plt.show()