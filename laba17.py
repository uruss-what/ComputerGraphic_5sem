import cv2
import numpy as np

def find_isolated_points(image):
    # ѕреобразуем изображение в градации серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # ѕримен€ем оператор свертки дл€ обнаружени€ изолированных точек
    kernel = np.array([[0, 1, 0],
                       [1, -4, 1],
                       [0, 1, 0]])
    filtered = cv2.filter2D(gray, -1, kernel)
    
    # ѕримен€ем пороговое значение дл€ получени€ бинарного изображени€
    _, binary = cv2.threshold(filtered, 1, 255, cv2.THRESH_BINARY)
    
    # Ќаходим контуры изолированных точек
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # ќтмечаем области, содержащие изолированные точки рамкой
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return image


image = cv2.imread('kartinka.png')

# ќбнаруживаем изолированные точки
result = find_isolated_points(image)


cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

