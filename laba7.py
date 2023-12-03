import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, cauchy

def plot_histogram(image, title):
    colors = ('r', 'g', 'b')
    plt.figure()
    plt.title(title)

    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        normalized_histogram = histogram / histogram.sum()
        plt.plot(normalized_histogram, color=color, label='channel {}'.format(color))

    plt.legend()
    plt.xlim([0, 256])
    plt.show()

def normalize_histogram(image):
    normalized_image = np.zeros_like(image)

    for i in range(3):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        normalized_histogram = histogram / histogram.sum()
        cum_sum = np.cumsum(normalized_histogram)
        normalized_image[:, :, i] = np.interp(image[:, :, i], range(256), cum_sum * 255).astype(np.uint8)

    return normalized_image



# Загрузка изображения
image = cv2.imread('kartinka.jpg')

# Гистограмма изображения
plot_histogram(image, 'Original Histogram')

# Нормализованная гистограмма изображения
normalized_image = normalize_histogram(image)
plot_histogram(normalized_image, 'Normalized Histogram')

# Получаем значения каналов RGB
red_channel = image[:,:,0].flatten()
green_channel = image[:,:,1].flatten()
blue_channel = image[:,:,2].flatten()

# Создаем гистограммы для каждого канала
red_hist, red_bins, _ = plt.hist(red_channel, bins=256, range=(0, 256), color='red', alpha=0.5)
green_hist, green_bins, _ = plt.hist(green_channel, bins=256, range=(0, 256), color='green', alpha=0.5)
blue_hist, blue_bins, _ = plt.hist(blue_channel, bins=256, range=(0, 256), color='blue', alpha=0.5)

# Нормализуем гистограммы
red_hist /= np.sum(red_hist)
green_hist /= np.sum(green_hist)
blue_hist /= np.sum(blue_hist)

# Преобразуем гистограммы к экспоненциальному распределению
lambda_ = 1.0
red_hist_exp = expon.pdf(red_bins[:-1], scale=1.0/lambda_)
green_hist_exp = expon.pdf(green_bins[:-1], scale=1.0/lambda_)
blue_hist_exp = expon.pdf(blue_bins[:-1], scale=1.0/lambda_)

# Преобразуем гистограммы к распределению Коши
loc = 0.0
scale = 1.0
red_hist_cauchy = cauchy.pdf(red_bins[:-1], loc=loc, scale=scale)
green_hist_cauchy = cauchy.pdf(green_bins[:-1], loc=loc, scale=scale)
blue_hist_cauchy = cauchy.pdf(blue_bins[:-1], loc=loc, scale=scale)

# Строим графики
plt.figure(figsize=(10, 5))

plt.subplot(2, 3, 1)
plt.plot(red_bins[:-1], red_hist_cauchy)
plt.title('Red Channel')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

plt.subplot(2, 3, 2)
plt.plot(green_bins[:-1], green_hist_cauchy)
plt.title('Green Channel')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

plt.subplot(2, 3, 3)
plt.plot(blue_bins[:-1], blue_hist_cauchy)
plt.title('Blue Channel')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

plt.subplot(2, 3, 4)
plt.plot(red_bins[:-1], red_hist_exp)
plt.title('Red Channel - Exponential Distribution')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

plt.subplot(2, 3, 5)
plt.plot(green_bins[:-1], green_hist_exp)
plt.title('Green Channel - Exponential Distribution')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

plt.subplot(2, 3, 6)
plt.plot(blue_bins[:-1], blue_hist_exp)
plt.title('Blue Channel - Exponential Distribution')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

