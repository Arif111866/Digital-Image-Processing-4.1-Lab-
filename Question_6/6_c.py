import cv2
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

def boundary_extraction(image , structuring_element):
   image_erosion = erosion(image, structuring_element)
   image_boundary = image - image_erosion
   return image_boundary

image = cv2.imread('./Lincoln 221x269.tif', 0)
plt.subplot(1,2,1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

bounday = boundary_extraction(image, np.ones((3, 3)))
plt.subplot(1,2,2)
plt.imshow(bounday, cmap='gray')
plt.title('Boundary Image')
plt.show()
