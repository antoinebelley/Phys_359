import numpy as np
import matplotlib.pyplot as plt
from Energy_to_velocity import fit
from MossbauerFit import MossbauerModel
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

data = np.loadtxt('folded_data_ferricfluoride.txt', delimiter=',')

x = fit(data[:,0][1:])
y = data[:,1][1:]
yerr = np.sqrt(y)
err_x = np.sqrt((6e-5*x)**2 +0.009**2)

p0=[0.2,np.max(y),14400.000035,(0.18088)/(-1.752), 40000,2.88e4,  2.879999997e4, 6e3,6e3,2e3, 3e4]

func = MossbauerModel(Zeeman=True, quad=True).mod
func2 = MossbauerModel(quad=True).mod

def new_func(x_arr, sf, c, is1, g2,B1, qs1, qs2, a1,a2,a3,a4):
	return (func(x_arr, sf,c, is1,g2,B1,qs1,a1,a2,a3)+func2(x_arr,sf,c,is1,qs2,a4))/2
	

p,pcov = curve_fit(new_func,x,y, p0=p0, bounds=([0,2.6e6,14400.00002,-1,39000,2.879999e4, 2.879999e4,1e3,1e3,1e3, 2.7e4],[0.2, 2.7e6, 14400.00008,0,50000, 2.880000001e4,2.8800001e4,1e4, 1e4,1e4, np.inf]), sigma = yerr)
for i in range(len(p)):
	print(p[i], np.sqrt(pcov[i,i]))
x_arr = np.linspace(-10,10,10000000)
# plt.plot(x,y)
# plt.plot(x_arr,(func(x_arr,0.2,np.max(y), 14400.000035,(0.18088)/(-1.752), 40000,2.88e4, 6e3, 6e3, 2e3)+func2(x_arr,0.2,np.max(y), 14400.000035, 2.879999997e4, 3e4))/2)
# plt.show()

fit = new_func(x_arr,p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10])
fit_point = new_func(x,p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9],p[10])
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
plt.savefig('Fit_fluoride.png',bbox_inches='tight')