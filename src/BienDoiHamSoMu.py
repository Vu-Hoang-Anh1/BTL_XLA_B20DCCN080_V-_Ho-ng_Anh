import cv2
import numpy as np
import matplotlib.pyplot as plt

def power_transform(input_image, c, gamma):
    output_image = c * np.power(input_image, gamma)
    return output_image

# Đọc ảnh đầu vào
input_image = cv2.imread('img/Screenshot 2023-11-28 023953.png', cv2.IMREAD_GRAYSCALE)

# Hằng số c cho biến đổi mũ
c = 1.0

# Tham số mũ gamma
gamma = 0.3

# Áp dụng biến đổi hàm số mũ
power_transformed_image = power_transform(input_image, c, gamma)

# Hiển thị ảnh gốc và ảnh sau khi biến đổi hàm số mũ
plt.subplot(1, 2, 1), plt.imshow(input_image, cmap='gray'), plt.title('Ảnh gốc')
plt.subplot(1, 2, 2), plt.imshow(power_transformed_image, cmap='gray'), plt.title('Ảnh sau biến đổi Hàm số mũ')
plt.show()
