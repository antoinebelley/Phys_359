import numpy as np 


h = 6.6260705e-34
c = 299792458


def Error_ub(B,B_err, delta, delta_err, Delta, Delta_err):
	fac = h*c/(4*B*0.004*Delta)
	err_sq = delta_err**2+delta**2*B_err*2/B**2+delta**2*Delta_err**2/Delta**2
	err = fac*np.sqrt(err_sq)
	return err



err_60 = Error_ub(0.499395497592118, 0.028077959566550815, 3.26E+04,1.06E+04,3.25E+05,1.75E+04)
err_89_ab = Error_ub(0.6223406675736655, 0.068219427819598046, 1.38E+05,3.96E+04,4.14E+05,4.91E+04)
err_89_cd = Error_ub(0.6223406675736655, 0.068219427819598046, 1.36E+05,3.69E+04,4.14E+05,4.91E+04)
print(err_60)
print(err_89_ab)
print(err_89_cd)