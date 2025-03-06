import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('TORREDELMAR.jpg')

plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("Selecciona 4 puntos de control en orden: \nSuperior-derecho, Superior-izquierdo, Inferior-Izquierdo, Inferior-Derecho")
pts = plt.ginput(4)
plt.close()

pts = np.array(pts, dtype=np.float32)

width = int(np.linalg.norm(pts[1] - pts[0]))
height = int(np.linalg.norm(pts[2] - pts[1]))

outs = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

M = cv2.getPerspectiveTransform(pts, outs)

dst = cv2.warpPerspective(src, M, (width, height))

cv2.imshow("Imagen original", src)
cv2.imshow("Imagen rectificada", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
