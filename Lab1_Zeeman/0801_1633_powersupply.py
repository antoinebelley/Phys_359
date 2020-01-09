import numpy as np
from scipy import interpolate as interp
from matplotlib import pyplot as plt

#### EQ3485 ######
data=np.loadtxt('Data/CalibrationPowerSupply/0801_1663_PSCalibraiton.csv',delimiter=',', skiprows=1)
volt=data[:,0]
Hall=data[:,1]

plt.clf()
plt.plot(volt,Hall,'o')
plt.title('Calibration of the Power source')
plt.xlabel('Power supply voltage (mV)')
plt.ylabel('Hall probe voltage (mV)')
plt.savefig('0801_1633_Calibration_of_power_source.png')

