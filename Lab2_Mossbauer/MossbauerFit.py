import numpy as np
import matplotlib.pyplot as plt

#Defines conestant that will be used:
c = 3e8
g = 0.18088
ub = 3.152451e-8


def PeakIntensity(x, u, sf, n = 0):
	"""Instensity of a peaks of mossbauer spectrum according to equation 9 of
	  https://onlinelibrary.wiley.com/doi/epdf/10.1002/pssb.19650090314. 
	  x correpsonds to omega, u to delta and sf to Omega."""
	fac = 2*sf/(1-n)
	up = (x**2*n**2-u**2)
	down = (x**2-u**2)**2+4*sf**2/(1-n)**2*(x+u*n)**2
	return fac*up/down


def Lorentzian(x, u ,sig,A):
	return -sig*2*A/((x-u)**2+sig**2)

class MossbauerModel:

	def __init__(self, isomershift= True, quad = False, Zeeman=False, quad_angle = False):
		self.Es  = 14.4e3
		self.mod = self.model(isomershift = isomershift, quad = quad, Zeeman = Zeeman, quad_angle = quad_angle)
		

	def quadrupole_split(self, QV, n=0):
		EQ = QV/2*np.sqrt(1+n**2/3)
		return self.convert_E_to_v(EQ) 

	def quadrupole_angle(self, QV, theta, n=0):
		EQ = QV/2*np.sqrt(1+n**2/3)
		# we compute the ratio of the peaks due to the angle
		ratio = (1 + (np.cos(theta))**2)/((2/3) + (np.sin(theta))**2)
		return ratio, self.convert_E_to_v(EQ)


	def isomer_shift(self, Ea):
		return self.convert_E_to_v(Ea)

	def zeeman_speed_one_peak(self, ml, Beff):
		return self.convert_E_to_v(-g*ub*Beff*ml)

	def convert_E_to_v(self, E):
		return c*(E-self.Es)/self.Es

	def model(self,isomershift = True, quad = False, Zeeman = False, quad_angle = False):
		if isomershift == True and quad == False and Zeeman == False and quad_angle == False:
			def model(x,sf,c, Ea, A):
				shift = self.isomer_shift(Ea)
				return Lorentzian(x, -shift, sf,A)+c
		elif isomershift == True and quad == True and Zeeman == False and quad_angle == False:
			def model(x,sf,c, Ea, QV, A):
				shift = self.isomer_shift(Ea)
				print(shift)
				EQ = self.quadrupole_split(QV)
				print(EQ)
				return Lorentzian(x, -shift-EQ, sf,A)+Lorentzian(x, -shift+EQ, sf,A)+c

		elif isomershift == True and quad == False and Zeeman == False and quad_angle == True:
			def model(x,sf,c,Ea,QV,angle,A):
				shift = self.isomer_shift(Ea)
				#print(shift)
				ratio, EQ = self.quadrupole_angle(QV, angle)
				#print(ratio, EQ)
				#print(-shift-EQ, -shift+EQ)
				return Lorentzian(x, -shift-EQ, sf,A)+Lorentzian(x, -shift+EQ, sf,A/ratio)+c


		elif isomershift == True and quad == False and Zeeman == True and quad_angle == False:
			def model(x,sf,c,Ea,g2,B,A1,A2,A3):
				shift = self.isomer_shift(Ea)
				mod = 0
				zeeman = (g2*-3/2 - g*-1/2)*ub*B+self.Es
				zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman), sf, A1)
				zeeman = (g2*-1/2 - g*-1/2)*ub*B+self.Es
				zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman), sf, A2)
				zeeman = (g2*1/2 - g*-1/2)*ub*B+self.Es
				zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman), sf, A3)
				zeeman = (g2*-1/2 - g*1/2)*ub*B+self.Es
				zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman), sf, A3)
				zeeman = (g2*1/2 - g*1/2)*ub*B+self.Es
				zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman), sf, A2)
				zeeman = (g2*3/2 - g*1/2)*ub*B+self.Es
				zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman), sf, A1)

				return mod+c

		elif isomershift == True and quad == True and Zeeman == True and quad_angle == False:
			def model(x,sf,c,Ea,g2,B,QV,A1,A2,A3):
				shift = self.isomer_shift(Ea)
				quadshift = self.quadrupole_split(QV)
				mod = 0
				zeeman = (g2*-3/2 - g*-1/2)*ub*B+self.Es
				zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman+quadshift), sf, A1)
				zeeman = (g2*-1/2 - g*-1/2)*ub*B+self.Es
				zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman+quadshift), sf, A2)
				zeeman = (g2*1/2 - g*-1/2)*ub*B+self.Es
				zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman+quadshift), sf, A3)
				zeeman = (g2*-1/2 - g*1/2)*ub*B+self.Es
				zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman+quadshift), sf, A3)
				zeeman = (g2*1/2 - g*1/2)*ub*B+self.Es
				zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman+quadshift), sf, A2)
				zeeman = (g2*3/2 - g*1/2)*ub*B+self.Es
				zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman+quadshift), sf, A1)

				return mod+c

		return model



# x = np.linspace(-10,10,1000000)
# func = MossbauerModel(Zeeman=False, quad=False, quad_angle=True).mod

# y = func(x, 0.2, 5.25e6, 14399.999991, 28800.00000011, 0.4, 12500)
# plt.plot(x,y)
# plt.show()





