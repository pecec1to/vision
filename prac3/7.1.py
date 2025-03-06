import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
img=cv2.imread("peppers.png", cv2.IMREAD_GRAYSCALE)
sx=cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sy=cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)


fig, axs = plt.subplots(1, 3)
axs[0].imshow(img, cmap="gray")
axs[0].set_title("Imagen original")
axs[0].axis("off")

axs[1].imshow(sx, cmap="gray")
axs[1].set_title("Sobel x")
axs[1].axis("off")

axs[2].imshow(sy, cmap="gray")
axs[2].set_title("Sobel y")
axs[2].axis("off")

plt.show()