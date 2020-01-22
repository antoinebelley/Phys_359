import numpy as np 
from scipy import signal, ndimage
from scipy import optimize as opt
from PIL import Image
from matplotlib import pyplot as plt

# import the image
print('Import image\n')
im = Image.open('IMG_4378.JPG').convert('F')
pixels = np.array(im)
# print(pixels)
# plt.imshow(im)
# plt.show()

# Create a template
print('Create circle template\n')
template = np.ones_like(pixels)
r = 200
y0 = (template[0].size)/2
x0 = (template[:,0].size)/2
for i in range(template[0].size):
    for j in range(template[1].size):
        if (i-x0)**2 + (j-y0)**2 < 470**2 and (i-x0)**2 + (j-y0)**2 > 430**2:
            template[i,j] = 80

# plt.imshow(template)
# plt.show()


print('Cross Correlate\n')
# corr = signal.correlate2d(pixels, template, boundary='symm')
corr = signal.fftconvolve(pixels,template, mode='same')
print(corr.shape)

y0, x0 = np.unravel_index(np.argmax(corr), corr.shape)
amp = np.max(corr)
print(y0)
print(x0)

# plt.imshow(corr)
# plt.axvline(x0)
# plt.axhline(y0)
# plt.show()



def twoD_Gaussian(data,amplitude, xo, yo, sigma_x, sigma_y, theta, offset):
    x,y = data
    xo = float(xo)
    yo = float(yo)    
    a = (np.cos(theta)**2)/(2*sigma_x**2) + (np.sin(theta)**2)/(2*sigma_y**2)
    b = -(np.sin(2*theta))/(4*sigma_x**2) + (np.sin(2*theta))/(4*sigma_y**2)
    c = (np.sin(theta)**2)/(2*sigma_x**2) + (np.cos(theta)**2)/(2*sigma_y**2)
    g = offset + amplitude*np.exp( - (a*((x-xo)**2) + 2*b*(x-xo)*(y-yo) 
                            + c*((y-yo)**2)))
    return g.ravel()

# Create x and y indices
x = np.linspace(0, 3999, 4000)
y = np.linspace(0, 2999, 3000)
x, y = np.meshgrid(x, y)
xdata = np.vstack((x.ravel(),y.ravel()))

# add some noise to the data and try to fit the data generated beforehand
initial_guess = (amp,x0,y0,40,40,0,2)

popt, pcov = opt.curve_fit(twoD_Gaussian, xdata, corr.ravel(), p0=initial_guess)

data_fitted = twoD_Gaussian(xdata, *popt)

fig, ax = plt.subplots(1, 1)

ax.imshow(corr, origin='bottom',extent=(x.min(), x.max(), y.min(), y.max()))
ax.contour(x, y, data_fitted.reshape(3000, 4000), 8, colors='w')
plt.show()
    


# plt.imshow(pixels)
# plt.plot(x,y, '.', color='red')
# plt.show()

