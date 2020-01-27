import numpy as np
from matplotlib import pyplot as plt

def err(B,errB,dist,h,c,t): #add herr and cerr as params eventually
	#We retrieve the error on the distance
	disterr=dist[:,2]
	#We retrieve the distance
	rsq=dist[:,1]**2
	#we propagate the error on r^2
	rsqerr=4*rsq*disterr**2


	delta=0
	deltaerr=0
	for i in range(4):
		delta+=rsq[2*i]-rsq[2*i+1]
		deltaerr+=rsqerr[2*i]-rsqerr[2*i+1] #this is the variance squared
	delta*=0.25
	

	triangle=0
	triangleerr=0
	for i in range(2):
		triangle+=rsq[4*i+2]-rsq[4*i]+rsq[4*i+3]-rsq[4*i+1]
		triangleerr+=rsqerr[4*i+2]-rsqerr[4*i]+rsqerr[4*i+3]-rsqerr[4*i+1] #this is the variance squared

	triangle*=0.25

	delV=delta/(2*t*triangle)
	delVerr=deltaerr/((2*t*triangle)**2)+((delta/(2*t*triangle**2))**2)*triangleerr
	magneton=h*c*0.5*delV/B
	magnetonerr=((h*c*delV/(2*B**2))**2)*errB**2
	magnetonerr+=((h*c/(2*B))**2)*delVerr
	#Add uncertainties caused by c&h
	#magnetonerr+=((c*delV/(2*B))**2)*herr**2
	#magnetonerr+=((h*delV/(2*B))**2)*cerr**2
	magnetonerr=np.sqrt(magnetonerr)
	return magneton, magnetonerr

c=299792458
h=1.054571726*10**(-34)
dist=np.array([[ 511.17044696,277.43629086,9.22613738],
[ 884.29486324,621.55103402,13.0627208 ],
[ 884.29486324,621.55103402,13.0627208 ],
[1046.34889927,838.62341561,16.18934633],
[1046.34889927,838.62341561,16.18934633],
[1225.40860574,1008.68012008,24.23038232],
[1225.40860574,1008.68012008,24.23038232],
[1502.50100067,1222.751501,43.61494066]]) 
t=0.004
B=0.193
errB=0.001

magneton, magnetonerr=err(B,errB,dist,h,c,t)
print(magneton)
print(magnetonerr)

