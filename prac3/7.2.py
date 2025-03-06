import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
img=cv2.imread("peppers.png", cv2.IMREAD_GRAYSCALE)

gaussian = cv2.GaussianBlur(img, (5, 5), 0)

log = cv2.Laplacian(gaussian, cv2.CV_64F, ksize=3)


fig, axs = plt.subplots(1, 2)
axs[0].imshow(img, cmap="gray")
axs[0].set_title("Imagen original")
axs[0].axis("off")

# axs[1].imshow(gaussian, cmap="gray")
# axs[1].set_title("Sobel x")
# axs[1].axis("off")

axs[1].imshow(log, cmap="gray")
axs[1].set_title("LoG")
axs[1].axis("off")

plt.show()