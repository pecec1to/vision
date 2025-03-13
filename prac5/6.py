# segmentat_imagen.py
#
# Programa pasa realizar operaciones de umbrallización global con imágenes de niveles de gris y extracción de las cartas
# de la imagen
#
# Autor: José M Valiente    Fecha: marzo 2023
#
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import cv2
from tkinter import filedialog
import os
import random as rng

class Card:
    # Suits. Palos de las cartas de póker
    DIAMONDS = 'Diamonds' # Rombos
    SPADES = 'Spades' # Picas
    HEARDS = 'Hearts' # Corazones
    CLUBS ='Clubs' # Tréboles
    # Figuras y cifras de las cartas de póker
    FIGURES = ('0','A','2','3','4','5','6','7','8','9','J','Q','K') # Se accede mediantge Carta.FIGURES[i]
    def __init__(self): # Constructor
        self.cardId = 0
        self.realSuit = ''
        self.realFigure = ''
        self.predictedSuit = ''
        self.predictedFigure = ''
        bboxType = [('x', np.intc),('y',np.intc),('width',np.intc),('height',np.intc)]
        self.boundingBox = np.zeros(1, dtype=bboxType).view(np.recarray)
        self.angle = 0.0
        self.grayImage = np.empty([0,0], dtype=np.uint8)
        self.colorImage = np.empty([0,0,0], dtype=np.uint8)
    def __repr__(self): # Para imprimir el contenido
        rep = f"Card number: {str(self.cardId)} -- Real Suit/Figure: {self.realSuit} / {self.realFigure} -- Predicted Suit/Fifure: {self.predictedSuit} / {self.predictedFigure}"
        bb = f"Bounding Box: {str(self.boundingBox)} Rect angle: {str(self.angle)}"
        ims = f"Gray image: {str(self.grayImage.shape)} Color image: {str(self.colorImage.shape)}"
        new_line = "\n"
        return rep + new_line + bb + new_line + ims

window_original = 'Original_image'
window_threshold = 'Thresholded_image'
window_roi = 'ROI image'
window_roi_color = 'ROI color image'
cv2.namedWindow(window_original, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow(window_threshold, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow(window_roi, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)
cv2.namedWindow(window_roi_color, cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO | cv2.WINDOW_GUI_EXPANDED)

low_H = 155

def label2rgb(label_img):
    # Función para conversión de etiquetas a colores
    label_hue = np.uint8(179 * (label_img) / np.max(label_img))
    blank_ch = 255 * np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
    # Converting cvt to BGR
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
    # set bg label to black
    labeled_img[label_ids == 0] = 0
    return labeled_img

# Hacemos una lista vacía de cartas 'Cards' para ir añadiendo items mediante Cards.append(Card)
Cards = []
icard = 0

# Selección de una carpeta mediante un diálogo de la biblioteca 'tkinter'
folders = '../VxC FOTOS'  # Poner la ruta de la carpeta de cartas de póker
path = filedialog.askdirectory(initialdir=folders, title="Seleccione una carpeta")

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if not (name.endswith('.jpg')):
            continue
        filename = os.path.join(root, name)
        img = cv2.imread(filename)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow(window_original, img)
        fret, thresh1 = cv2.threshold(img_gray, low_H, 255, cv2.THRESH_BINARY_INV)
        (totalLabels, label_ids, values, centroid) = cv2.connectedComponentsWithStats(thresh1, 4, cv2.CV_32S)

        output = np.zeros(img_gray.shape, dtype="uint8")
        # Bucle para cada objeto 'i'
        for i in range(1, totalLabels):
            # Área del objeeto
            area = values[i, cv2.CC_STAT_AREA]

            if (area > 300000):  # Filtro de tamaño   NUEVA CARTA
                componentMask = (label_ids == i).astype("uint8") * 255
                output = cv2.bitwise_or(output, componentMask)
                print(area)
                # A completar: Contornos del objeto ‘i’ con área mayor que el mínimo indicado
                contours, jerarquia = cv2.findContours(output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                # Bounding box del objeto ‘i’
                x1 = values[i, cv2.CC_STAT_LEFT]
                y1 = values[i, cv2.CC_STAT_TOP]
                w = values[i, cv2.CC_STAT_WIDTH]
                h = values[i, cv2.CC_STAT_HEIGHT]
                roi = img_gray[int(y1):int(y1 + h), int(x1):int(x1 + w)].copy()  # ROI de la imagen de gris del objeto
                rows, cols = roi.shape[:2]

                roi_color = img[int(y1):int(y1 + h), int(x1):int(x1 + w)].copy()

                # Crear y apuntar los datos de la carta
                c = Card()
                c.cardId = icard
                c.boundingBox[0] = (x1, y1, w, h)
                c.grayImage = roi
                c.colorImage = roi_color

                # Añadir la carta a la lista de cartas
                Cards.append(c)
                icard+=1

        print('\n')
        key = -1
        while (key == -1):
            key = cv2.pollKey()
            # Aquí va la función  cv2.inRange(....)
            cv2.imshow(window_original, img)  # , cmap='gray')
            cv2.imshow(window_roi, roi)
            cv2.imshow(window_roi_color, roi_color)
            cv2.imshow(window_threshold, output)  # , cmap='gray')

        if key == ord('q') or key == 27:  # 'q' o ESC para acabar
            break

# Guardar las cartas en una archivo 'cartas.npz'
if len(Cards) > 0:
    np.savez('cartas.npz', Cartas=Cards)
    print(f"Se han guardado {len(Cards)} cartas en el archivo 'cartas.npz'")
    print(f"Tamaño del archivo: {os.path.getsize('cartas.npz')/1024:.2f} KB")

cv2.destroyAllWindows()

