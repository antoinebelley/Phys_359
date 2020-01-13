import pandas as pd
from util import *

#Import the data using pandas
df = pd.read_csv('Line_Profile_Ray_0.0.txt', sep="\t", header=None)
df.columns = ["pixel","intensity"]

#Create the profile that I want to fit
spec = {
    'x': df['pixel'].values[500:1500],
    'y': df['intensity'].values[500:1500],
    'model': [
        {'type': 'GaussianModel',
        'params': {'center': 600, 'height': 1.14, 'sigma': 3},
        'help': {'center': {'min': 598, 'max': 602}}},
        {'type': 'GaussianModel',
        'params': {'center': 652, 'height': 3.55, 'sigma': 3},
        'help': {'center': {'min': 645, 'max': 669}}},
        {'type' : 'GaussianModel',
        'params':{'center': 652, 'height': 3.55, 'sigma': 3},
        'help': {'center': {'min': 645, 'max': 669}}},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
        {'type': 'GaussianModel'},
    ]
}
update_spec_from_peaks(spec, [0,1,2,3,4,5,6,7,8,9,10,11,12], peak_widths=(10, 25))
model, params = generate_model(spec)
print(params)
output = model.fit(spec['y'], params, x=spec['x'])
fig, gridspec = output.plot(data_kws={'markersize':  1})
plt.show(fig)


fig, ax = plt.subplots()
ax.scatter(spec['x'], spec['y'], s=4)
components = output.eval_components(x=spec['x'])
print(len(spec['model']))
for i, model in enumerate(spec['model']):
    ax.plot(spec['x'], components[f'm{i}_'])
plt.show(fig)