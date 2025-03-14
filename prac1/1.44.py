from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen TIFF
img = Image.open("A122.tif")
img = img.convert(mode='RGB')
img = img.convert(mode='P', palette=Image.Palette.ADAPTIVE, colors=256)
paleta = img.getpalette()
print('Colores en la paleta: ', len(paleta) / 3)
paleta = np.array(paleta)

fig, ax = plt.subplots(1, 1)
ax.imshow(img)

plt.show()
