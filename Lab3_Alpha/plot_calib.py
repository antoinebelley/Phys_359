import numpy as np 
import matplotlib.pyplot as plt 

data = np.loadtxt('calibration_pulse.txt', delimiter=',',skiprows=1)

pulse_h = data[:-3,0]
channel = data[:-3,1]

p = np.polyfit(pulse_h, channel,1)
fit = np.polyval(p, pulse_h)
chisq = np.sum((channel-fit)**2/(len(channel)-2))
print(chisq)

plt.plot(pulse_h, channel, '.')
plt.plot(pulse_h, fit)
plt.xlabel('pulse height')
plt.ylabel('channel nb.')
plt.show()
#plt.savefig('calibration_v1.png')