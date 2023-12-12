import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('kartinka.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применение преобразования Хафа
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=100, maxLineGap=10)

# Визуализация шагов преобразования Хафа
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB))
plt.title('Canny')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('HoughLinesP')

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB))
plt.title('step 1:Canny')

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('step 2:HoughLinesP')

plt.tight_layout()
plt.show()

