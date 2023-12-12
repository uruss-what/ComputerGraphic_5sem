import numpy as np
import cv2

def lucy_richardson(image, kernel, iterations):
    # Инициализация оценки исходного изображения
    estimation = np.ones_like(image, dtype=np.float64)

    # Нормализация ядра
    normalized_kernel = kernel / np.sum(kernel)

    for _ in range(iterations):
        # Вычисление оценки для каждого пикселя исходного изображения
        estimated_image = cv2.filter2D(estimation, -1, normalized_kernel)

        # Вычисление оценки нормализации для каждого пикселя
        normalization = cv2.filter2D(image / estimated_image, -1, kernel)

        # Обновление оценки исходного изображения
        estimation *= normalization

    return estimation

# Загрузка исходного изображения
image = cv2.imread("kartinka.png", 0)

# Загрузка ядра (можно использовать предопределенное ядро или создать свое)
kernel = np.ones((5, 5), dtype=np.float64)

# Установка количества итераций
iterations = 1000

# Восстановление изображения
restored_image = lucy_richardson(image, kernel, iterations)

# Вывод восстановленного изображения
cv2.imshow("Restored Image", restored_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
