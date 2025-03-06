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


def translate_image(image, tx=100, ty=50):
    ancho, alto = image.size  # Obtener dimensiones
    lienzo = Image.new("L", (ancho + tx, alto + ty), (255))  # Crear un lienzo más grande
    lienzo.paste(image, (tx, ty))  # Pegar la imagen en la nueva posición
    return lienzo

# Aplicar traslación
img_translated = translate_image(img, 100, 50)

def rotate_image(image, angle=30):
    return image.rotate(angle, resample=Image.BICUBIC, expand=True)

# Aplicar rotación
img_rotated = rotate_image(img, 30)

# Mostrar resultado
plt.figure(figsize=(6,6))
plt.imshow(img_rotated, cmap="gray")
plt.title("Imagen Rotada 30°")
plt.axis("off")
plt.show()


fig, axes = plt.subplots(1, 3, figsize=(18,6))

# Imagen original
axes[0].imshow(img, cmap="gray")
axes[0].set_title("Original")
axes[0].axis("off")

# Imagen trasladada
axes[1].imshow(img_translated, cmap="gray")
axes[1].set_title("Traslación (100,50)")
axes[1].axis("off")

# Imagen rotada
axes[2].imshow(img_rotated, cmap="gray")
axes[2].set_title("Rotación 30°")
axes[2].axis("off")

plt.show()
