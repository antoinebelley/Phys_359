import numpy as np
import matplotlib.pyplot as plt

N0 = 5
lam_pb = np.log(2)/38304
lam_bi = np.log(2)/3636

def A2(t):
	A2 = N0*lam_bi*lam_pb*(np.exp(-lam_pb*t)-np.exp(-lam_bi*t))
	A2 /= lam_bi-lam_pb
	return A2

t = np.linspace(0,200000, 10000)

plt.plot(t,A2(t))
plt.xlabel("t")
plt.ylabel('A2')
plt.show()