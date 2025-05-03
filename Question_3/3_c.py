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

def harmonic_mean_filter(image, karnel_size):
    hight = image.shape[0]
    widht = image.shape[1]
    new_image = image.copy()
    offset = karnel_size//2
    for i in range(hight):
        for j in range(widht):
            sum = 0
            for x in range(-offset, offset + 1):
                for y in range(-offset, offset + 1):
                    if (i + x >= 0 and i + x < hight) and (j + y >= 0 and j + y < widht):
                        if(image[i+x][j+y]):
                            sum += float(1/image[i+x][j+y])
            if(sum):
                new_image[i][j] = min(255, (karnel_size*karnel_size/sum))
            else:
                new_image[i][j] = 0
    return np.uint8(new_image)

def geometric_mean_filter(image, karnel_size):
    hight = image.shape[0]
    widht = image.shape[1]
    new_image = image.copy()
    offset = karnel_size//2
    for i in range(hight):
        for j in range(widht):
            product = 1
            count = 0
            for x in range(-offset, offset + 1):
                for y in range(-offset, offset + 1):
                    if (i + x >= 0 and i + x < hight) and (j + y >= 0 and j + y < widht):
                        if(image[i+x][j+y]):
                            product *= int(image[i+x][j+y])
                            count += 1
            count = max(count, 1)
            new_image[i][j] = int(product**(1/count))
    return np.uint8(new_image)

image = cv2.imread("Noisy PCB 455x440.tif", cv2.IMREAD_GRAYSCALE)
plt.subplot(1,4, 1)
plt.imshow(image, cmap='gray')
plt.title('PCB Image')

harmonic_image = harmonic_mean_filter(image, 3)
plt.subplot(1,4, 2)
plt.imshow(harmonic_image, cmap='gray')
plt.title('Harmonic image -' + str(PSNR(image, harmonic_image)))


geometric_image = geometric_mean_filter(image, 3)
plt.subplot(1,4, 3)
plt.imshow(geometric_image, cmap='gray')
plt.title('Geometric image -' + str(PSNR(image, geometric_image)))

plt.show()