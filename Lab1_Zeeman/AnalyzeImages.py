from crosscorrelation import ImageAnalyse
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import numpy as np


def Plot1Image(image):
    im = ImageAnalyse(f'Pictures/JPEG_29Jan/IMG_{image}.JPG')
    im.find_circle_center(r=155)
    fit_y = im.find_split(5)
    im.plot_fig()
    plt.clf()
    with open(f'Results/IMG_{image}.csv', 'w', newline='') as file:
        file.write(f'{fit_y}')
    plt.clf()
    x = np.arange(im.y0-1600,im.y0-700)
    fig = plt.figure(figsize=(9.5,9.5))
    gs = gridspec.GridSpec(ncols=1, nrows=3, figure=fig, wspace=0)
    ax1 = fig.add_subplot(gs[0:2, :])
    ax2 = fig.add_subplot(gs[2, :])
    gs.update(wspace=0.05, hspace=0.05)
    ax1.errorbar(x,im.line_profile_y[im.y0-1600:im.y0-700],yerr=0.6,fmt='.', label='Data')
    fit_total = 0
    color = next(ax1._get_lines.prop_cycler)['color']
    ax1.plot(im.spec_y['x'], im.components_y[f'm{0}_'],color=color, label='Fitted Gaussians')
    for i, model in enumerate(im.spec_y['model']):
        ax1.plot(im.spec_y['x'], im.components_y[f'm{i}_'],color=color)
        fit_total += im.components_y[f'm{i}_']
    ax1.plot(x, fit_total, label='Total fit of the curve')
    ax1.set_ylabel('Intenstity', size=22)
    ax1.tick_params(axis="y", labelsize=18 )
    ax1.tick_params(axis='both', direction='in', length=10)
    ax1.tick_params(which='minor',axis='both', direction='in', length=5)
    plt.setp(ax1.get_xticklabels(), visible=False)
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    ax1.legend(prop={'size': 18})

    residuals = (im.line_profile_y[im.y0-1600:im.y0-700]-fit_total)
    ax2.errorbar(x,residuals,yerr=0.6,fmt='.', label='Residuals')
    ax2.axhline(color='k', linewidth=0.5)
    ax2.tick_params(axis="both", labelsize=18)
    ax2.tick_params(axis='both', direction='in', length=10)
    ax2.tick_params(which='minor',axis='both', direction='in', length=5)
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.yaxis.set_minor_locator(AutoMinorLocator())
    ax2.legend( prop={'size': 18})

    ax2.set_xlabel('y-position of pixels along \n vertical line profile throuh the center', size=22)
    plt.gcf()
    plt.savefig(f'Results/IMG_{image}.png')
files = [4442]
for image in files:
    Plot1Image(image)


