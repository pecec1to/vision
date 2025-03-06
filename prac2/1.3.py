from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

img = Image.open('sea.png')

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(np.asarray(img))
plt.title("Imagen original")

angle = 10
sen = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))

escala_x, escala_y = 1.5, 1.5
transl_x, transl_y = 20, 30

T_rot = np.array([
	[cos, -sen, 0],
	[sen, cos, 0],
	[0, 0, 1]
])

T_escala = np.array([
	[escala_x, 0, 0],
	[0, escala_y, 0],
	[0, 0, 1]
])

T_transl = np.array([
	[1, 0, transl_x],
	[0, 1, transl_y],
	[0, 0, 1]
])

T = T_transl @ T_escala @ T_rot
T_inv = np.linalg.inv(T)

img_transformada = img.transform(img.size, Image.Transform.AFFINE, data=T_inv[:2, :].flatten(), resample=Image.NEAREST)

plt.subplot(1, 2, 2)
plt.imshow(np.asarray(img_transformada))
plt.title("Imagen transformada")
plt.axis("off")

plt.show()
