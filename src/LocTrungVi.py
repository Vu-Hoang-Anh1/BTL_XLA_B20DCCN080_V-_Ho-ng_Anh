import cv2
import numpy as np
from matplotlib import pyplot as plt

def median_filter(image, kernel_size):
    # Áp dụng bộ lọc trung vị
    filtered_image = cv2.medianBlur(image, kernel_size)
    return filtered_image

# Đọc ảnh từ đường dẫn
image = cv2.imread('img/Screenshot 2023-11-28 004714.png', cv2.IMREAD_GRAYSCALE)

# Áp dụng bộ lọc trung bình
blur_average = cv2.blur(image, (3, 3))

# Áp dụng bộ lọc trung vị
kernel_size_median = 3  # Kích thước của kernel cho bộ lọc trung vị
blur_median = median_filter(image, kernel_size_median)

# Chuyển đổi sang định dạng RGB để hiển thị bằng matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
blur_average_rgb = cv2.cvtColor(blur_average, cv2.COLOR_BGR2RGB)
blur_median_rgb = cv2.cvtColor(blur_median, cv2.COLOR_BGR2RGB)

# Hiển thị ảnh gốc và ảnh sau khi áp dụng bộ lọc trung bình và bộ lọc trung vị
plt.subplot(131), plt.imshow(image_rgb), plt.title('Ảnh gốc')
plt.xticks([]), plt.yticks([])

plt.subplot(132), plt.imshow(blur_average_rgb), plt.title('Ảnh sau lọc trung bình')
plt.xticks([]), plt.yticks([])

plt.subplot(133), plt.imshow(blur_median_rgb), plt.title('Ảnh sau lọc trung vị')
plt.xticks([]), plt.yticks([])

plt.show()
