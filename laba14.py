import numpy as np
import cv2
import matplotlib.pyplot as plt

def add_noise(image, noise_level): #гауссовский шум
        noisy_image = np.copy(image)
        mean = 0
        std_dev = np.sqrt(noise_level)
        noise = np.random.normal(mean, std_dev, image.shape).astype(np.uint8)
        noisy_image = cv2.add(image, noise)
        return noisy_image

def restore_image(image, restoration_type):
    restored_image = np.copy(image)
    if restoration_type == 'blur':
        restored_image = cv2.GaussianBlur(restored_image, (5, 5), 0)
    elif restoration_type == 'median':
        restored_image = cv2.medianBlur(restored_image, 5)
    elif restoration_type == 'bilateral':
        restored_image = cv2.bilateralFilter(restored_image, 9, 75, 75)
    return restored_image

def compare_images(original_image, restored_image):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    axes[1].imshow(cv2.cvtColor(restored_image, cv2.COLOR_BGR2RGB))
    axes[1].set_title('Restored Image')
    axes[1].axis('off')
    plt.show()
    
original_image = cv2.imread('kartinka.png')

noise_level = 2
noisy_image = add_noise(original_image, noise_level)

restoration_type = 'bilateral'
restored_image = restore_image(noisy_image, restoration_type)

compare_images(original_image, restored_image)