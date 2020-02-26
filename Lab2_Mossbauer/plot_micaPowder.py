import numpy as np
import matplotlib.pyplot as plt
from Energy_to_velocity import fit
from MossbauerFit import MossbauerModel
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

data = np.loadtxt('folded_data_mica0212.txt', delimiter=',')

x = fit(data[:,0][1:])
y = np.flip(data[:,1][1:])
yerr = np.sqrt(y)
err_x = np.sqrt((6e-5*x)**2 +0.009**2)


# plt.plot(x,y)
# plt.show()
# exit(1)

# flat line background level
flat = np.max(y)

p0=[0.15, flat, 30000, -100000, 0, 12500]

func = MossbauerModel(Zeeman=False, quad=False, quad_angle=True).mod

p,pcov = curve_fit(func,x,y, p0=p0, bounds=([0, flat-5000,1000,-200000, -np.pi/4, 0],[0.4, flat+5000, 35000, 200000, np.pi/2, 15000]), sigma = yerr)
for i in range(len(p)):
	print(p[i], np.sqrt(pcov[i,i]))
x_arr = np.linspace(-10,10,10000000)

# plt.plot(x_arr,func(x_arr,0.1,np.max(y), 1.44e+04,(0.18088)/(-1.752), 33000, 1e2, 50, 20))
# plt.plot(x_arr,func(x_arr,p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7]))
# plt.show()

fit = func(x_arr,p[0],p[1],p[2],p[3], p[4], p[5])
fit_point = func(x,p[0],p[1],p[2],p[3], p[4], p[5])
res = (y-fit_point)
chi_squared = np.sum(res**2/yerr**2)/(len(x)-8)
print(chi_squared)


fig = plt.figure(figsize=(9.5,9.5))
gs = gridspec.GridSpec(ncols=1, nrows=3, figure=fig, wspace=0)
ax1 = fig.add_subplot(gs[0:2, :])
ax2 = fig.add_subplot(gs[2, :])
gs.update(wspace=0.05, hspace=0.05)

ax1.errorbar(x,y,yerr=yerr,xerr=err_x, fmt='none', label ='Data')
ax1.plot(x_arr, fit, linewidth=0.8, label='Best fit')
ax1.set_ylabel('Counts', size = 24)
ax1.tick_params(axis="y", labelsize=22 )
ax1.tick_params(axis='both', direction='in', length=10)
ax1.tick_params(which='minor',axis='both', direction='in', length=5)
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.yaxis.set_minor_locator(AutoMinorLocator())
ax1.legend(loc=4, prop={'size': 20})


# ax2.plot(V_PS,fit_true-B_true,'.', label='Residuals', markersize=10)
ax2.errorbar(x, res, yerr=yerr, fmt='none', label="Residuals")
ax2.axhline(color='k', linewidth=0.5)
ax2.tick_params(axis="both", labelsize=22)
ax2.tick_params(axis='both', direction='in', length=10)
ax2.tick_params(which='minor',axis='both', direction='in', length=5)
ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax2.set_xlabel('Velocity (mm/s)', size = 24)
ax2.set_ylabel('Data-Fit (Counts)', size = 24)
ax2.legend( prop={'size': 20})
#plt.show()
plt.savefig('Fit_micaPowder.png',bbox_inches='tight')