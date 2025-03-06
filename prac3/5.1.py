import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
src = np.array (Image.open('peppers.png'))
H = np.array([
[0,-1,-1],
[1, 0, -1],
[1, 1, 0] ])

dst = cv2.filter2D(src, -1, H)
fig, axs = plt.subplots(1, 2)
axs[0].imshow(src)
axs[0].set_title("Imagen original")
axs[0].axis("off")
axs[1].imshow(dst)
axs[1].set_title("Emboss filter")
axs[1].axis("off")
plt.show()