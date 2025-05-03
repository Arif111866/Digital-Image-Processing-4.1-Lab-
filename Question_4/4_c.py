import cv2
import numpy as np
import matplotlib.pyplot as plt

def ideal_high_pass_filter(image, cutoff_freq):
    hight = image.shape[0]
    width = image.shape[1]
    filter = np.zeros((hight, width), dtype=np.float32)
    for i in range(hight):
        for j in range(width):
            D = np.sqrt((i - hight / 2) ** 2 + (j - width / 2) ** 2)
            if D > cutoff_freq:
                filter[i, j] = 1
    filter_image = image * filter
    filter_image = np.fft.ifft2(np.fft.ifftshift(filter_image))
    filter_image = np.abs(filter_image)
    return filter_image

def gaussian_high_pass_filter(image, cutoff_freq):
    hight = image.shape[0]
    width = image.shape[1]
    filter = np.zeros((hight, width), np.float32)
    for i in range(hight):
        for j in range(width):
            D = np.sqrt((i - hight / 2) ** 2 + (j - width / 2) ** 2)
            filter[i, j] = 1 - np.exp(-D**2/(2*(cutoff_freq**2)))

    filter_image = image * filter
    filter_image = np.fft.ifft2(np.fft.ifftshift(filter_image))
    filter_image = np.abs(filter_image)
    return np.uint8(filter_image)

image = cv2.imread('./Characters Test Pattern 688x688.tif', 0)
plt.subplot(2, 5, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

image_fft = np.fft.fftshift(np.fft.fft2(image))
plt.subplot(2, 5, 6)
plt.imshow(np.log(1 + np.abs(image_fft)), cmap='gray')
plt.title('FFT of Original Image')

for i in range(4):
    cutoff_freq = 10 + i * 10
    ideal_filtered_image = ideal_high_pass_filter(image_fft, cutoff_freq)
    plt.subplot(2, 5, i + 2)
    plt.imshow(ideal_filtered_image, cmap='gray')
    plt.title(f'Ideal HPF (cutoff={cutoff_freq})')

for i in range(4):
    cutoff_freq = 10 + i * 10
    gaussian_filtered_image = gaussian_high_pass_filter(image_fft, cutoff_freq)
    plt.subplot(2, 5, i + 7)
    plt.imshow(gaussian_filtered_image, cmap='gray')
    plt.title(f'Gaussian HPF (cutoff={cutoff_freq})')

plt.show()