import numpy as np
import matplotlib.pyplot as plt

#Defines conestant that will be used:
c = 3e8
g = 2
ub = 5.7883818012e-5


def PeakIntensity(x, u,sf, n = 0):
	"""Instensity of a peaks of mossbauer spectrum according to equation 9 of
	  https://onlinelibrary.wiley.com/doi/epdf/10.1002/pssb.19650090314. 
	  x correpsonds to omega, u to delta and sf to Omega."""
	fac = 2*sf/(1-n)
	up = (x**2*n**2-u**2)
	down = (x**2-u**2)**2+4*sf**2/(1-n)**2*(x+u*n)**2
	return fac*up/down


def Lorentzian(x, u ,sig):
	return -sig*2/((x-u)**2+sig**2)

class MossbauerModel:

	def __init__(self, Ea=0, Q=0, V=0, Beff=0,  ml = [], isomershift= True, quad = False, Zeeman=False):
		self.Es  = 14.4e3
		self.Q = Q
		self.V = V
		self.Beff = Beff
		self.Ea = Ea
		self. ml = ml
		self.mod = self.model(isomershift = isomershift, quad = quad, Zeeman = Zeeman)
		

	def quadrupole_split(self, Q, V, n=0):
		EQ = Q*V/2*np.sqrt(1+n**2/3)
		return self.convert_E_to_v(EQ) 

	def isomer_shift(self, Ea):
		return self.convert_E_to_v(Ea)

	def zeeman_speed_one_peak(self, ml, Beff):
		return self.convert_E_to_v(-g*ub*Beff*ml)

	def convert_E_to_v(self, E):
		return c*(self.Es - E)/E

	def model(self, isomershift = True, quad = False, Zeeman = False):
		if isomershift == True and quad == False and Zeeman == False:
			shift = self.isomer_shift(self.Ea)
			model = lambda x,u,sf : Lorentzian(x, (u-shift), sf)
		elif isomershift == True and quad == True and Zeeman == False:
			shift = self.isomer_shift(self.Ea)
			EQ = self.quadrupole_split(self.Q, self.V)
			print(EQ,shift)
			model = lambda x,u,sf : Lorentzian(x, (u-shift-EQ), sf)+Lorentzian(x, (u-shift+EQ), sf)
		elif isomershift == True and quad == True and Zeeman == True:
			for i in self.ml:

		return model



x = np.linspace(-5,5,10000)
func = MossbauerModel(Ea=14.4000001e3, Q=1, V=28.80000002e3,ml=[1/2] quad=True).mod

y = func(x,0,0.01)
plt.plot(x,y)
plt.show()





