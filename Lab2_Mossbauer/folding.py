import numpy as np 
import matplotlib.pyplot as plt


# import the peak values for the Fe57 assuming csv format
peaks_errors = np.loadtxt('iron_Loc.txt', delimiter=',')

peaks  = peaks_errors[:,0]
errors = peaks_errors[:,1]

# for each peak (pair) get the associated center
middles = np.zeros(6)
for i in range(6):
	middles[i] = 0.5*(peaks[i]+peaks[-(i+1)])

#compute the mean and error
middle = np.mean(middles)
middle_err = np.std(middles)

print('The middle channel for folding is at ', middle, ' with error ', middle_err, '\n')

#fold the data

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

	# add up
	new_strain = data_1 + data_2


	return channels, new_strain

filename = 'stainlesssteel.txt'
x,y = fold_strain(filename)

plt.clf()
plt.plot(x,y)
plt.show()

new_data = np.array([x,y]).transpose()

output = 'folded_data_'+filename
print(output)
#save the data
np.savetxt(output, new_data, delimiter=',')






