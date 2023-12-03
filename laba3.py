import cv2
import numpy as np
import statistics
import matplotlib.pyplot as plt


def main():
    filename = 'image.png'
    image = cv2.imread(filename)
    #m,n = 10, 10
    #image = np.random.randint(low=0, high=255, size=(m, n))

    print("Type:",type(image))
    print("Shape of Image:", image.shape)
    print('Total Number of pixels:', image.size)
    print("Image data type:", image.dtype)
    # print("Pixel Values:\n", img)
    print("Dimension:", image.ndim)

    cv2.imshow('Image', image)
    cv2.waitKey(0)

    mean_img = np.zeros_like(image, dtype=np.float32)
    g_sum = np.zeros_like(image, dtype=np.float32)

    num_images = 10
    K = 100
    distorted_images = []

    for i in range(K):
      
      noise = np.random.normal(0, 255, image.shape)
      
      img_noised = image + noise
    
      g_sum += img_noised
      
      distorted_images.append(img_noised)
    
    
    #average_image = np.mean(distorted_images, axis=0)
    average_image= np.mean(distorted_images, axis=0)
    average_variance = np.var(average_image) 

    noise_variance = np.var(noise) 

    #assert average_variance == noise_variance / K

    print(f"Distorted Image Variance: {average_variance}")
    print(f"Noise dispersion: {noise_variance}")
    print(f"Variance ratio = K =: {average_variance/noise_variance}")


    cv2.imshow('Diff Mask', img_noised)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    cv2.imshow('M (Diff Mask)',average_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    

if __name__ == '__main__':
    main()
