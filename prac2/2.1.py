import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Función para generar un tablero de ajedrez
def checkboard(grid=10, square_size=20):
    print("Generando tablero de ajedrez...")

    # Crear una matriz de ceros (negro)
    x = np.zeros((grid, grid), dtype=np.uint8)

    # Llenar las casillas alternas con 255 (blanco)
    x[1::2, ::2] = 255
    x[::2, 1::2] = 255

    # Redimensionar la imagen para que cada cuadrado tenga el tamaño correcto
    img = Image.fromarray(x, mode="L")
    img_resized = img.resize((grid * square_size, grid * square_size), resample=Image.Resampling.NEAREST)

    return img_resized

# Crear la imagen de un tablero de 10x10 con cuadrados de 20x20 píxeles
img = checkboard(10, 20)

# Mostrar la imagen
plt.figure(figsize=(6, 6))
plt.imshow(img, cmap="gray")
plt.title("Tablero de Ajedrez 10x10")
plt.axis("off")
plt.show()

# Guardar la imagen
img.save("checkerboard.jpg")
