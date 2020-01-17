from util import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)


#Import the data and put it in the right unit for the interpolation
data = np.loadtxt('Data/CalibrationPowerSupply/0801_1663_PSCalibraiton.csv', delimiter=',', skiprows=1)
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


def fit_B_field(B):
    """Compute the least-square fit of the B-field and computes the error on the fit 
    using the covariance matrix"""
    p, cov = np.polyfit(V_PS, B,1, cov=True)
    cov_err = [np.sqrt(cov[0,0]), np.sqrt(cov[1,1])]
    p_min = p - cov_err
    p_max = p + cov_err
    return [p, p_min, p_max]

def convert_V_to_B(V_HP,V_PS, bound=None, fit = True):
    """Convert the voltage in B-field using the interpolation of the values given in
    the appendix table. Procede to a linear fit of the data for the both the upper and lower limits
    on the B-field as well as the data."""
    #Use the interpolation to find the B-field for the given voltage
    #Define upper and lower bound on the B-field
    B, err = interpolation_hall_probe(V_HP)
    if bound==None:
        p = fit_B_field(B)[0]
    elif bound == 'lower':
        B = B-err
        p = fit_B_field(B)[1]
    elif bound == 'upper':
        B = B+err
        p = fit_B_field(B)[2]
    else:
        print('This bound doesn\'t exist...')
        print('Choose between "lower" or "upper" or leave empty to perform on the measured points!')
        print('Exiting...')
        exit(1)

    if fit == True:
        fit = np.polyval(p,V_PS)
    model = lambda V: np.polyval(p,V)
    return B, fit, model



B, fit, model   = convert_V_to_B(V_HP, V_PS)
B_min, fit_min, model_min  = convert_V_to_B(V_HP_min, V_PS, bound='lower')
B_max, fit_max, model_max = convert_V_to_B(V_HP_max, V_PS, bound='upper')

#print(model(20), model(20)-model_min(19.9), model_max(20.1)-model(20))

fig = plt.figure(figsize=(9.5,9.5))
gs = gridspec.GridSpec(ncols=1, nrows=3, figure=fig, wspace=0)
ax1 = fig.add_subplot(gs[0:2, :])
ax2 = fig.add_subplot(gs[2, :])
gs.update(wspace=0.05, hspace=0.05)

ax1.fill_between(V_PS,fit_min, fit_max, color='gray', alpha=0.7, label='Error on linear fit')
ax1.errorbar(V_PS, B,xerr=0.1, yerr=[B-B_min,B_max-B], label='Measured B_field', fmt='.')
ax1.plot(V_PS, fit, linewidth=0.8, label='Best linear fit', color='r')
ax1.set_ylabel('B-Field measured by \n the Hall Probe (T)', size = 22)
ax1.tick_params(axis="y", labelsize=20 )
ax1.tick_params(axis='both', direction='in', length=10)
ax1.tick_params(which='minor',axis='both', direction='in', length=5)
plt.setp(ax1.get_xticklabels(), visible=False)
ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.yaxis.set_minor_locator(AutoMinorLocator())
ax1.set_xticks([0,10,20,30,40,50,60])
ax1.legend(loc=4, prop={'size': 18})


# ax2.plot(V_PS,fit_true-B_true,'.', label='Residuals', markersize=10)
ax2.errorbar(V_PS, fit-B, yerr=[B-B_min,B_max-B],xerr=0.1, label='Residuals', fmt='.')
ax2.axhline(color='k', linewidth=0.5)
ax2.tick_params(axis="both", labelsize=20)
ax2.tick_params(axis='both', direction='in', length=10)
ax2.tick_params(which='minor',axis='both', direction='in', length=5)
ax2.set_xticklabels(['0.0','10.0','20.0','30.0','40.0','50.0', '60.0'])
ax2.set_xticks([0,10,20,30,40,50,60])
ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax2.set_xlabel('Voltage of the power supply (mV)', size = 22)
ax2.legend( prop={'size': 18})
#plt.savefig('Power_Supply_Calibraiton.png',bbox_inches='tight')
#plt.show()

print(len(V_PS))
chi_squared = 0
for i in range(len(B)):
    chi_squared+=(fit[i]-B[i])**2/B[i]
print(chi_squared)
