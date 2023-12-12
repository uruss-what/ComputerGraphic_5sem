import cv2

image = cv2.imread('kartinka.png')

# �������������� ����������� � ������� ������
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# ���������� ������ ��� � �������������� ������� graythresh
_, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

