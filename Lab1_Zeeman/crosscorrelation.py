import numpy as np 
from scipy import signal, ndimage
from scipy import optimize as opt
from PIL import Image
from matplotlib import pyplot as plt
from lmfit import models
import random

# # import the image
# print('Import image\n')
# im = Image.open('IMG_4378.JPG').convert('F')
# pixels = np.array(im)
# # print(pixels)
# # plt.imshow(im)
# # plt.show()

# # Create a template
# print('Create circle template\n')
# template = np.ones_like(pixels)
# r = 200
# y0 = (template[0].size)/2
# x0 = (template[:,0].size)/2
# for i in range(template[0].size):
#     for j in range(template[1].size):
#         if (i-x0)**2 + (j-y0)**2 < 470**2 and (i-x0)**2 + (j-y0)**2 > 430**2:
#             template[i,j] = 80

# # plt.imshow(template)
# # plt.show()


# print('Cross Correlate\n')
# # corr = signal.correlate2d(pixels, template, boundary='symm')
# corr = signal.fftconvolve(pixels,template, mode='same')
# print(corr.shape)

# y0, x0 = np.unravel_index(np.argmax(corr), corr.shape)
# amp = np.max(corr)
# print(y0)
# print(x0)

# # plt.imshow(corr)
# # plt.axvline(x0)
# # plt.axhline(y0)
# # plt.show()



# def twoD_Gaussian(data,amplitude, xo, yo, sigma_x, sigma_y, theta, offset):
#     x,y = data
#     xo = float(xo)
#     yo = float(yo)    
#     a = (np.cos(theta)**2)/(2*sigma_x**2) + (np.sin(theta)**2)/(2*sigma_y**2)
#     b = -(np.sin(2*theta))/(4*sigma_x**2) + (np.sin(2*theta))/(4*sigma_y**2)
#     c = (np.sin(theta)**2)/(2*sigma_x**2) + (np.cos(theta)**2)/(2*sigma_y**2)
#     g = offset + amplitude*np.exp( - (a*((x-xo)**2) + 2*b*(x-xo)*(y-yo) 
#                             + c*((y-yo)**2)))
#     return g.ravel()

# # Create x and y indices
# x = np.linspace(0, 3999, 4000)
# y = np.linspace(0, 2999, 3000)
# x, y = np.meshgrid(x, y)
# xdata = np.vstack((x.ravel(),y.ravel()))

# # add some noise to the data and try to fit the data generated beforehand
# initial_guess = (amp,x0,y0,40,40,0,2)

# popt, pcov = opt.curve_fit(twoD_Gaussian, xdata, corr.ravel(), p0=initial_guess)

# data_fitted = twoD_Gaussian(xdata, *popt)

# fig, ax = plt.subplots(1, 1)

# ax.imshow(corr, origin='bottom',extent=(x.min(), x.max(), y.min(), y.max()))
# ax.contour(x, y, data_fitted.reshape(3000, 4000), 8, colors='w')
# plt.show()
    


# plt.imshow(pixels)
# plt.plot(x,y, '.', color='red')
# plt.show()
def generate_model(spec):
    composite_model = None
    params = None
    x = spec['x']
    y = spec['y']
    x_min = np.min(x)
    x_max = np.max(x)
    x_range = x_max - x_min
    y_max = np.max(y)
    for i, basis_func in enumerate(spec['model']):
        prefix = f'm{i}_'
        model = getattr(models, basis_func['type'])(prefix=prefix)
        if basis_func['type'] in ['GaussianModel', 'LorentzianModel', 'VoigtModel']: # for now VoigtModel has gamma constrained to sigma
            model.set_param_hint('sigma', min=1, max=300)
            model.set_param_hint('center', vary=False)
            model.set_param_hint('height', min=1e-6, max=1.1*y_max)
            model.set_param_hint('amplitude', min=1e-6)
            # default guess is horrible!! do not use guess()
            default_params = {
                prefix+'center': x_min + x_range * random.random(),
                prefix+'height': y_max * random.random(),
                prefix+'sigma': x_range * random.random()
            }
        else:
            raise NotImplemented(f'model {basis_func["type"]} not implemented yet')
        if 'help' in basis_func:  # allow override of settings in parameter
            for param, options in basis_func['help'].items():
                model.set_param_hint(param, **options)
        model_params = model.make_params(**default_params, **basis_func.get('params', {}))
        if params is None:
            params = model_params
        else:
            params.update(model_params)
        if composite_model is None:
            composite_model = model
        else:
            composite_model = composite_model + model
    return composite_model, params

