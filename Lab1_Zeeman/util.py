#This module contains all useful functions for the plotting/scripting required for the analysis of the lab



import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline as spline
import matplotlib.pyplot as plt
from lmfit import models
from scipy import signal
import random

class ErrorPropagationSpline(object):
    """
    Does a spline fit, but returns both the spline value and associated uncertainty.
    """
    def __init__(self, x, y, yerr, N=1000, *args, **kwargs):
        """
        See docstring for InterpolatedUnivariateSpline
        """
        yy = np.vstack([y + np.random.normal(loc=0, scale=yerr) for i in range(N)]).T
        self._splines = [spline(x, yy[:, i], *args, **kwargs) for i in range(N)]

    def __call__(self, x, *args, **kwargs):
        """
        Get the spline value and uncertainty at point(s) x. args and kwargs are passed to spline.__call__
        :param x:
        :return: a tuple with the mean value at x and the standard deviation
        """
        x = np.atleast_1d(x)
        s = np.vstack([curve(x, *args, **kwargs) for curve in self._splines])
        return (np.mean(s, axis=0), np.std(s, axis=0))

 

def interpolation_hall_probe(value):
    """Returns the interpolation of the measurement chart for the HallProbe. It uses the cubic spine interpolation from scipy
    to give the interpolation and error associated."""

    #Import the data from the appendix
    #MAKE SURE TO EDIT THIS PATH IF FILE LOCATION CHANGES
    HallProbe_Data=np.loadtxt('Data/CalibrationHallProbe/EQ3485_Calibration.csv',delimiter=',')
    volt=HallProbe_Data[:,0]
    bfield=HallProbe_Data[:,1]*0.1
    #Interpolation 
    interp = ErrorPropagationSpline(volt, bfield, 0.001)
    return interp(value)



def convert_voltage_to_tesla():
    raise NotImplementedError

def plot_data_csv(filename, path = "Data/CalibrationPowerSupply/" , savepath= "Figures/"):
    data = np.loadtxt(path+filename+'.csv', skiprows=1, delimiter=',')
    x = data[:,0]
    y = data[:,1]
    plt.plot(x,y,'.')
    plt.savefig(savepath+filename+'.png')


def gaussian(x, amp, cen, wid):
    return amp * exp(-(x-cen)**2 /wid)


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
            model.set_param_hint('sigma', min=1, max=30)
            model.set_param_hint('center', min=x_min, max=x_max)
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







