import numpy as np 
from scipy import signal, ndimage
from scipy import optimize as opt
from PIL import Image
from matplotlib import pyplot as plt
from lmfit import models
import random
from mpl_toolkits.axes_grid1 import make_axes_locatable
from numba import jit

@jit
def circular_pattern(template, r,x,y):
    template = template.copy()
    for n in range(1,4):
        for i in range(template[0].size):
            for j in range(template[1].size):
                if (i-x)**2 + (j-y)**2 < (n*r+10)**2 and (i-x)**2 + (j-y)**2 > (n*r-10)**2:
                    template[i,j] = 40
        #template[x-10:x+10,:] = 60
               
    return template



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
            model.set_param_hint('sigma', min=1, max=100)
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
        params[f'm{i}_amplitude'].stderr = 0.6
    return composite_model, params


def update_spec_from_peaks(spec, model_indicies, peak_widths=(10, 25), **kwargs):
    x = spec['x']
    y = spec['y']
    x_range = np.max(x) - np.min(x)
    peak_indicies = signal.find_peaks(ndimage.gaussian_filter(y,4), width=peak_widths)[0]
    np.random.shuffle(peak_indicies)
    for peak_indicie, model_indicie in zip(peak_indicies, model_indicies):
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


def exponential(x,a,b,c):
    return a*np.exp(x*b)+c




