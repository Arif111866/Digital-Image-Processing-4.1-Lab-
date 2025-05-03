import cv2
import numpy as np
import matplotlib.pyplot as plt

def ideal_low_pass_filter(image , cutoff_freq):
    hight = image.shape[0]
    width = image.shape[1]
    filter = np.zeros((hight, width), dtype= np.float32)
    for i in range(hight):
        for j in range(width):
            D = np.sqrt((i - hight/2)**2 + (j - width/2)**2)
            if D <= cutoff_freq:
                filter[i, j] = 1
    filter_image = image * filter
    filter_image = np.fft.ifft2(np.fft.ifftshift(filter_image))
    filter_image = np.abs(filter_image)
    return filter_image

image = cv2.imread('./Characters Test Pattern 688x688.tif', 0)
plt.subplot(2,4,1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

gaussion_noise = np.random.normal(7, 13 , image.shape).astype(np.uint8)
image = cv2.add(image, gaussion_noise)
plt.subplot(2,4,2)
plt.imshow(image, cmap='gray')
plt.title('Image with Gaussian Noise')

noisy_image_fft = np.fft.fftshift(np.fft.fft2(image))
plt.subplot(2,4,3)
plt.imshow(np.log(1 + np.abs(noisy_image_fft)), cmap='gray')
plt.title('FFT of Noisy Image')

for i in range(5):
    cutoff_freq = 5 + i*5
    ideal_filtered_image = ideal_low_pass_filter(noisy_image_fft, cutoff_freq)
    plt.subplot(2,4,i+4)
    plt.imshow(ideal_filtered_image, cmap='gray')
    plt.title(f'Image (cutoff={cutoff_freq})')

plt.show()