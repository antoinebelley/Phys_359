import numpy as np
from matplotlib import pyplot as plt

a=np.loadtxt('True_folded_data_YFeO3_room_temperature18C.txt', delimiter=',')
b =np.loadtxt('True_folded_data_YFeO3_208c.txt', delimiter=',')
c=np.loadtxt('True_folded_data_YFeO3_250c.txt', delimiter=',')
d=np.loadtxt('True_folded_data_YFeO3_300c.txt', delimiter=',')
e=np.loadtxt('True_folded_data_YFeO3_379c.txt', delimiter=',')

a=a[:,1][:-1]
b=b[:,1][:-1]
c=c[:,1][:-1]
d=d[:,1][:-1]
e=e[:,1][:-1]

x=[18,208,250,300,379]
y=[(np.max(a)-np.min(a))/np.mean(a),(np.max(b)-np.min(b))/np.mean(b),(np.max(c)-np.min(c))/np.mean(c),(np.max(d)-np.min(d))/np.mean(d),(np.max(e)-np.min(e))/np.mean(e)]

plt.plot(x,y,'o')
plt.show()
