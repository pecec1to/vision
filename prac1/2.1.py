from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("A122.tif")

img_rotada = img.rotate(45)

img_flip = img.transpose(Image.FLIP_TOP_BOTTOM)

fig, ax = plt.subplots(1, 3, figsize=(10,5))

ax[0].imshow(img)
ax[0].set_title("Imagen original")
ax[0].axis("off")

ax[1].imshow(img_rotada)
ax[1].set_title("Imagen rotada 45 grados")
ax[1].axis("off")

ax[2].imshow(img_flip)
ax[2].set_title("Imagen invertida")
ax[2].axis("off")
plt.show()