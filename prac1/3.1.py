from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img1 = Image.open("cameraman.tif")
img2 = Image.open("moon.tif")

img1 = img1.resize((256, 256))
img2 = img2.resize((256, 256))

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(img1, cmap='gray')
ax[0].set_title("Cameraman")
ax[0].axis("off")

ax[1].imshow(img2, cmap='gray')
ax[1].set_title("Moon")
ax[1].axis("off")

plt.show()