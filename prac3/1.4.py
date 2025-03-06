import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
img = np.asarray(Image.open('peppers.png'))
hr, edges_r = np.histogram(img[:,:,0],16)
hg, edges_g = np.histogram(img[:, :, 1], bins=16)
hb, edges_b = np.histogram(img[:, :, 2], bins=16)
fig, axs = plt.subplots(1, 2, figsize=(12,4)) # Dos subplots en horizontal
axs[1].stairs(hr, edges_r, label='Red histogram', ec='r')
axs[1].stairs(hg, edges_g, label='Green histogram', ec='g', hatch='||')
axs[1].stairs(hb, edges_b, label='Blue histogram', ec='b', hatch='||')
axs[1].set_title("Step Histograms")
axs[1].legend()
plt.sca(axs[0]) # Para poner en el subplot izquierdo la imagen
plt.imshow(img)
plt.show()