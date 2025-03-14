from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("aloel.jpg")
img_array = np.array(img)

r, g, b = img.split()

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

ax[0].imshow(r, cmap="gray")
ax[0].set_title("Componente rojo")
ax[0].axis("off")

ax[1].imshow(g, cmap="gray")
ax[1].set_title("Componente verde")
ax[1].axis("off")

ax[2].imshow(b, cmap="gray")
ax[2].set_title("Componente azul")
ax[2].axis("off")

plt.show()
