from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open("moon.tif").convert('L'))

x = np.arange(0, img.shape[1], 1)
y = np.arange(0, img.shape[0], 1)
x, y = np.meshgrid(x, y)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, img, cmap='viridis')

ax.set_title("Superficie 3D de la imagen")
plt.show()