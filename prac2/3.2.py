import matplotlib.pyplot as plt
import numpy as np
import string
import math

# Definir puntos en coordenadas homogéneas
a, b, c, d = (0, 1, 1), (1, 0, 1), (0, -1, 1), (-1, 0, 1)
A = np.array([a, b, c, d])

# Definir matrices de transformación
# Matriz de traslación t=(-3, 3)
tx, ty = -3, 3
T_t = np.array([[1, 0, tx],
                [0, 1, ty],
                [0, 0, 1]])

# Matriz de rotación θ=30°
angle = 30
sen = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
T_r = np.array([[cos, -sen, 0],
                [sen, cos, 0],
                [0, 0, 1]])

# Combinar transformaciones: rotación seguida de traslación
T = T_t @ T_r

# Crear matriz identidad para comparación
I = np.eye(3)

# Definir colores para los puntos
color_lut = 'rgbc'

# Crear figura y eje
fig = plt.figure()
ax = plt.gca()

# Listas para almacenar las coordenadas x e y de los puntos originales y transformados
xs_s = []
ys_s = []

# Iterar sobre cada punto en A
i = 0
for row in A:
    # Coordenadas del punto original
    x, y, h = row

    # Aplicar transformación al punto
    output_row = T @ row
    x_s, y_s, k = output_row

    # Almacenar coordenadas transformadas
    xs_s.append(x_s)
    ys_s.append(y_s)

    # Obtener color correspondiente
    c = color_lut[i]

    # Dibujar el punto original y su etiqueta
    plt.scatter(x, y, color=c)
    plt.text(x + 0.15, y, f"{string.ascii_letters[int(i)]}")

    # Dibujar el punto transformado y su etiqueta
    plt.scatter(x_s, y_s, color=c)
    plt.text(x_s + 0.15, y_s, f"{string.ascii_letters[int(i)]}'")

    i += 1

# Cerrar el polígono con el primer punto
xs_s.append(xs_s[0])
ys_s.append(ys_s[0])

# Dibujar líneas punteadas entre los puntos originales y transformados
plt.plot(A[:, 0], A[:, 1], color="gray", linestyle='dotted')
plt.plot(xs_s, ys_s, color="gray", linestyle='dotted')

# Configurar ejes y cuadrícula
ax.set_xticks(np.arange(-10, 10, 1.0))
ax.set_yticks(np.arange(-10, 10, 1.0))
plt.grid()

# Mostrar gráfica
plt.show()