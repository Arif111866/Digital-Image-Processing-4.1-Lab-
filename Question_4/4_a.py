import cv2
import numpy as np
import matplotlib.pyplot as plt


def butterworth_filter(image, cutoff_freq , order=2):
    hight = image.shape[0]
    width = image.shape[1]
    filter = np.zeros((hight, width), dtype= np.float32)
    for i in range(hight):
        for j in range(width):
            D = np.sqrt((i - hight / 2) ** 2 + (j - width / 2) ** 2)
            filter[i, j] = 1 / (1 + (D/ cutoff_freq)**(2*order))
    filter_image = image * filter
    filter_image = np.fft.ifft2(np.fft.ifftshift(filter_image))
    filter_image = np.abs(filter_image)
    return filter_image 

def gaussian_filter(image, cutoff_freq):
    hight = image.shape[0]
    width = image.shape[1]
    filter = np.zeros((hight, width), np.float32)
    for i in range(hight):
        for j in range(width):
            D = np.sqrt((i - hight / 2) ** 2 + (j - width / 2) ** 2)
            filter[i, j] = np.exp(-D**2/(2*(cutoff_freq**2)))
    
    filter_image = image * filter
    filter_image = np.fft.ifft2(np.fft.ifftshift(filter_image))
    filter_image = np.abs(filter_image)
    return np.uint8(filter_image)

image = cv2.imread('./Characters Test Pattern 688x688.tif', 0)
plt.subplot(1,5,1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

gaussion_noise = np.random.normal(7, 13 , image.shape).astype(np.uint8)
image = cv2.add(image, gaussion_noise)
plt.subplot(1,5,2)
plt.imshow(image, cmap='gray')
plt.title('Image with Gaussian Noise')

noisy_image_fft = np.fft.fftshift(np.fft.fft2(image))
plt.subplot(1,5,5)
plt.imshow(np.log(1 + np.abs(noisy_image_fft)), cmap='gray')
plt.title('FFT of Noisy Image')


gaussian_filtered_image = gaussian_filter(noisy_image_fft, 20)
plt.subplot(1,5,3)
plt.imshow(gaussian_filtered_image, cmap='gray')
plt.title('Gaussian Filtered Image')

butterworth_filtered_image = butterworth_filter(noisy_image_fft, 25, 2)
plt.subplot(1,5,4)
plt.imshow(butterworth_filtered_image, cmap='gray')
plt.title('Butterworth Filtered Image')
plt.show()
