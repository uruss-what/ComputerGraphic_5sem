import cv2
import numpy as np

def main():
    filename = 'image.png'
    image = cv2.imread(filename)

    print("Type:",type(image))
    print("Shape of Image:", image.shape)
    print('Total Number of pixels:', image.size)
    print("Image data type:", image.dtype)
    # print("Pixel Values:\n", img)
    print("Dimension:", image.ndim)

    cv2.imshow('Image', image)
    cv2.waitKey(0)

    retval, threshold = cv2.threshold(image, 62, 255, cv2.THRESH_BINARY)

    cv2.imshow('Diff Mask', threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

