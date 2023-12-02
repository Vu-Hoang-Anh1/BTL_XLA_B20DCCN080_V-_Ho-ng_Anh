import cv2

import numpy as np

import matplotlib.pyplot as plt

def log_transform(input_image, c):

    output_image = c * np.log1p(input_image)

    return output_image



def power_transform(input_image, c, gamma):

    output_image = c * np.power(input_image, gamma)

    return output_image



input_image = cv2.imread('img/Screenshot 2023-11-28 004714.png', cv2.IMREAD_GRAYSCALE)



# Xử lý bằng biến đổi log

c1 = 1.0  # Hằng số c cho biến đổi log

log_transformed_image1 = log_transform(input_image, c1)



# Xử lý bằng biến đổi mẫu

c2 = 1.0  # Hằng số c cho biến đổi mẫu

gamma = 0.67  # Tham số gamma cho biến đổi mẫu

power_transformed_image = power_transform(log_transformed_image1, c2, gamma)



# Xử lý bằng biến đổi log lần nữa

c3 = 1.0  # Hằng số c cho biến đổi log lần nữa

log_transformed_image2 = log_transform(power_transformed_image, c3)



plt.imshow(log_transformed_image2, cmap='gray')

plt.show()

cv2.waitKey(0)

cv2.destroyAllWindows()