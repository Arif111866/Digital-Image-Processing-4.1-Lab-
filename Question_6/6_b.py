import  cv2
import numpy as np
import matplotlib.pyplot as plt


def erosion(image, structuring_element):
    hight = image.shape[0]
    width = image.shape[1]
    structuring_element *= 255
    kernel_hight = structuring_element.shape[0]
    kernel_width = structuring_element.shape[1]
    offset = kernel_hight // 2
    result = image.copy()
    for i in range(hight):
        for j in range(width):
            fit = True
            for x in range(-offset, offset + 1):
                for y in range(-offset, offset + 1):
                    if(i+x >= 0 and i+x < hight and j+y >= 0 and j+y < width):
                        if(structuring_element[x + offset, y + offset] and image[i + x, j + y] !=  structuring_element[x + offset, y + offset]):
                            fit = False
                    elif (structuring_element[x + offset, y + offset]):
                        fit = False
            if fit:
                result[i, j] = 255
            else:
                result[i, j] = 0
    return np.uint8(result)

def dilation(image, structuring_element):
    dilated_image = image.copy()
    offset = structuring_element.shape[0] // 2
    structuring_element = structuring_element * 255
    height, width = image.shape
    for r in range(height):
        for c in range(width):
            hit = False
            for x in range(-offset, offset + 1):
                for y in range(-offset, offset + 1):
                    if (r + x >= 0 and r + x < height and c + y >= 0 and c + y < width):
                        sr, sc = x + offset, y + offset
                        if (structuring_element[sr, sc] and image[r + x, c + y] == 255):
                            hit = True
            dilated_image[r, c] = 255 if hit else 0

    return np.uint8(dilated_image)

def opening(image, structuring_element):
    open_image = dilation(erosion(image, structuring_element), structuring_element)
    return open_image
def closing(image, structuring_element):
    close_image = erosion(dilation(image, structuring_element), structuring_element)
    return close_image

image = cv2.imread('./Noisy Fingerprint 315x238.tif', 0)
plt.subplot(1,5,1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

open = opening(image, np.ones((3, 3)))
plt.subplot(1,5,2)
plt.imshow(open, cmap='gray')
plt.title('Opening Image')

close = closing(image, np.ones((3, 3)))
plt.subplot(1,5,3)
plt.imshow(close, cmap='gray')
plt.title('Closing Image')

plt.show()