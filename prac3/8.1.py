import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny_edge_detection(image_path, min_threshold=100, max_threshold=200):

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    blurred = cv2.GaussianBlur(img, (5, 5), 0)

    edges = cv2.Canny(blurred, min_threshold, max_threshold)

    plt.figure(figsize=(15, 10))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Original')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(blurred, cmap='gray')
    plt.title('Suavizado Gaussiano')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(edges, cmap='gray')
    plt.title(f'Bordes Canny (min={min_threshold}, max={max_threshold})')
    plt.axis('off')

    plt.tight_layout()
    plt.show()


def canny_threshold_comparison(image_path):
    """
    Compara diferentes umbrales para el detector Canny.
    """
    # Cargar la imagen
    img = cv2.imread(image_path)

    # Convertir a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar suavizado Gaussiano
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Diferentes combinaciones de umbrales para Canny
    thresholds = [
        (30, 100),
        (50, 150),
        (100, 200),
        (150, 250)
    ]

    # Visualizar comparación
    plt.figure(figsize=(15, 10))

    # Mostrar imagen original
    plt.subplot(2, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Imagen Original')
    plt.axis('off')

    # Aplicar Canny con diferentes umbrales
    for i, (low, high) in enumerate(thresholds):
        edges = cv2.Canny(blurred, low, high)

        plt.subplot(2, 3, i + 2)
        plt.imshow(edges, cmap='gray')
        plt.title(f'Canny (min={low}, max={high})')
        plt.axis('off')

    plt.tight_layout()
    plt.show()


# Ejecutar el detector de Canny con la imagen 'checkerboard.jpg'
if __name__ == "__main__":
    # Ruta de la imagen - cambia por la ruta donde tengas 'checkerboard.jpg'
    image_path = "checkerboard.jpg"

    # Aplicar detector Canny con umbrales por defecto
    canny_edge_detection("peppers.png")
    canny_edge_detection("checkerboard.jpg")

    # Comparar diferentes umbrales
    # canny_threshold_comparison(image_path)