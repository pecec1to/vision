import cv2
import numpy as np

src = cv2.imread('sea.png')

rows, cols = src.shape[:2]

M_translation = np.float32([[1, 0, 100], [0, 1, 50]])
dst_translation = cv2.warpAffine(src, M_translation, (cols + 100, rows + 50))

cv2.imshow('Imagen trasladada', dst_translation)

M_rotation = cv2.getRotationMatrix2D((cols / 2, rows / 2), 10, 1.5)
dst_rotation = cv2.warpAffine(src, M_rotation, (cols, rows))

cv2.imshow('Imagen rotada', dst_rotation)

M_scaling = np.float32([[2, 0, 0], [0, 2, 0]])
dst_scaling = cv2.warpAffine(src, M_scaling, (cols * 2, rows * 2))

cv2.imshow('Imagen escalada', dst_scaling)

dst_combined = cv2.warpAffine(dst_rotation, M_translation, (cols + 100, rows + 50))
dst_combined = cv2.warpAffine(dst_combined, M_scaling, (cols * 2, rows * 2))

cv2.imshow('Imagen combinada', dst_combined)

cv2.waitKey(0)
cv2.destroyAllWindows()
