import cv2
import numpy as np
import matplotlib.pyplot as plt

# Загрузка изображения (пример на монохромных изображениях)
image = cv2.imread('kartinka.jpg', cv2.IMREAD_GRAYSCALE)

# Построение гистограммы яркости
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# Отображение гистограммы яркости
plt.plot(hist)
plt.xlabel('Pixel brightness')
plt.ylabel('Number of pixels')
plt.title('Brightness histogram')
plt.show()

# Преобразование эквализации
eq_image = cv2.equalizeHist(image)

# Отображение изображения после преобразования эквализации
cv2.imshow('equalization', np.hstack((image, eq_image)))
cv2.waitKey(0)
cv2.destroyAllWindows()