class ImageAnalyse():
    def __init__(self, image, image_size = (4000,3000)):
        self.name = image[:-4]
        print('Importing image...\n')
        im = Image.open(image).convert('F')
        pixels = np.array(im)
        pixels[pixels>50] = 50
        self.image = pixels
        self.image_size_x=image_size[0]-1
        self.image_size_y=image_size[1]-1
        x = np.linspace(0, self.image_size_x, self.image_size_x+1)
        y = np.linspace(0, self.image_size_y, self.image_size_y+1)
        self.x, self.y = np.meshgrid(x, y)


    def find_circle_center(self, r=225):
        #Creates a cricular mask to for which we want to find the correlation
        template = np.ones_like(self.image)
        y = int(template[0].size)//2
        x = int(template[:,0].size)//2
        x0=[]
        y0=[]
        for s in range(r-10,r+11):
            template_r = circular_pattern(template,s,x,y)
            #Use fft's to find the correaltion between the mask and the image
            print('Performing cross correlation...\n')
            corr = signal.fftconvolve(self.image,template_r, mode='same')
            yc, xc = np.unravel_index(np.argmax(corr), corr.shape)
            y0.append(yc)
            x0.append(xc)
        y0 = np.array(y0)
        x0=np.array(x0)
        err_y0 = np.round(np.std(y0))
        self.y0=int(np.round((np.mean(y0))))
        err_x0 = np.round(np.std(x0))
        self.x0 = int(np.round((np.mean(x0))))+100

        self.amp = np.max(corr)
        self.corr = corr
        print(f'The position of the center is given by ({self.x0} pm {err_x0},{self.y0} pm {err_y0}).\n')


    def line_profile(self,xvalues, yvalues, z):
        x0, x1 = xvalues[0],xvalues[1] # These are in _pixel_ coordinates!!
        y0, y1 = yvalues[0],yvalues[1] # These are in _pixel_ coordinates!!
        length = int(np.hypot(x1-x0,y1-y0))
        x, y = np.linspace(x0, x1, length), np.linspace(y0, y1, length)
        # Extract the values along the line, using cubic interpolation
        zi = ndimage.map_coordinates(z, np.vstack((y,x)))
        return zi, x,y


    def find_split(self, width):
        line_profile_y,_,self.y = self.line_profile([self.x0,self.x0],[0, self.image_size_y], self.image)
        self.line = line_profile_y
        self.line_profile_y = ndimage.gaussian_filter(line_profile_y,4)
        #self.exp_y = self.exp_fit(self.y, self.line_profile_y,width, self.y0)
        line_profile_y_clean = self.line_profile_y[:self.y0]#-exp_y
        self.line_profile_x,self.x,_ = self.line_profile([0,self.image_size_x],[self.y0, self.y0], self.image)
        #self.exp_x = self.exp_fit(self.x, self.line_profile_x,width, self.x0)
        #line_profile_x_clean = self.line_profile_x[:self.x0]#-exp_x
        self.spec_y, self.peaks_y, self.components_y, self.fit_y = self.multi_gaussian_fitting(self.y,line_profile_y_clean, width, self.y0, distance = 1700)
        #self.spec_x, self.peaks_x, self.components_x, self.fit_x = self.multi_gaussian_fitting(self.x,line_profile_x_clean, width, self.x0, distance = 1500)
        return self.fit_y


    def plot_fig(self):
        fig, ax1 = plt.subplots(figsize=(8, 8))
        ax1.imshow(self.image)
        ax1.plot([self.x0,self.x0], [0, self.image_size_y], 'r-')
        ax1.plot([0, self.image_size_x], [self.y0, self.y0], 'r-')
        ax1.plot(self.x0, self.y0,'ro')
        ax1.margins(0)
        ax1.use_sticky_edges = True
        ax1.set_aspect(1.)
        ax1.set_ylabel('Pixels', size = 14)
        ax1.set_xlabel('Pixels', size = 14)
        

        # create new axes on the right and on the top of the current axes
        # The first argument of the new_vertical(new_horizontal) method is
        # the height (width) of the axes to be created in inches.
        divider = make_axes_locatable(ax1)
        ax0 = divider.append_axes("top", 1.2, pad=0.32, sharex=ax1)
        ax2 = divider.append_axes("right", 1.2, pad=0.32, sharey=ax1)
        
        

        # make some labels invisible
        ax1.xaxis.set_tick_params(labelrotation = -60)
        ax2.xaxis.set_tick_params(labelrotation = -60)
        ax1.yaxis.set_tick_params(labelrotation = 30)
        ax0.yaxis.set_tick_params(labelrotation = 30)
        ax0.xaxis.set_tick_params(labelbottom=False)
        ax0.xaxis.set_tick_params(labelbottom=False)
        ax2.yaxis.set_tick_params(labelleft=False)


        ax2.errorbar(self.line_profile_y, self.y, xerr=0.6, fmt='')
        ax2.axhline(self.y0, c='red')
        ax2.margins(0)
        ax2.set_xlabel(r'Intensity', size = 14)
        ax2.set_xlim(0,75)
        ax2.tick_params(axis="both", labelsize=14)
        ax0.tick_params(axis="both", labelsize=14)
        ax1.tick_params(axis="both", labelsize=14)
        ax0.set_ylabel('Intensity', size=14)
        
        
        ax0.errorbar(self.x,self.line_profile_x, yerr=0.6, fmt='')
        ax0.axvline(self.x0, c='red')
        ax0.set_ylim(0,75)
        ax0.margins(0)
        plt.savefig(f'{self.name}.png')
        
        


    def multi_gaussian_fitting(self,x,y, width, center, distance):
        spec = {
                'x': x[center-distance:center-700],
                'y': y[center-distance:center-700],
                'model': [{'type': 'GaussianModel'}]
            }
        peaks = signal.find_peaks(ndimage.gaussian_filter(y[center-distance:center-700],4), width=width)[0]
        for i in range(len(peaks)):
            spec['model'].append({'type': 'GaussianModel'})
        indices = np.arange(len(peaks))
        peaks_found = update_spec_from_peaks(spec, indices, peak_widths=width)
        model, params = generate_model(spec)
        output = model.fit(spec['y'], params, x=spec['x'])
        components = output.eval_components(x=spec['x'])
        fit_peak = np.zeros([len(spec['model']),3])
        best_values = output.best_values
        for i, model in enumerate(spec['model']):
            prefix = f'm{i}_'
            fit_peak[i][0] = best_values[prefix+"center"]
            fit_peak[i][1]=  center-best_values[prefix+"center"]
            fit_peak[i][2] = best_values[prefix+'sigma']
        fit_peak = np.array(sorted(fit_peak, key=lambda fit_peak_entry: fit_peak_entry[1]))
        return spec, peaks_found, components, fit_peak

    def exp_fit(self,x, y, width, center):
        peaks = signal.find_peaks_cwt(-y[:center-700],(width,))
        background = y[peaks]
        initial_guess = np.array([2,0.0001,0])
        popt, pcov = opt.curve_fit(exponential,peaks , background, p0=initial_guess)
        exp = exponential(x[:center-600],popt[0],popt[1],popt[2])
        y = y[:center]-exponential(x[:center],popt[0],popt[1],popt[2])
        return exp



# im = ImageAnalyse('Pictures/JPEG_29Jan/IMG_4442.JPG')
# im.find_circle_center(r=155)
# fit_y = im.find_split(10)

# print('Peaks found in y\n')
# print(fit_y)