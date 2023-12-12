import numpy as np
import cv2

def main():
    image = cv2.imread("kartinka.png", cv2.IMREAD_GRAYSCALE)

    # ���������� ������� ������
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.sqrt(np.square(sobelx) + np.square(sobely))

    # ���������� ������� ��������
    gradient_x = cv2.convertScaleAbs(cv2.Scharr(image, cv2.CV_64F, 1, 0))
    gradient_y = cv2.convertScaleAbs(cv2.Scharr(image, cv2.CV_64F, 0, 1))
    prewitt = cv2.addWeighted(gradient_x, 0.5, gradient_y, 0.5, 0)

    # ���������� ������� ����������
    laplacian = cv2.Laplacian(image, cv2.CV_64F)

    # ���������� ������� ���������
    gaussian = cv2.GaussianBlur(image, (3, 3), 0)

    # ���������� ������� �����
    edges = cv2.Canny(image, 100, 200)

    # ����������� �����������
    cv2.imshow("Original Image", image)
    cv2.imshow("Sobel", sobel)
    cv2.imshow("Prewitt", prewitt)
    cv2.imshow("Laplacian", laplacian)
    cv2.imshow("Gaussian", gaussian)
    cv2.imshow("Canny", edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

