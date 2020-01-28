import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt


im = Image.open('FP_pattern_91.6mV_j0.JPG').convert('F')
pixels_1 = np.array(im)

plt.imshow(pixels_1)
plt.colorbar()
plt.show()

im = Image.open('FP_pattern_91.6mV_j1.JPG').convert('F')
pixels_2 = np.array(im)

plt.imshow(pixels_2)
plt.colorbar()
plt.show()

print(np.mean(np.absolute(pixels_1-pixels_2)))

plt.imshow(np.absolute(pixels_1-pixels_2))
plt.colorbar()
plt.show()