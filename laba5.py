import cv2
import numpy as np

def piecewise_linear_transform(image, breakpoints):
    breakpoints.sort(key=lambda x: x[0])  # Сортировка по значению яркости
    new_image = np.copy(image)
    
    for i in range(len(breakpoints)-1):
        x_start, y_start = breakpoints[i] # точка перелома
        x_end, y_end = breakpoints[i+1] #точка перелома +1
        slope = (y_end - y_start) / (x_end - x_start) # наклон прямой 
        intercept = y_start - slope * x_start # точка через которую проходит прямая
        mask = np.logical_and(image >= x_start, image < x_end)
        new_image[mask] = slope * image[mask] + intercept
    
    return new_image



img = cv2.imread('kartinka.jpg')
print("Image data type:", img.dtype)

_, thresholded = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

c = 255 / np.log1p(np.max(img))
log_transformed = c* np.log1p(img)

gamma = 0.5
gamma_transformed = np.power(img / 255.0, gamma) * 255.0

breakpoints = [(0, 0), (128, 64), (255, 255)]
piecewise_image = piecewise_linear_transform(img, breakpoints)

cv2.imshow('Original', img)
cv2.imshow('Thresholded', thresholded)
cv2.imshow('Log-Transformed', np.uint8(log_transformed))
cv2.imshow('Gamma-Transformed', np.uint8(gamma_transformed))
cv2.imshow('Piecewise-Transformed', np.uint8(piecewise_image))
cv2.waitKey(0)
cv2.destroyAllWindows()