def update_spec_from_peaks(spec, model_indicies, peak_widths=(10, 25), **kwargs):
    x = spec['x']
    y = spec['y']
    x_range = np.max(x) - np.min(x)
    peak_indicies = signal.find_peaks_cwt(y, peak_widths)
    np.random.shuffle(peak_indicies)
    for peak_indicie, model_indicie in zip(peak_indicies.tolist(), model_indicies):
        model = spec['model'][model_indicie]
        if model['type'] in ['GaussianModel', 'LorentzianModel', 'VoigtModel']:
            params = {
                'height': y[peak_indicie],
                'sigma': x_range / len(x) * np.min(peak_widths),
                'center': x[peak_indicie]
            }
            if 'params' in model:
                model.update(params)
            else:
                model['params'] = params
        else:
            raise NotImplemented(f'model {basis_func["type"]} not implemented yet')
    return peak_indicies

def print_best_values(spec, output):
    model_params = {
        'GaussianModel':   ['sigma'],
    }
    best_values = output.best_values
    print('center  sigma')
    for i, model in enumerate(spec['model']):
        prefix = f'm{i}_'
        values = ', '.join(f'{best_values[prefix+param]:8.3f}' for param in model_params[model["type"]])
        print(f'[{best_values[prefix+"center"]:3.3f}]  {values}')





