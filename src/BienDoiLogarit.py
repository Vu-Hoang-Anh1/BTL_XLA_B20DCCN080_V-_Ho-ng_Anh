import cv2
import numpy as np
import matplotlib.pyplot as plt

def log_transform(input_image, c):
    output_image = c * np.log1p(input_image)
    return output_image

# Đọc ảnh đầu vào
input_image = cv2.imread('img/Screenshot 2023-11-28 023409.png', cv2.IMREAD_GRAYSCALE)

# Hằng số c cho biến đổi log
c = 1.0  

# Áp dụng biến đổi logarit
log_transformed_image = log_transform(input_image, c)

# Hiển thị ảnh gốc và ảnh sau khi biến đổi logarit
plt.subplot(1, 2, 1), plt.imshow(input_image, cmap='gray'), plt.title('Ảnh gốc')
plt.subplot(1, 2, 2), plt.imshow(log_transformed_image, cmap='gray'), plt.title('Ảnh sau biến đổi Log')
plt.show()
