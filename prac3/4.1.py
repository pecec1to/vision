from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2
def imadjust(img, low_in, high_in):
    min_val = low_in
    max_val = high_in
    # Calcular imagen ajustada
    img_out = np.round(255.0 * (img - min_val) / (max_val - min_val + 1))
    # Convertir a uint8 y asegurar límites
    img_out = img_out.astype(np.uint8)
    img_out[img < min_val] = 0
    img_out[img > max_val] = 255
    return img_out

def imadjustLUT (img, low_in, high_in, *args):
    if isinstance(args, np.ndarray):
        LUT = args
    else:
        min = low_in
        max = high_in
        # Make a LUT (Look-Up Table) to translate image values
        LUT = np.zeros(256,dtype=np.uint8)
        LUT[max+1:] = 255
        LUT[min:max+1] = np.linspace(start=0,stop=255,num=(max-min)+1,endpoint=True, dtype= np.uint8)
    # Apply LUT and save resulting image
    img_out = LUT[img]
    return img_out

# Función mejorada con recorte automático del 1%
def imadjust_auto(img):
    # Calcular histograma
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist = hist.flatten() / hist.sum()  # Normalizar a probabilidad

    # Calcular CDF (Cumulative Distribution Function)
    cdf = hist.cumsum()

    # Encontrar los valores para recortar el 1% por arriba y por abajo
    low_in = np.argmax(cdf >= 0.01)
    high_in = np.argmax(cdf >= 0.99)

    # Ajustar la imagen
    return imadjust(img, low_in, high_in), low_in, high_in


img = cv2.imread('peppers.png')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#img_adj = imadjustLUT(img_rgb, 100, 200)
fig, axs = plt.subplots(1, 2, figsize=(12,4)) # Dos subplots en horizontal
axs[0].imshow(img_rgb, vmin=0, vmax=255)
nonlinear_lut = np.zeros(256, dtype=np.uint8)
for i in range(256):
    if i <= 100:
        nonlinear_lut[i] = 0
    elif i >= 200:
        nonlinear_lut[i] = 255
    else:
        # Función cuadrática en lugar de lineal
        x = (i - 100) / (200 - 100)
        y = x * x
        nonlinear_lut[i] = int(255 * y)

img_auto, low_auto, high_auto = imadjust_auto(img_rgb)
axs[1].imshow(img_auto, cmap='gray')
axs[1].set_title(f'Ajuste auto (1%) [{low_auto}, {high_auto}]')
axs[1].axis('off')
plt.show()