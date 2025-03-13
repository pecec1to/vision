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


# Add this class after the Card class definition
class Motif:
    def __init__(self):
        self.id = 0
        self.label = ''  # One of: 'Diamonds', 'Spades', 'Hearts', 'Clubs', '0', '2',...
        self.area = 0
        self.boundingBox = np.zeros(1, dtype=[('x', np.intc), ('y', np.intc),
                                              ('width', np.intc), ('height', np.intc)]).view(np.recarray)
        self.contour = None
        self.grayImage = np.empty([0, 0], dtype=np.uint8)

    def __repr__(self):
        rep = f"Motif ID: {self.id} -- Label: {self.label} -- Area: {self.area}"
        bb = f"Bounding Box: {str(self.boundingBox)}"
        new_line = "\n"
        return rep + new_line + bb


# Modify the Card class to include a list of motifs
# Add this line inside the Card.__init__ method:
# self.motifs = []

# Function to segment and extract motifs from a card
def segmentar_objetos_carta(card):
    # Possible labels for classification
    card_labels = ('Diamonds', 'Spades', 'Hearts', 'Clubs', '0', '2', '3', '4', '5',
                   '6', '7', '8', '9', 'A', 'J', 'Q', 'K', 'Others')

    roi = card.grayImage

    ret, bw = cv2.threshold(roi, 150, 255, cv2.THRESH_BINARY_INV)

    (totalLabels, label_ids, values, centroid) = cv2.connectedComponentsWithStats(bw, 4, cv2.CV_32S)

    viz_image = card.colorImage.copy()

    # Process each component (skip the first one which is the background)
    motif_id = 0
    for i in range(1, totalLabels):
        # Get area of the component
        area = values[i, cv2.CC_STAT_AREA]

        # Filter by area to eliminate noise (adjust threshold as needed)
        if area > 100 and area < 20000:  # Skip very small or very large objects
            # Create a binary mask for this component
            componentMask = (label_ids == i).astype("uint8") * 255

            # Find contours of the component
            contours, hierarchy = cv2.findContours(componentMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if len(contours) > 0:
                # Create a new motif
                motif = Motif()
                motif.id = motif_id
                motif.area = area
                motif.contour = contours[0]

                # Get bounding box
                x, y, w, h = cv2.boundingRect(contours[0])
                motif.boundingBox[0] = (x, y, w, h)

                # Extract the grayscale image of the motif
                motif.grayImage = roi[y:y + h, x:x + w].copy()

                # For now, set all labels to 'Others'
                # Later, we could implement a classifier to identify suits and figures
                motif.label = 'Others'

                # Add the motif to the card
                card.motifs.append(motif)

                # Draw contour on visualization image
                cv2.drawContours(viz_image, contours, -1, (0, 255, 0), 2)

                # Draw bounding box
                cv2.rectangle(viz_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # Increment motif ID
                motif_id += 1

    # Show the visualization
    cv2.imshow(window_roi_color, viz_image)

    return card

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

                minRect = cv2.minAreaRect(contours[0])
                angle = minRect[2]

                # Crear y apuntar los datos de la carta
                c = Card()
                c.cardId = icard
                c.boundingBox[0] = (x1, y1, w, h)
                c.grayImage = roi
                c.colorImage = roi_color

                c.angle = angle
                center = (int(w // 2), int(h // 2))
                rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
                rotated_roi = cv2.warpAffine(roi, rotation_matrix, (w, h))
                rotated_roi_color = cv2.warpAffine(roi_color, rotation_matrix, (w, h))

                c.motifs = []
                c = segmentar_objetos_carta(c)

                # Añadir la carta a la lista de cartas
                Cards.append(c)
                icard+=1

        print('\n')
        key = -1
        while (key == -1):
            key = cv2.pollKey()
            # Aquí va la función  cv2.inRange(....)
            cv2.imshow(window_original, img)  # , cmap='gray')
            cv2.imshow(window_roi, rotated_roi)
            cv2.imshow(window_roi_color, rotated_roi_color)
            cv2.imshow(window_threshold, output)  # , cmap='gray')

        if key == ord('q') or key == 27:  # 'q' o ESC para acabar
            break

# Guardar las cartas en una archivo 'cartas.npz'
if len(Cards) > 0:
    np.savez('cartas.npz', Cartas=Cards)
    print(f"Se han guardado {len(Cards)} cartas en el archivo 'cartas.npz'")
    print(f"Tamaño del archivo: {os.path.getsize('cartas.npz')/1024:.2f} KB")

cv2.destroyAllWindows()

