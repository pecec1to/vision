import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('sea.png')

plt.imshow(img)
plt.show()