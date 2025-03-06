import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('clahe_1.png', cv2.IMREAD_GRAYSCALE)

fig, axs = plt.subplots(2, 2, figsize=(15, 10))

axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].set_title('Imagen original (gris)')
axs[0, 0].axis('off')

hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])
clahe = cv2.createCLAHE(clipLimit=1, tileGridSize=(5,5))
img_clahe = clahe.apply(img)

axs[0, 1].plot(hist_original, color='black')
axs[0, 1].set_title('Histograma original')

axs[1, 0].imshow(img_clahe, cmap='gray')
axs[1, 0].set_title('Imagen CLAHE')
axs[1, 0].axis('off')

hist_clahe = cv2.calcHist([img_clahe], [0], None, [256], [0, 256])
axs[1, 1].plot(hist_clahe, color='black')
axs[1, 1].set_title('Histograma CLAHE')

plt.tight_layout()
plt.show()