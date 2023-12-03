import cv2
import numpy as np

# ��������� �������� ����������� �� ������ ����������
def laplacian_sharpening(image):
    sharpened = cv2.Laplacian(image, cv2.CV_64F)
    sharpened = np.uint8(np.absolute(sharpened))
    return sharpened

# ���������� ��������� ������
def sobel_operator(image):
    gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    gradient = cv2.addWeighted(gradient_x, 0.5, gradient_y, 0.5, 0)
    return gradient

# ����������� � ������� ������������ ������� 5x5
def smoothing(image):
    kernel = np.ones((5, 5), np.float32) / 25
    smoothed = cv2.filter2D(image, -1, kernel)
    return smoothed

# �������������� �������������� �����������
def arithmetic_transform(image, alpha, beta):
    transformed = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return transformed

# ������������ ��������������
def gradient_transform(image):
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(grayscale, 128, 255, cv2.THRESH_BINARY)
    return thresholded

# �������� �����������
image = cv2.imread("kartinka.jpg")

# ��������� �������� �� ������ ����������
sharpened_image = laplacian_sharpening(image)

# ���������� ��������� ������
sobel_image = sobel_operator(image)

# ����������� � ������� ������������ ������� 5x5
smoothed_image = smoothing(image)

# �������������� ��������������
transformed_image = arithmetic_transform(image, 1.2, 30)

# ������������ ��������������
gradient_image = gradient_transform(image)

# ����� �����������
cv2.imshow("Original Image", image)
cv2.imshow("Sharpened Image", sharpened_image)
cv2.imshow("Sobel Image", sobel_image)
cv2.imshow("Smoothed Image", smoothed_image)
cv2.imshow("Transformed Image", transformed_image)
cv2.imshow("Gradient Image", gradient_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
