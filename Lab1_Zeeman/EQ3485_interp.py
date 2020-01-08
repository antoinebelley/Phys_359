import numpy as np
from scipy import interpolate as interp
from matplotlib import pyplot as plt

#### EQ3485 ######
data=np.loadtxt('EQ3485_Calibration.csv',delimiter=',')
volt=data[:,0]
bfield=data[:,1]*0.1

plt.plot(volt,bfield)
plt.title('EQ3485_Calibration')
plt.xlabel('Voltage (V)')
plt.ylabel('B Field (Tesla)')
plt.savefig('Calibration_of_Hall_Probe.pdf')

