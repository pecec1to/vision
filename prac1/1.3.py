from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = Image.open("A122.tif")

paleta=img.getpalette()

imgRGB=img.convert(mode='RGB')
img_reducida = imgRGB.convert(mode='P', palette=Image.Palette.ADAPTIVE, colors=16)
paleta_reducida=img_reducida.getpalette()
print('Número de colores reducidos en la paleta: ', len(paleta_reducida)/3)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))

ax[0].imshow(img)
ax[0].set_title("Imagen Original")
ax[0].axis("off")

ax[1].imshow(img_reducida)
ax[1].set_title("Imagen Reducida a 16 Colores")
ax[1].axis("off")

plt.show()



