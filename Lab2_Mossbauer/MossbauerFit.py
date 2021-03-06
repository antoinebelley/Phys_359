import numpy as np
import matplotlib.pyplot as plt

#Defines conestant that will be used:
cc = 299792458*1e3
g = 0.18088
ub = 3.152451e-11
#g2=0.18088/1.752

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

# class MossbauerModel:

# 	def __init__(self, isomershift= True, quad = False, Zeeman=False):
# 		self.Es  = 14.4e3
# 		self.mod = self.model(isomershift = isomershift, quad = quad, Zeeman = Zeeman)
		

# 	def quadrupole_split(self, QV, n=0):
# 		EQ = QV/2*np.sqrt(1+n**2/3)
# 		return self.convert_E_to_v(EQ) 

# 	def isomer_shift(self, Ea):
# 		return self.convert_E_to_v(Ea)

# 	def convert_E_to_v(self, E):
# 		return c*(E - self.Es)/self.Es

# 	def model(self,isomershift = True, quad = False, Zeeman = False):
# 		if isomershift == True and quad == False and Zeeman == False:
# 			def model(x,sf,c, Ea, A):
# 				shift = self.isomer_shift(Ea)
# 				return Lorentzian(x, -shift, sf,A)+c
# 		elif isomershift == True and quad == True and Zeeman == False:
# 			def model(x,sf,c, Ea, QV, A):
# 				shift = self.isomer_shift(Ea)
# 				EQ = self.quadrupole_split(QV)
# 				return Lorentzian(x, -shift-EQ, sf,A)+Lorentzian(x, -shift+EQ, sf,A)+c
# 		elif isomershift == True and quad == False and Zeeman == True:
# 			def model(x,sf,c,Ea,g2,B,A1,A2,A3):
# 				shift = self.isomer_shift(Ea)
# 				mod = 0
# 				zeeman = (g2*-3/2 - g*-1/2)*ub*B+self.Es
# 				zeeman = self.convert_E_to_v(zeeman)
# 				mod += Lorentzian(x, (-shift+zeeman), sf, A1)
# 				zeeman = (g2*-1/2 - g*-1/2)*ub*B+self.Es
# 				zeeman = self.convert_E_to_v(zeeman)
# 				mod += Lorentzian(x, (-shift+zeeman), sf, A2)
# 				zeeman = (g2*1/2 - g*-1/2)*ub*B+self.Es
# 				zeeman = self.convert_E_to_v(zeeman)
# 				mod += Lorentzian(x, (-shift+zeeman), sf, A3)
# 				zeeman = (g2*-1/2 - g*1/2)*ub*B+self.Es
# 				zeeman = self.convert_E_to_v(zeeman)
# 				mod += Lorentzian(x, (-shift+zeeman), sf, A3)
# 				zeeman = (g2*1/2 - g*1/2)*ub*B+self.Es
# 				zeeman = self.convert_E_to_v(zeeman)
# 				mod += Lorentzian(x, (-shift+zeeman), sf, A2)
# 				zeeman = (g2*3/2 - g*1/2)*ub*B+self.Es
# 				zeeman = self.convert_E_to_v(zeeman)
# 				mod += Lorentzian(x, (-shift+zeeman), sf, A1)

# 				return mod+c

# 		elif isomershift == True and quad == True and Zeeman == True:
# 			def model(x,sf,c,Ea,g2,B,QV,A1,A2,A3):
# 				shift = self.isomer_shift(Ea)
# 				quadshift = self.quadrupole_split(QV)
# 				mod = 0
# 				zeeman = (g2*-3/2 - g*-1/2)*ub*B+self.Es
# 				zeeman = self.convert_E_to_v(zeeman)
# 				mod += Lorentzian(x, (-shift+zeeman+quadshift), sf, A1)
# 				zeeman = (g2*-1/2 - g*-1/2)*ub*B+self.Es
# 				zeeman = self.convert_E_to_v(zeeman)
# 				mod += Lorentzian(x, (-shift+zeeman+quadshift), sf, A2)
# 				zeeman = (g2*1/2 - g*-1/2)*ub*B+self.Es
# 				zeeman = self.convert_E_to_v(zeeman)
# 				mod += Lorentzian(x, (-shift+zeeman+quadshift), sf, A3)
# 				zeeman = (g2*-1/2 - g*1/2)*ub*B+self.Es
# 				zeeman = self.convert_E_to_v(zeeman)
# 				mod += Lorentzian(x, (-shift+zeeman-quadshift), sf, A3)
# 				zeeman = (g2*1/2 - g*1/2)*ub*B+self.Es
# 				zeeman = self.convert_E_to_v(zeeman)
# 				mod += Lorentzian(x, (-shift+zeeman-quadshift), sf, A2)
# 				zeeman = (g2*3/2 - g*1/2)*ub*B+self.Es
# 				zeeman = self.convert_E_to_v(zeeman)
# 				mod += Lorentzian(x, (-shift+zeeman-quadshift), sf, A1)

