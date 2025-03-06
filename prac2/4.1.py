import cv2
import numpy as np
import matplotlib.pyplot as plt
src = cv2.imread('sea.png')
dst = cv2.resize(src, (256, 256), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Imagen original', src)
cv2.imshow('Imagen escalada', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.subplot(121),plt.imshow(src),plt.title('Input') # Visualización en matpolotlib.pyplot
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()