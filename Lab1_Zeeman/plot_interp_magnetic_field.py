from util import *
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('Data/CalibrationHallProbe/EQ3485_Calibration.csv', delimiter=',')
V_True = data[:,0]
B_True = data[:,1]*0.1 

V = np.linspace(0.01,0.37,10000)
B, err = interpolation_hall_probe(V)

B_min = B-err
B_max = B+err
fig = plt.figure(1,(12,10))
plt.plot(V,B, label='Interpolated B-field')
plt.plot(V_True, B_True, '.', label='Measured B-field')
plt.fill_between(V,B_min, B_max, color='gray', alpha=0.5)
#plt.title('Interpolation of the Hall Probe B-field measurement', size = 28)
plt.ylabel('Magnetic Field (T)', size = 22)
plt.xticks(size=16)
plt.yticks(size=16)
plt.xlabel('Voltage (V)', size = 22)
plt.legend( prop={'size': 14})
plt.show()

print(interpolation_hall_probe(0.026))
print(interpolation_hall_probe(0.020))
print(interpolation_hall_probe(0.0899))