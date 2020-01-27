import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt


im = Image.open('IMG_4399.JPG').convert('F')
pixels_1 = np.array(im)

im = Image.open('IMG_4400.JPG').convert('F')
pixels_2 = np.array(im)

print(np.mean(np.absolute(pixels_1-pixels_2)))

plt.imshow(np.absolute(pixels_1-pixels_2))
plt.colorbar()
plt.show()