# 				return mod+c

# 		return model



class MossbauerModel:

	def __init__(self, isomershift= True, quad = False, Zeeman=False, quad_angle = False):
		self.Es  = 14.4
		self.mod = self.model(isomershift = isomershift, quad = quad, Zeeman = Zeeman, quad_angle = quad_angle)
		

	def quadrupole_split(self, QV, n=0):
		#EQ = QV/2*np.sqrt(1+n**2/3)
		EQ=QV/2
		return self.convert_E_to_v(EQ) 

	def quadrupole_angle(self, QV, theta, n=0):
		EQ = QV/2*np.sqrt(1+n**2/3)
		# we compute the ratio of the peaks due to the angle
		ratio = (1 + (np.cos(theta))**2)/((2/3) + (np.sin(theta))**2)
		return ratio, self.convert_E_to_v(EQ)


	def isomer_shift(self, Ea):
		return self.convert_E_to_v(Ea)

	def convert_E_to_v(self, E):
		return cc*(E - self.Es)/self.Es



	def model(self,isomershift = True, quad = False, Zeeman = False, quad_angle = False):
		if isomershift == True and quad == False and Zeeman == False and quad_angle == False:

			def model(x,sf,c, Ea, A):
				shift = self.isomer_shift(Ea)
				return Lorentzian(x, -shift, sf,A)+c
		elif isomershift == True and quad == True and Zeeman == False and quad_angle == False:
			def model(x,sf,c, Ea, QV, A):
				shift = self.isomer_shift(Ea)
				#print(shift)
				EQ = self.quadrupole_split(QV)
				#print(EQ)
				return Lorentzian(x, -shift-EQ, sf,A)+Lorentzian(x, -shift+EQ, sf,A)+c

		elif isomershift == True and quad == False and Zeeman == False and quad_angle == True:
			def model(x,sf,c,Ea,QV,angle,A):
				shift = self.isomer_shift(Ea)
				ratio, EQ = self.quadrupole_angle(QV, angle)
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
				zeeman1 = cc*(g2*-3/2 - g*-1/2)*ub*B/self.Es

				#zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman1+quadshift), sf, A1)
				zeeman2 = cc*(g2*-1/2 - g*-1/2)*ub*B/self.Es
				#zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman2+quadshift), sf, A2)
				zeeman3 = cc*(g2*1/2 - g*-1/2)*ub*B/self.Es
				#zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman3+quadshift), sf, A3)
				zeeman4 = cc*(g2*-1/2 - g*1/2)*ub*B/self.Es
				#zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman4-quadshift), sf, A3)
				zeeman5 = cc*(g2*1/2 - g*1/2)*ub*B/self.Es
				#zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman5-quadshift), sf, A2)
				zeeman6 = cc*(g2*3/2 - g*1/2)*ub*B/self.Es
				#zeeman = self.convert_E_to_v(zeeman)
				mod += Lorentzian(x, (-shift+zeeman6-quadshift), sf, A1)

				return mod+c

		return model




'''x = np.linspace(-100,100,1000000)
func = MossbauerModel(quad=True).mod

y = func(x,0.1,0,1.44e4, 1.4400001e4, 1e3)
plt.plot(x,y)
plt.show()'''



# x = np.linspace(-100,100,1000000)
# func = MossbauerModel(Zeeman=True, quad=True).mod


# y = func(x, 0.2, 5.25e6, 14399.999991, 28800.00000011, 0.4, 12500)
# plt.plot(x,y)
# plt.show()






