import cv2
import numpy as np
from scipy import ndimage
from scipy.signal import butter, lfilter
from matplotlib import pyplot as plt
from PIL import Image, ImageFilter

def high_pass_ideal(image):
    rows, cols = image.shape

    # ѕреобразуем изображение в частотное пространство
    fft = np.fft.fftshift(np.fft.fft2(image))

    filter = np.zeros((rows, cols), np.uint8)
    center = (int(rows / 2), int(cols / 2))
    cv2.circle(filter, center, 80, 1, -1)
    filtered_image = fft * filter

    # ѕреобразуем изображение обратно в пространство пикселей
    result_image = np.abs(np.fft.ifft2(np.fft.ifftshift(filtered_image)))

    # Ќормализуем значени€ пикселей в диапазон 0-255
    result_image = cv2.normalize(result_image, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    return result_image


def butterworth_filter(image, cutoff, order):
   nyquist = 0.5 * np.pi
   normal_cutoff = cutoff / nyquist
   b, a = butter(order, normal_cutoff, btype='low', analog=False)
   y = lfilter(b, a, image)
   return y

def sharpen_image(image, cutoff=0.5, order=3):
   image = butterworth_filter(image, cutoff, order)
   image = image.astype(np.uint8)
   return image
    
def high_pass_gauss(image):
 kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
 im = cv2.filter2D(image, -1, kernel)

 return im


image = cv2.imread("kartinka.png", cv2.IMREAD_GRAYSCALE)


image_filtered_ideal = high_pass_ideal(image)

image_filtered_butterworth = sharpen_image(image)

image_filtered_gaussian = high_pass_gauss(image)

# ¬ыводим изображени€
plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(2, 2, 2), plt.imshow(image_filtered_ideal, cmap='gray'), plt.title('Ideal High Pass Filter')
plt.subplot(2, 2, 3), plt.imshow(image_filtered_butterworth, cmap='gray'), plt.title('Butterworth High Pass Filter')
plt.subplot(2, 2, 4), plt.imshow(image_filtered_gaussian, cmap='gray'), plt.title('Gaussian High Pass Filter')

plt.show()

