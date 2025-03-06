from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

img = Image.open('sea.png')

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.imshow(np.asarray(img))
plt.title('Imagen original')

# 2. Rotación de +10 grados
angle = 10
sen = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))

# Matriz de rotación
T_rotate = np.array([
    [cos, -sen, 0],
    [sen, cos, 0],
    [0, 0, 1]
])

# Matriz para centrar la imagen
T_center = np.array([
    [1, 0, -img.width/2],
    [0, 1, -img.height/2],
    [0, 0, 1]
])

# Matriz para devolver la imagen al origen
T_uncenter = np.array([
    [1, 0, img.width/2],
    [0, 1, img.height/2],
    [0, 0, 1]
])

# Concatenar transformaciones
T = T_uncenter @ T_rotate @ T_center

# Obtener la inversa para transform()
T_inv = np.linalg.inv(T)

# Aplicar transformación
img_rotated = img.transform(
    img.size,
    Image.Transform.AFFINE,
    data=T_inv.flatten()[:6],
    resample=Image.BILINEAR
)

# Mostrar resultado
plt.subplot(122)
plt.imshow(np.asarray(img_rotated))
plt.title('Rotación +10°')
plt.show()

