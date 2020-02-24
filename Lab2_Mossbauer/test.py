import numpy as np
import matplotlib.pyplot as plt
from Energy_to_velocity import fit
from MossbauerFit import MossbauerModel
from scipy.optimize import curve_fit
import matplotlib.gridspec as gridspec
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

data = np.loadtxt('hematite0221.txt', delimiter=' ')

x = fit(data[:,0][1:])
y = data[:,1][1:]
yerr = np.sqrt(y)

plt.plot(x,y)
plt.show()

def fold_strain(filename, middle = 256):
	# read the data
	data = np.loadtxt(filename)
	
	channels = data[:,0][:middle]
	data = data[:,1][:]

	# split the strain in the middle
	data_1 = data[:middle]
	data_2 = data[middle:]
	

	#flip the second half
	data_2 = np.flip(data_2)
	plt.clf()
	plt.plot(data_1)
	plt.plot(data_2)
	plt.show()
	# add up
	new_strain = data_2


	return channels, new_strain

filename = 'hematite0221.txt'
x,y = fold_strain(filename)

# plt.clf()
# plt.plot(x,y)
# plt.show()


# new_data = np.array([x,y]).transpose()

# output = 'folded_data_'+filename
# print(output)
#save the data
# np.savetxt(output, new_data, delimiter=',')