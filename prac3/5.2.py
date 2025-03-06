import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
src = np.array (Image.open('peppers.png'))
H = np.array([
    [0,-1,-1],
    [1, 0, -1],
    [1, 1, 0] ])
E2 = np.array([
    [-2,-1,0],
    [-1, 1, 1],
    [0, 1, 2] ])
S = np.array([
    [0,-1,0],
    [-1, 5, -1],
    [0, -1, 0] ])

B = np.array([
    [1/9,1/9,1/9],
    [1/9,1/9,1/9],
    [1/9, 1/9,1/9] ])

ED = np.array([
    [-1,-1,-1],
    [-1, 8, -1],
    [-1, -1, -1] ])

Sepia = np.array([
    [0.272, 0.534, 0.1311],
    [0.349, 0.686, 0.168],
    [0.393, 0.769, 0.189] ])

dst = cv2.filter2D(src, -1, H)
imge2 = cv2.filter2D(src, -1, E2)
imgs = cv2.filter2D(src, -1, S)
imgb = cv2.filter2D(src, -1, B)
imged = cv2.filter2D(src, -1, ED)
imgsepia = cv2.filter2D(src, -1, Sepia)

fig, axs = plt.subplots(2, 3)
axs[0,0].imshow(src)
axs[0,0].set_title("Imagen original")
axs[0,0].axis("off")

axs[0,1].imshow(dst)
axs[0,1].set_title("Emboss filter")
axs[0,1].axis("off")

axs[0,2].imshow(imge2)
axs[0,2].set_title("Realce 2")
axs[0,2].axis("off")

axs[1,0].imshow(imgs)
axs[1,0].set_title("Agudizado")
axs[1,0].axis("off")

axs[1,1].imshow(imgb)
axs[1,1].set_title("Suavizado")
axs[1,1].axis("off")

axs[1,2].imshow(imgsepia)
axs[1,2].set_title("Sepia")
axs[1,2].axis("off")

plt.show()