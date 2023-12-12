import cv2
import numpy as np

def find_isolated_points(image):
    # ����������� ����������� � �������� ������
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # ��������� �������� ������� ��� ����������� ������������� �����
    kernel = np.array([[0, 1, 0],
                       [1, -4, 1],
                       [0, 1, 0]])
    filtered = cv2.filter2D(gray, -1, kernel)
    
    # ��������� ��������� �������� ��� ��������� ��������� �����������
    _, binary = cv2.threshold(filtered, 1, 255, cv2.THRESH_BINARY)
    
    # ������� ������� ������������� �����
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # �������� �������, ���������� ������������� ����� ������
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return image


image = cv2.imread('kartinka.png')

# ������������ ������������� �����
result = find_isolated_points(image)


cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

