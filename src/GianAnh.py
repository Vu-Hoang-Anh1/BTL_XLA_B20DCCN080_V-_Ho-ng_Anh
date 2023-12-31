import cv2
import numpy as np
import matplotlib.pyplot as plt

def dilation_image(image_path, kernel_size=(3, 3)):
    # Read the grayscale image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Check if the image is valid
    if image is None:
        print("Unable to read the image.")
        return

    # Create a kernel for dilation
    kernel = np.ones(kernel_size, np.uint8)

    # Perform dilation
    dilated_image = cv2.dilate(image, kernel, iterations=1)

    # Display the results
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(dilated_image, cmap='gray')
    plt.title('Dilated Image')

    plt.show()

# Example usage
image_path =  'img/3087889034-1620532650.jpg'   # Change the path to your actual image
dilation_image(image_path)
