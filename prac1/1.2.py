from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("corn.TIF")

img_paleta = img.convert("P")

paleta = []
for i in range(256):
    paleta.extend((i, i, i))

img_paleta.putpalette(paleta)
col_paleta=np.unique(np.array(img_paleta))
n_col=len(col_paleta)
print(f"La imagen tiene {n_col} colores")

fig, ax = plt.subplots(1,2)
ax[0].imshow(img)
ax[1].imshow(img_paleta)

plt.show()




