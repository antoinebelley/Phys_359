import numpy as np
from scipy.optimize import curve_fit
from MossbauerFit import MossbauerModel
import matplotlib.pyplot as plt 

data = np.loadtxt('folded_data_Ironfoil0207.txt', delimiter=',')

x = data[:,0][1:]
y = data[:,1][1:]


p0=[128,0.5,np.max(y), 1.44e+04,2.88e+04, 8e5, 2e6, 2e6, 2e6]

func = MossbauerModel(Zeeman=True, quad=True).mod

p,pcov = curve_fit(func,x,y, p0=p0, bounds=([120,0,1.41e6,1.43e4,2.87e4,1e5,1e4,1e4,1e4],[130,2, 1.43e6, np.inf,np.inf,np.inf,5e7,5e7,5e7]))
x_arr = np.linspace(x[0],x[-1],10000000)


print(p)
plt.plot(x_arr,func(x_arr,p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8]))
plt.plot(x,y,"*")
plt.show()