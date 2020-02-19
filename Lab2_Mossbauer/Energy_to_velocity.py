import numpy as np 
import matplotlib.pyplot as plt

peak_found = np.array([66.491, 92.886, 119.479, 139.362, 165.966, 192.643])
peak_real  = np.array([-5.4823, -3.2473, -1.0132, 0.6624, 2.8967, 5.1338])
err = np.array([0.0008, 0.0008, 0.0010, 0.0007, 0.0007,0.0010])

p, cov = np.polyfit(peak_found,peak_real,deg=1,w=err, cov = True)



x =np.linspace(peak_found[0], peak_found[-1], 100)

fit = lambda x: np.polyval(p,x)


print(fit(peak_found))


print(np.sum(((fit(peak_found)-peak_real)**2)))