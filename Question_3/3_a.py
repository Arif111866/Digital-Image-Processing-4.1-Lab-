import cv2
import numpy as np
import matplotlib.pyplot as plt

def PSNR(image, noise_image):
    mse = np.mean((image - noise_image)** 2)
    if mse == 0:
        return "infinity"
    max_pixel = 255.0
    psnr = 10 * np.log10((max_pixel**2) / mse)
    return psnr

def add_salt_peeper(image, persentage):
    new_image = image.copy()
    total_pixels = image.shape[0] * image.shape[1]
    salt_pixels = int(total_pixels * persentage / 100)
    for _ in range(salt_pixels):
        x = np.random.randint(0, image.shape[0])
        y = np.random.randint(0, image.shape[1])
        x1 = np.random.randint(0, image.shape[0])
        y1 = np.random.randint(0, image.shape[1])
        new_image[x][y] = 0
        new_image[x][y] = 255
    return np.uint8(new_image)

image = cv2.imread("Characters Test Pattern 688x688.tif", cv2.IMREAD_GRAYSCALE)
plt.subplot(2,3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

noise_image = add_salt_peeper(image, 40)
plt.subplot(2,3, 2)
plt.imshow(noise_image, cmap='gray')
plt.title('Salt and Pepper Noise' + str(PSNR(image, noise_image)))

pcb_image = cv2.imread("Noisy PCB 455x440.tif", cv2.IMREAD_GRAYSCALE)
plt.subplot(2,3, 3)
plt.imshow(pcb_image, cmap='gray')
plt.title('PCB Image with noise')

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

avg_image = avg_filter(pcb_image, 5)
plt.subplot(2,3, 4)
plt.imshow(avg_image, cmap='gray')
plt.title('Average Filtered Image' + str(PSNR(pcb_image, avg_image)))


def median_filter(image, kernel_size):
    hight = image.shape[0]
    widht = image.shape[1]
    offset = kernel_size // 2
    new_image = image.copy()
    for i in range(hight):
        for j in range(widht):
            values = []
            for x in range(-offset, offset + 1):
                for y in range(-offset, offset + 1):
                    if (i + x >= 0 and i + x < hight) and (j + y >= 0 and j + y < widht):
                        values.append(image[i + x][j + y])
            new_image[i][j] = np.median(values)
    return np.uint8(new_image)

median_image = median_filter(pcb_image, 5)
plt.subplot(2,3, 5)
plt.imshow(median_image, cmap='gray')
plt.title('Median Filtered Image' + str(PSNR(pcb_image , median_image)))

plt.show()