class ImageAnalyse():

    def __init__(self, image, image_size = (4000,3000)):
        print('Importing image...\n')
        im = Image.open(image).convert('F')
        pixels = np.array(im)
        self.image = pixels
        self.image_size_x=image_size[0]-1
        self.image_size_y=image_size[1]-1
        x = np.linspace(0, self.image_size_x, self.image_size_x+1)
        y = np.linspace(0, self.image_size_y, self.image_size_y+1)
        self.x, self.y = np.meshgrid(x, y)

    def find_circle_center(self, r=200):
        #Creates a cricular mask to for which we want to find the correlation
        template = np.ones_like(self.image)
        y0 = (template[0].size)/2
        x0 = (template[:,0].size)/2
        for i in range(template[0].size):
            for j in range(template[1].size):
                if (i-x0)**2 + (j-y0)**2 < 470**2 and (i-x0)**2 + (j-y0)**2 > 430**2:
                    template[i,j] = 80
        #Use fft's to find the correaltion between the mask and the image
        print('Performing cross correlation...\n')
        corr = signal.fftconvolve(self.image,template, mode='same')
        self.y0, self.x0 = np.unravel_index(np.argmax(corr), corr.shape)
        self.amp = np.max(corr)
        self.corr = corr
        print(f'The position of the center is given by ({self.x0},{self.y0}).\n')
        self.line_profile_corr_x = self.line_profile([0,self.image_size_x], [self.y0, self.y0], self.corr)
        self.line_profile_corr_y = self.line_profile([self.x0, self.x0], [0, self.image_size_y], self.corr)

    def line_profile(self,xvalues, yvalues, z):
        x0, x1 = xvalues[0],xvalues[1] # These are in _pixel_ coordinates!!
        y0, y1 = yvalues[0],yvalues[1] # These are in _pixel_ coordinates!!
        length = int(np.hypot(x1-x0,y1-y0))
        x, y = np.linspace(x0, x1, length), np.linspace(y0, y1, length)
        # Extract the values along the line, using cubic interpolation
        zi = ndimage.map_coordinates(z, np.vstack((y,x)))
        return zi, x,y

    def twoD_Gaussian(self,data, amplitude, sigma_x, sigma_y, theta, offset):
        x,y = data
        xo = float(self.x0)
        yo = float(self.y0)    
        a = (np.cos(theta)**2)/(2*sigma_x**2) + (np.sin(theta)**2)/(2*sigma_y**2)
        b = -(np.sin(2*theta))/(4*sigma_x**2) + (np.sin(2*theta))/(4*sigma_y**2)
        c = (np.sin(theta)**2)/(2*sigma_x**2) + (np.cos(theta)**2)/(2*sigma_y**2)
        g = offset + amplitude*np.exp( - (a*((x-xo)**2) + 2*b*(x-xo)*(y-yo) 
                                + c*((y-yo)**2)))
        return g.ravel()

    def fit_gaussian(self):
        xdata = np.vstack((self.x.ravel(),self.y.ravel()))
        try:
            initial_guess = (self.amp,5,5,0,0)
            popt, pcov = opt.curve_fit(self.twoD_Gaussian, xdata, self.corr.ravel(), p0=initial_guess)
        except:
            self.find_circle_center()
            initial_guess = (self.amp,1,1,0,0)
            popt, pcov = opt.curve_fit(self.twoD_Gaussian, xdata, self.corr.ravel(), p0=initial_guess)
        data_fitted = self.twoD_Gaussian(xdata, *popt)
        return popt, pcov, data_fitted

    def plot_center_and_error(self):
        #popt, pcov, fit = self.fit_gaussian()
        fig, ax = plt.subplots(1, 1)
        #print(popt)
        ax.imshow(self.image,extent=(self.x.min(), self.x.max(), self.y.min(), self.y.max()))
        plt.plot(self.x0, 3000-self.y0,'ro')
        #ax.contour(self.x, np.abs(3000-self.y), fit.reshape(3000, 4000), 0, colors='w')
        plt.show()

    def find_split(self, width):
        line_profile,_,y = self.line_profile([self.x0,self.x0],[0, self.image_size_y], self.image)
        spec = {
                'x': y[:self.y0],
                'y': line_profile[:self.y0],
                'model': []
            }
        peaks = signal.find_peaks_cwt(line_profile[:self.y0], (width,))
        for i in range(len(peaks)):
            spec['model'].append({'type': 'GaussianModel'})
        indices = np.arange(len(peaks))
        peaks_found = update_spec_from_peaks(spec, indices, peak_widths=(width,))
        model, params = generate_model(spec)
        output = model.fit(spec['y'], params, x=spec['x'])
        components = output.eval_components(x=spec['x'])
        fig, axes = plt.subplots(nrows=2)
        axes[0].imshow(self.image,origin='bottom', extent=(self.x.min(), self.x.max(), self.y.min(), self.y.max()))
        axes[0].plot([self.x0,self.x0], [0, self.image_size_y], 'ro-')
        axes[0].axis('image')

        axes[1].plot(line_profile)
        axes[1].axvline(self.y0, c='red')
        for i in peaks_found:
            axes[1].axvline(x=i, c='black', linestyle='dotted')
        for i, model in enumerate(spec['model']):
            axes[1].plot(spec['x'], components[f'm{i}_'])

        plt.show()
        fit_peak = np.zeros([len(spec['model']),2])
        best_values = output.best_values
        for i, model in enumerate(spec['model']):
            prefix = f'm{i}_'
            fit_peak[i][0] = best_values[prefix+"center"]
            fit_peak[i][1] = best_values[prefix+'sigma']
        fit_peak = np.sort(fit_peak,axis=0)
        print(fit_peak)
        delta = fit_peak[-5:-1]
        delta[:,0] = np.absolute(self.y0-delta[:,0])
        print(delta)



im = ImageAnalyse('Pictures/Pattern_30.1.JPG')
im.find_circle_center(r=500)
im.find_split(50)
im.plot_center_and_error()

