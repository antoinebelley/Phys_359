import numpy as np 
from matplotlib import pyplot as plt 
from Energy_to_velocity import fit
import matplotlib.gridspec as gridspec
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,AutoMinorLocator)
data=np.loadtxt('True_folded_data_FeNH3liquid.txt',delimiter=',')
x=data[:,0][:-2]
x=fit(x)
y=data[:,1][:-2]
yerr = np.sqrt(y)

err_x = np.sqrt((6e-5*x)**2 +0.009**2)

fig = plt.figure(figsize=(9.5,9.5))
gs = gridspec.GridSpec(ncols=1, nrows=3, figure=fig, wspace=0)
ax1 = fig.add_subplot(gs[0:2, :])
ax1.errorbar(x,y,yerr=yerr,xerr=err_x, fmt='none', label ='Data')
#ax1.plot(x_arr, fit, linewidth=0.8, label='Best fit')
ax1.set_ylabel('Counts', size = 24)
ax1.set_xlabel('Velocity (mm/s)', size = 24)
ax1.tick_params(axis="y", labelsize=22 )
ax1.tick_params(axis='both', direction='in', length=10)
ax1.tick_params(which='minor',axis='both', direction='in', length=5)
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.yaxis.set_minor_locator(AutoMinorLocator())
#ax1.legend(loc=4, prop={'size': 20})
plt.show()