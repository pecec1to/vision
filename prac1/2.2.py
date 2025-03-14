from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("A122.tif")

img_gris = img.convert(mode='L')

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(img)
ax[0].set_title("Imagen original")
ax[0].axis("off")

ax[1].imshow(img_gris, cmap='gray')
ax[1].set_title("Imagen en escala de grises")
ax[1].axis("off")

plt.show()