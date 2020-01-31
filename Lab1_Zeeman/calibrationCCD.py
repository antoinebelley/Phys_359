import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt


print('Load images')
im = Image.open('Data/CalibrationCCD/WhiteImage1.JPG').convert('F')
pixels1 = np.array(im)

im = Image.open('Data/CalibrationCCD/WhiteImage2.JPG').convert('F')
pixels2 = np.array(im)

im = Image.open('Data/CalibrationCCD/WhiteImage3.JPG').convert('F')
pixels3 = np.array(im)

im = Image.open('Data/CalibrationCCD/WhiteImage4.JPG').convert('F')
pixels4 = np.array(im)

im = Image.open('Data/CalibrationCCD/WhiteImage5.JPG').convert('F')
pixels5 = np.array(im)


images = [pixels1, pixels2, pixels3, pixels4, pixels5]

# Compute mean flux difference between each photo
error = 0
error += np.mean(np.absolute(pixels5-pixels4))
# error += np.mean(np.absolute(pixels5-pixels3))
# error += np.mean(np.absolute(pixels5-pixels2))
# error += np.mean(np.absolute(pixels5-pixels1))
# error += np.mean(np.absolute(pixels4-pixels3))
# error += np.mean(np.absolute(pixels4-pixels2))
# error += np.mean(np.absolute(pixels4-pixels1))
# error += np.mean(np.absolute(pixels3-pixels2))
# error += np.mean(np.absolute(pixels3-pixels1))
# error += np.mean(np.absolute(pixels2-pixels1))

print(error)



