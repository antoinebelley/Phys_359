from util import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import seaborn as sns


#Import the data and put it in the right unit for the interpolation
data = np.loadtxt('Data/CalibrationPowerSupply/2001_1214_PSCalibration.csv', delimiter=',', skiprows=1)
data = np.sort(data, axis=0)
V_PS = data[:,0]
V_HP = data[:,1]*0.001
#Computes the error on the voltage of the Hall Probe
err_V_HP = V_HP*0.003+0.001+0.0005
#Computes the upper and lower bounds for V_HP
V_HP_min = V_HP-err_V_HP
V_HP_max = V_HP+err_V_HP


# #Used for fitting purposes
# x = np.linspace(V_PS[0], V_PS[-1], 10000)


def fit_B_field(B,err):
    """Compute the least-square fit of the B-field and computes the error on the fit 
    using the covariance matrix"""
    p, cov = np.polyfit(V_PS, B,3, cov=True, w=1/err)

    cov_err = np.zeros(len(p))
    for i in range(len(p)):
        cov_err[i] = np.sqrt(cov[i,i])
    print(p)
    print(cov_err)
    return p,cov_err

def B_err(V,V_err,p,cov_err):
    """Compute the error on B by doing the error propagation on the fit"""
    B_err_sq = (p[0]*V**2+p[1]*V+p[2])**2*V_err**2+V**6*cov_err[0]**2+V**4*cov_err[1]**2+V**2*cov_err[2]**2+cov_err[3]**2
    B_err = np.sqrt(B_err_sq)
    return B_err

def convert_V_to_B(V_HP,V_PS, V_min, V_max):
    """Convert the voltage in B-field using the interpolation of the values given in
    the appendix table. Procede to a linear fit of the data for the both the upper and lower limits
    on the B-field as well as the data."""
    #Use the interpolation to find the B-field for the given voltage
    #Define upper and lower bound on the B-field
    B, err = interpolation_hall_probe(V_HP)
    B_min,err_min = interpolation_hall_probe(V_min)
    B_min = B_min-err_min
    B_max,err_max = interpolation_hall_probe(V_max)
    B_max = B_max-err_max
    B_sys_min,err_min = interpolation_hall_probe(V_HP_min-0.0013243447)
    B_sys_min = B_sys_min - err_min
    B_sys_max,err_max = interpolation_hall_probe(V_HP_max+0.0013243447)
    B_sys_max = B_sys_max - err_max

    p,cov_err = fit_B_field(B,B_max-B_min)
    fit_err = B_err(V_PS,0.001,p,cov_err)
    fit = np.polyval(p,V_PS)
    model = lambda V: np.polyval(p,V)
    error = lambda V: B_err(V,0.001,p,cov_err)
    return B,B_min,B_max,B_sys_min, B_sys_max, fit,fit_err,model,error



B,B_min,B_max,B_sys_min, B_sys_max, fit,fit_err,model,error   = convert_V_to_B(V_HP, V_PS, V_HP_min, V_HP_max)

print(model(60.7))
print(error(60.7))



fig = plt.figure(figsize=(9.5,9.5))
gs = gridspec.GridSpec(ncols=1, nrows=3, figure=fig, wspace=0)
ax1 = fig.add_subplot(gs[0:2, :])
ax2 = fig.add_subplot(gs[2, :])
gs.update(wspace=0.05, hspace=0.05)

#ax1.fill_between(V_PS,fit-fit_err,fit+fit_err, color='gray', alpha=0.7, label='Error on linear fit')
ax1.errorbar(V_PS, B,yerr=[B-B_sys_min, B_sys_max-B], label='Error including systematics', fmt='none', color='tab:orange')
ax1.errorbar(V_PS, B,xerr=0.1,yerr=[B-B_min,B_max-B], label='Measured B_field', fmt='.', color='tab:blue')
ax1.plot(V_PS, fit, linewidth=0.8, label='Best linear fit', color='r')
ax1.set_ylabel('B-Field measured by \n the Hall Probe (T)', size = 22)
ax1.tick_params(axis="y", labelsize=20 )
ax1.tick_params(axis='both', direction='in', length=10)
ax1.tick_params(which='minor',axis='both', direction='in', length=5)
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.yaxis.set_minor_locator(AutoMinorLocator())
ax1.set_xticks([0,10,20,30,40,50,60,70,90])
ax1.legend(loc=4, prop={'size': 18})


# ax2.plot(V_PS,fit_true-B_true,'.', label='Residuals', markersize=10)
ax2.errorbar(V_PS, fit-B, yerr=[B-B_sys_min, B_sys_max-B],xerr=0.1, label='Residuals including systematics (T)', fmt='none', color='tab:orange')
ax2.errorbar(V_PS, fit-B, yerr=[B-B_min,B_max-B],xerr=0.1, label='Residuals (T)', fmt='.', color='tab:blue')
print(np.sum((fit-B/B_max-B_min)**2/(len(V_PS)-3)))
ax2.axhline(color='k', linewidth=0.5)
ax2.tick_params(axis="both", labelsize=20)
ax2.tick_params(axis='both', direction='in', length=10)
ax2.tick_params(which='minor',axis='both', direction='in', length=5)
ax2.set_xticklabels(['0.0','10.0','20.0','30.0','40.0','50.0', '60.0','70.0', '80.0', '90.0'])
ax2.set_xticks([0,10,20,30,40,50,60,70,80,90])
ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax2.set_xlabel('Voltage measured on the shunt resistor (mV)', size = 22)
ax2.legend( prop={'size': 18})
plt.savefig('Power_Supply_Calibraiton.png',bbox_inches='tight')
#plt.show()


