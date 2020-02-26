import numpy as np
from lmfit import models
import matplotlib.pyplot as plt
from scipy import signal
import random


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
            model.set_param_hint('sigma', min=1e-6, max=x_range)
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


def Fit_Lorentzian(x,y):
    spec = {
                'x': x,
                'y': y,
                'model': [{'type': 'LorentzianModel',
                            'params': {'center': 66, 'sigma':1, 'amplitude':70000}},
                          {'type': 'LorentzianModel',
                          'params': {'center': 93, 'sigma':1, 'amplitude':70000}},
                          {'type': 'LorentzianModel',
                          'params': {'center': 119, 'sigma':1, 'amplitude':40000}},
                          {'type': 'LorentzianModel',
                          'params': {'center': 137, 'sigma':1, 'amplitude':40000}},
                          {'type': 'LorentzianModel',
                          'params': {'center': 165, 'sigma':1, 'amplitude':70000}},
                          {'type': 'LorentzianModel',
                          'params': {'center': 192, 'sigma':1, 'amplitude':70000}},
                          {'type': 'LorentzianModel',
                          'params': {'center': 319, 'sigma':1, 'amplitude':80000}},
                          {'type': 'LorentzianModel',
                          'params': {'center': 346, 'sigma':1, 'amplitude':70000}},
                          {'type': 'LorentzianModel',
                          'params': {'center': 374, 'sigma':1,'amplitude':40000}},
                          {'type': 'LorentzianModel',
                          'params': {'center': 392, 'sigma':1, 'amplitude':40000}},
                          {'type': 'LorentzianModel',
                          'params': {'center': 419, 'sigma':1, 'amplitude':80000}},
                          {'type': 'LorentzianModel',
                          'params': {'center': 446, 'sigma':1}}]
            }
    #peaks_found = update_spec_from_peaks(spec, [0,1,2,3,4,5,6,7,8,9,10,11], peak_widths=(15,))
    model, params = generate_model(spec)
    output = model.fit(spec['y'], params, x=spec['x'])
    #components = output.eval_components(x=spec['x'])
    fig, gridspec = output.plot(data_kws={'markersize':  1})
    plt.show()
    print_best_values(spec,output)

def print_best_values(spec, output):
    model_params = {
        'GaussianModel':   ['amplitude', 'sigma'],
        'LorentzianModel': ['amplitude', 'sigma'],
        'VoigtModel':      ['amplitude', 'sigma', 'gamma']
    }
    best_values = output.best_values
    print('center    model   amplitude     sigma      gamma')
    for i, model in enumerate(spec['model']):
        prefix = f'm{i}_'
        values = ', '.join(f'{best_values[prefix+param]:8.3f}' for param in model_params[model["type"]])
        print(f'[{best_values[prefix+"center"]:3.3f}] {model["type"]:16}: {values}')



data = np.loadtxt('iron0224.txt')
x = data[:,0][:-1]
y = -data[:,1][:-1]+np.max(data[:,1])

Fit_Lorentzian(x,y)



# def Fit_Lorentzian(x,y):
#     spec = {
#                 'x': x,
#                 'y': y,
#                 'model': [{'type': 'LorentzianModel',
#                             'params': {'center': 46, 'sigma':1, 'amplitude':20000}},
#                           {'type': 'LorentzianModel',
#                           'params': {'center': 75, 'sigma':1, 'amplitude':20000}},
#                           {'type': 'LorentzianModel',
#                           'params': {'center': 120, 'sigma':1, 'amplitude':80000}},
#                           {'type': 'LorentzianModel',
#                           'params': {'center': 129, 'sigma':1, 'amplitude':80000}},
#                           {'type': 'LorentzianModel',
#                           'params': {'center': 168, 'sigma':1, 'amplitude':20000}},
#                           {'type': 'LorentzianModel',
#                           'params': {'center': 199, 'sigma':1, 'amplitude':20000}},
#                           {'type': 'LorentzianModel',
#                           'params': {'center': 313, 'sigma':1, 'amplitude':20000}},
#                           {'type': 'LorentzianModel',
#                           'params': {'center': 338, 'sigma':3, 'amplitude':30000}},
#                           {'type': 'LorentzianModel',
#                           'params': {'center': 384, 'sigma':1,'amplitude':80000}},
#                           {'type': 'LorentzianModel',
#                           'params': {'center': 391, 'sigma':1, 'amplitude':80000}},
#                           {'type': 'LorentzianModel',
#                           'params': {'center': 429, 'sigma':1, 'amplitude':180000}},
#                           {'type': 'LorentzianModel',
#                           'params': {'center': 465, 'sigma':1, 'amplitude':20000}}]
#             }
#     #peaks_found = update_spec_from_peaks(spec, [0,1,2,3,4,5,6,7,8,9,10,11], peak_widths=(15,))
#     model, params = generate_model(spec)
#     output = model.fit(spec['y'], params, x=spec['x'])
#     #components = output.eval_components(x=spec['x'])
#     fig, gridspec = output.plot(data_kws={'markersize':  1})
#     plt.show()
#     print_best_values(spec,output)

# data = np.loadtxt('ferricfluoride.txt')
# x = data[:,0][:-1]
# y = -data[:,1][:-1]+np.max(data[:,1])

# Fit_Lorentzian(x,y)


