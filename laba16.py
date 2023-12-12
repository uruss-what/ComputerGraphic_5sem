import numpy as np
import cv2

def lucy_richardson(image, kernel, iterations):
    # ������������� ������ ��������� �����������
    estimation = np.ones_like(image, dtype=np.float64)

    # ������������ ����
    normalized_kernel = kernel / np.sum(kernel)

    for _ in range(iterations):
        # ���������� ������ ��� ������� ������� ��������� �����������
        estimated_image = cv2.filter2D(estimation, -1, normalized_kernel)

        # ���������� ������ ������������ ��� ������� �������
        normalization = cv2.filter2D(image / estimated_image, -1, kernel)

        # ���������� ������ ��������� �����������
        estimation *= normalization

    return estimation

# �������� ��������� �����������
image = cv2.imread("kartinka.png", 0)

# �������� ���� (����� ������������ ���������������� ���� ��� ������� ����)
kernel = np.ones((5, 5), dtype=np.float64)

# ��������� ���������� ��������
iterations = 1000

# �������������� �����������
restored_image = lucy_richardson(image, kernel, iterations)

# ����� ���������������� �����������
cv2.imshow("Restored Image", restored_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
