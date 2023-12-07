import cv2
import numpy as np


image = cv2.imread('kartinka.png')

laplacian1 = cv2.Laplacian(image, cv2.CV_64F, ksize=3)
laplacian2 = cv2.Laplacian(image, cv2.CV_64F, ksize=5)
laplacian3 = cv2.Laplacian(image, cv2.CV_64F, ksize=7) # чем больше матрица, тем меньше шума

# чем больше c, тем больше контрастность и резкость
c = 2 

enhanced_image1 = image + c * laplacian1
enhanced_image2 = image + c * laplacian2
enhanced_image3 = image + c * laplacian3


cv2.imshow("Original Image", image)
cv2.imshow("Enhanced Image with Laplacian 3x3", enhanced_image1)
cv2.imshow("Enhanced Image with Laplacian 5x5", enhanced_image2)
cv2.imshow("Enhanced Image with Laplacian 7x7", enhanced_image3)

cv2.waitKey(0)
cv2.destroyAllWindows()

