import cv2
import numpy as np
import matplotlib.pyplot as plt

# �������� ����������� (������ �� ����������� ������������)
image = cv2.imread('kartinka.jpg', cv2.IMREAD_GRAYSCALE)

# ���������� ����������� �������
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# ����������� ����������� �������
plt.plot(hist)
plt.xlabel('Pixel brightness')
plt.ylabel('Number of pixels')
plt.title('Brightness histogram')
plt.show()

# �������������� �����������
eq_image = cv2.equalizeHist(image)

# ����������� ����������� ����� �������������� �����������
cv2.imshow('equalization', np.hstack((image, eq_image)))
cv2.waitKey(0)
cv2.destroyAllWindows()

