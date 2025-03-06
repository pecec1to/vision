import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image



def saltAndPepper_noise(img, percent):
    # img: Image to introduce the noise
    # percent [0,1) percentaje of noise
    result = np.array(img)
    per = int(percent * result.size)
    for k in range(per):
        i = int(np.random.random() * result.shape[1])
        j = int(np.random.random() * result.shape[0])
        if result.ndim == 2:
            result[j, i] = 255
        elif (result.ndim == 3):
            result[j, i, 0] = 255
            result[j, i, 1] = 255
            result[j, i, 2] = 255
    return result


def clamp(num, min_value=0, max_value=255): return int(max(min(num, max_value), min_value))


def gaussian_noise(img):
    global s
    result = np.array(img)
    h, w, c = result.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = result[row, col, 0]
            g = result[row, col, 1]
            r = result[row, col, 2]
            result[row, col, 0] = clamp(b + s[0])
            result[row, col, 1] = clamp(g + s[1])
            result[row, col, 2] = clamp(r + s[2])
    return result


if __name__ == '__main__':

	fig, axs = plt.subplots(1, 3)

	img = np.array(Image.open('peppers.png'))

	axs[0].imshow(img)
	axs[0].set_title("Imagen original")
	axs[0].axis("off")

	plt.imshow(img)
	#print(img.flags)

	img_noise_g = gaussian_noise(img)
	plt.imshow(img_noise_g)
	axs[1].imshow(img_noise_g)
	axs[1].set_title("Ruido gaussiano")
	axs[1].axis("off")


	img_g_f = cv2.medianBlur(img_noise_g,5)
	axs[2].imshow(img_g_f)
	axs[2].set_title("Filtro de mediana")
	axs[2].axis("off")
	plt.show()

