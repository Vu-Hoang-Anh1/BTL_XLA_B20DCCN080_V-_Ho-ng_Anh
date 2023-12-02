import numpy as np 
import cv2 
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [10,8]
img = cv2.imread("img/Screenshot 2023-11-28 013342.png", 0)
# using cv2.calcHist()
def plot_img_and_hist(img):
    # Function to plot image and its histogram
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Image')

    plt.subplot(1, 2, 2)
    plt.hist(img.flatten(), bins=256, range=[0, 256], density=True, cumulative=True)
    plt.title('Histogram')

    plt.show()
hist = cv2.calcHist(
      [img],
      channels = [0],
      mask=None, # full image
      histSize=[256], #full scale
      ranges=[0,256]
)
plt.plot(hist)
plt.show()
def hist_equalize(img):
  # 1. calclate hist
  hist = cv2.calcHist([img], [0], None, [256], [0, 256])

  # 2. normalize hist
  h, w = img.shape[:2]
  hist = hist/(h*w)

  # 3. calculate CDF
  cdf = np.cumsum(hist)
  s_k = (255 * cdf - 0.5).astype("uint8")
  return s_k


s_k = hist_equalize(img)
equalized_img = cv2.LUT(img, s_k)
plot_img_and_hist(equalized_img)
