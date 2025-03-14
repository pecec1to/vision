import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("cameraman.tif", cv2.IMREAD_GRAYSCALE)  # Cargar en escala de grises
img2 = cv2.imread("moon.tif", cv2.IMREAD_GRAYSCALE)      # Cargar en escala de grises

img1 = cv2.resize(img1, (256, 256))
img2 = cv2.resize(img2, (256, 256))

img_suma = cv2.add(img1, img2)

img_resta = cv2.subtract(img1, img2)

img_multiplicacion = cv2.multiply(img1, img2)

img_division = cv2.divide(img1, img2 + 1)  # +1 para evitar división por cero

fig, ax = plt.subplots(2, 2, figsize=(10, 10))

ax[0, 0].imshow(img_suma, cmap='gray')
ax[0, 0].set_title("Suma")
ax[0, 0].axis("off")

ax[0, 1].imshow(img_resta, cmap='gray')
ax[0, 1].set_title("Resta")
ax[0, 1].axis("off")

ax[1, 0].imshow(img_multiplicacion, cmap='gray')
ax[1, 0].set_title("Multiplicación")
ax[1, 0].axis("off")

ax[1, 1].imshow(img_division, cmap='gray')
ax[1, 1].set_title("División")
ax[1, 1].axis("off")

plt.tight_layout()
plt.show()