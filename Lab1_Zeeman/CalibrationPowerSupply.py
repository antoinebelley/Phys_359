import numpy as np
from matplotlib import pyplot as plt
import glob

datastr=glob.glob('Data/CalibrationPowerSupply/*.csv')
xdata=[]
ydata=[]
for i in range(len(datastr)):
	data=np.loadtxt(datastr[i], skiprows=1, delimiter=',')
	x=data[:,0]
	y=data[:,1]
	xdata.extend(x)
	ydata.extend(y)

datafit,res=np.polyfit(xdata,ydata,1,cov=True)
err=np.sum(np.sqrt(np.diag(res)))
fig,(ax1, ax2)= plt.subplots(2)
ax1.plot(xdata,ydata,'o')
ax1.plot(xdata,np.polyval(datafit,xdata))
ax2.plot(xdata,ydata-np.polyval(datafit,xdata),'o')
ax2.hlines(0,0,100)


