import cv2
import os

def invert_image(image):
    inverted_image = cv2.bitwise_not(image)
    return inverted_image

def grayscale_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def rotate_image(image):
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return rotated_image

def crop_image(image, x, y, width, height):
    cropped_image = image[y:y+height, x:x+width]
    return cropped_image

def threshold_image(image, threshold):
    _, thresholded_image = cv2.threshold(image, threshold, 0, cv2.THRESH_TOZERO)
    return thresholded_image

def save_image(image, filename):
    cv2.imwrite(filename, image)

def show_image(image, title):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Загрузка изображения
filename = 'kartinka.jpg'
image = cv2.imread(filename)

# Показ и сохранение оригинального изображения
show_image(image, 'Original Image')
save_image(image, 'image_original.jpg')

# Инверсия цветов
inverted_image = invert_image(image)
show_image(inverted_image, 'Inverted Image')
save_image(inverted_image, 'image_inverted.jpg')

# Черно-белое изображение
gray_image = grayscale_image(image)
show_image(gray_image, 'Grayscale Image')
save_image(gray_image, 'image_grayscale.jpg')

# Поворот на 90 градусов против часовой стрелки
rotated_image = rotate_image(image)
show_image(rotated_image, 'Rotated Image')
save_image(rotated_image, 'image_rotated.jpg')

# Вырезание области
x, y, width, height = 100, 100, 700, 700
cropped_image = crop_image(image, x, y, width, height)
show_image(cropped_image, 'Cropped Image')
save_image(cropped_image, 'image_cropped.jpg')

# Обнуление пикселей, значение цвета которых меньше порогового
threshold = 128
thresholded_image = threshold_image(image, threshold)
show_image(thresholded_image, 'Thresholded Image')
save_image(thresholded_image, 'image_thresholded.jpg')
