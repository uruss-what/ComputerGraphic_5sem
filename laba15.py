import numpy as np
import cv2
import scipy.signal as sps
import matplotlib.pyplot as plt

def inverse_filter(image, kernel):
    padded_kernel = np.pad(kernel, ((0, image.shape[0] - kernel.shape[0]), (0, image.shape[1] - kernel.shape[1])), 'constant')
    fft_kernel = np.fft.fft2(padded_kernel)
    fft_image = np.fft.fft2(image)
    fft_result = np.divide(fft_image, fft_kernel)
    result = np.fft.ifft2(fft_result)
    return np.abs(result)

def wiener_filter(image, kernel, noise_var):
    padded_kernel = np.pad(kernel, ((0, image.shape[0] - kernel.shape[0]), (0, image.shape[1] - kernel.shape[1])), 'constant')
    fft_kernel = np.fft.fft2(padded_kernel)
    fft_image = np.fft.fft2(image)
    kernel_power = np.abs(fft_kernel) ** 2
    wiener_factor = np.divide(kernel_power, kernel_power + noise_var)
    fft_result = np.divide(fft_image, fft_kernel) * wiener_factor
    result = np.fft.ifft2(fft_result)
    return np.abs(result)

def tikhonov_filter(image, kernel, regularization_param):
    padded_kernel = np.pad(kernel, ((0, image.shape[0] - kernel.shape[0]), (0, image.shape[1] - kernel.shape[1])), 'constant')
    fft_kernel = np.fft.fft2(padded_kernel)
    fft_image = np.fft.fft2(image)
    kernel_power = np.abs(fft_kernel) ** 2
    tikhonov_factor = np.divide(kernel_power, kernel_power + regularization_param)
    fft_result = np.divide(fft_image, fft_kernel) * tikhonov_factor
    result = np.fft.ifft2(fft_result)
    return np.abs(result)


image = cv2.imread('kartinka.png', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((11, 11))
blurred = sps.convolve2d(image, kernel, 'same')

noise = np.random.normal(0, 10, (image.shape[0],image.shape[1]))
noisy = blurred + noise

restored_inverse = inverse_filter(noisy, kernel)

restored_wiener = wiener_filter(noisy, kernel, np.var(noise))

regularization_param = 0.01
restored_tikhonov = tikhonov_filter(noisy, kernel, regularization_param)

# Отображаем результаты
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.title('Restored (Tikhonov)')
plt.imshow(restored_tikhonov, cmap='gray')
plt.subplot(2, 2, 2)
plt.title('Blurred + Noisy')
plt.imshow(noisy, cmap='gray')
plt.subplot(2, 2, 3)
plt.title('Restored (Inverse)')
plt.imshow(restored_inverse, cmap='gray')
plt.subplot(2, 2, 4)
plt.title('Restored (Wiener)')
plt.imshow(restored_wiener, cmap='gray')
plt.show()