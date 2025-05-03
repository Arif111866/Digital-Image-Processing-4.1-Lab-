import cv2
import numpy as np
import matplotlib.pyplot as plt

def PSNR(image, noise_image):
    mse = np.mean((image - noise_image)** 2)
    if mse == 0:
        return "infinity"
    max_pixel = 255.0
    psnr = 10 * np.log10((max_pixel**2) / mse)
    return psnr.round(2)

def avg_filter(image, kernel_size):
    new_image = image.copy()
    hight = image.shape[0]
    widht = image.shape[1]
    offset = kernel_size // 2
    weight = kernel_size * kernel_size
    for i in range(hight):
        for j in range(widht):
            for x in range(-offset, offset + 1):
                for y in range(-offset, offset + 1):
                    if (i + x >= 0 and i + x < hight) and (j + y >= 0 and j + y < widht):
                        new_image[i][j] += (image[i + x][j + y])/weight
    return np.uint8(new_image)

pcb_image = cv2.imread("Noisy PCB 455x440.tif", cv2.IMREAD_GRAYSCALE)
plt.subplot(1,4, 1)
plt.imshow(pcb_image, cmap='gray')
plt.title('PCB Image')

avg_filter_3x3 = avg_filter(pcb_image, 3)
plt.subplot(1,4, 2)
plt.imshow(avg_filter_3x3, cmap='gray')
plt.title(' 3x3' + str(PSNR(pcb_image, avg_filter_3x3)))

avg_filter_5x5 = avg_filter(pcb_image, 5)
plt.subplot(1,4, 3) 
plt.imshow(avg_filter_5x5, cmap='gray')
plt.title('5x5' + str(PSNR(pcb_image, avg_filter_5x5)))

avg_filter_7x7 = avg_filter(pcb_image, 7)
plt.subplot(1,4, 4)
plt.imshow(avg_filter_7x7, cmap='gray')
plt.title(' 7x7 ' + str(PSNR(pcb_image, avg_filter_7x7)))

plt.show()
