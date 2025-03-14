import matplotlib.pyplot as plt
import cv2

cameraman = cv2.imread("cameraman.tif")
moon = cv2.imread("moon.tif")

cameraman_r = cv2.resize(cameraman, (256, 256))
moon_r = cv2.resize(moon, (256, 256))

cameraman_m = cv2.multiply(cameraman_r, 1.8)
moon_m = cv2.multiply(moon_r, 1.2)

S = cv2.subtract(cameraman_m, moon_m)
S = cv2.add(S, 128)

fig, ax = plt.subplots(1, 3, figsize=(15, 10))

ax[0].imshow(cameraman_r)
ax[0].set_title("Cameraman")
ax[0].axis("off")

ax[1].imshow(moon_r)
ax[1].set_title("Moon")
ax[1].axis("off")

ax[2].imshow(S)
ax[2].set_title("S = CAM * 1.8 - MOON * 1.2 + 128")
ax[2].axis("off")

plt.show()
