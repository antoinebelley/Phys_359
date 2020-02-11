import numpy as np 
import matplotlib.pyplot as plt

peak_found = [66.491, 92.886, 119.479, 139.362, 165.966, 192.643]
peak_real  = [-5.4823, -3.2473, -1.0132, 0.6624, 2.8967, 5.1338]

p = np.polyfit(peak_real,peak_found,deg=1)

x =np.linspace(peak_real[0], peak_real[-1], 100)
fit_tot = np.polyval(p,x)

plt.plot(x, fit_tot)
plt.scatter(peak_real,peak_found)
plt.show()


fit = np.polyval(p,peak_real)
plt.scatter(peak_real, fit-peak_found)
plt.show()