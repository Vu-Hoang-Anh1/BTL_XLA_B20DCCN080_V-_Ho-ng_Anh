import cv2

import numpy as np

import matplotlib.pyplot as plt

import cv2

import numpy as np

import matplotlib.pyplot as plt

input_image = cv2.imread('img/Screenshot 2023-11-28 013342.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow("ảnh gốc: ", input_image)
cv2.waitKey(5)

output_image = input_image.copy() 
[w, h] = output_image.shape[:2]

for i in range(w):
    for j in range(h):
        output_image[i][j] = 255 - output_image[i][j]


cv2.imshow('ảnh âm bản: ', output_image)
cv2.waitKey(0)