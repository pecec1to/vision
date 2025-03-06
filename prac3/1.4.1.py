from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2
img = cv2.imread('peppers.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hb = cv2.calcHist([img], [0], None, [256], [0, 256])
hg = cv2.calcHist([img], [1], None, [256], [0, 256])
hr = cv2.calcHist([img], [2], None, [256], [0, 256])
fig, axs = plt.subplots(1, 2, figsize=(12,4)) # Dos subplots en horizontal
axs[1].plot(hr, color='r')
axs[1].plot(hg, color='g')
axs[1].plot(hb, color='b')
axs[1].set_title("Step Histograms")
axs[1].legend()
plt.sca(axs[0]) # Para poner en el subplot izquierdo la imagen
plt.imshow(img_rgb)
plt.show()