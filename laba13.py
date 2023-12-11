import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('kartinka.png', cv2.IMREAD_GRAYSCALE)

# фильтр высоких частот гаусса
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])


sharpened = cv2.filter2D(image, -1, kernel)
# где kernel - выбранный фильтр (например, фильтр Шарра или фильтр Собеля)

# Применение эквализации гистограммы
hist_eq = cv2.equalizeHist(sharpened)

# Вывод изображений
plt.imshow(image, cmap='gray'), plt.title('Original')
plt.imshow(sharpened, cmap='gray'), plt.title('Sharpened')
plt.imshow(hist_eq, cmap='gray'), plt.title('Histogram Equalization')
plt.show()

