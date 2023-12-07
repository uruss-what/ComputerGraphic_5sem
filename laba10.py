import cv2
import numpy as np
from matplotlib import pyplot as plt


def ideal_lowpass_filter(img, cutoff_freq):
    fft = np.fft.fft2(img) # для дискретного преобразования фурье (из пикселей в частоты)
    shifted_fft = np.fft.fftshift(fft) # перемещает компоненты нулевой частоты из углов изображения в его центр
    
    rows, cols = img.shape 
    crow, ccol = rows//2, cols//2 # центр
    shifted_fft[crow-cutoff_freq:crow+cutoff_freq, ccol-cutoff_freq:ccol+cutoff_freq] = 0 # диапозон для удаления компонент высоких частот
    shifted_fft = np.fft.ifftshift(shifted_fft) # двигаем обратно
    filtered_img = np.fft.ifft2(shifted_fft) # возвращаем отфильтрованное изображение
    
    filtered_img = np.abs(filtered_img)
    filtered_img = filtered_img.astype(np.uint8)
    
    return filtered_img

def butterworth_filter(image, cutoff_freq, order, type='low'):
    rows, cols = image.shape[:2]
    img_center = (cols // 2, rows // 2)

    # Создаем частотный домен фильтра
    dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    # Создаем маску Баттерворта
    mask = np.zeros((rows, cols, 2), np.float32)
    
    for i in range(rows):
        for j in range(cols):
            dist = np.sqrt((i - img_center[1])**2 + (j - img_center[0])**2)
            if type == 'low':
                mask[i, j] = 1 / (1 + (dist / cutoff_freq)**(2 * order))
            elif type == 'high':
                mask[i, j] = 1 - 1 / (1 + (dist / cutoff_freq)**(2 * order))

    # Применяем фильтр
    dft_shift_filtered = dft_shift * mask
    dft_filtered = np.fft.ifftshift(dft_shift_filtered)
    filtered_image = cv2.idft(dft_filtered)
    filtered_image = cv2.magnitude(filtered_image[:, :, 0], filtered_image[:, :, 1])

    return filtered_image

def gaussian_lowpass_filter(img, cutoff_freq):
    filtered_img = cv2.GaussianBlur(img,(5, 5), cv2.BORDER_DEFAULT)
   
    return filtered_img

img = cv2.imread('kartinka.jpg', 0)

ideal_filtered_img = ideal_lowpass_filter(img, 10)

butterworth_filtered_img = butterworth_filter(img, cutoff_freq=50, order=2, type='low')

gaussian_filtered_img = gaussian_lowpass_filter(img, 10)


# Применение фильтра идеального сглаживания
smooth_image = cv2.blur(img, (30, 30))

# Визуализация исходного и обработанных изображений
plt.subplot(2,2,1), plt.imshow(img, cmap='gray')
plt.title('original image'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2), plt.imshow(smooth_image, cmap='gray')
plt.title('ideal filter'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3), plt.imshow(butterworth_filtered_img, cmap='gray')
plt.title('battervorth filter'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4), plt.imshow(gaussian_filtered_img, cmap='gray')
plt.title('gauss filter'), plt.xticks([]), plt.yticks([])

plt.show()
