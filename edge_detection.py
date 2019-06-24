import numpy as np
from cv2 import cv2
from matplotlib import pyplot as plt
import sys

img = cv2.imread('./test_images/cropped2.png', 1)
img = cv2.GaussianBlur(img, (3, 3), 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

np_im = np.array(edges)
np.set_printoptions(threshold=np.inf)
print(edges)

plt.show()
