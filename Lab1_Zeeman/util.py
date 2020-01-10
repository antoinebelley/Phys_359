#This module contains all useful functions for the plotting/scripting required for the analysis of the lab



import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline as spline
import matplotlib.pyplot as plt

class ErrorPropagationSpline(object):
    """
    Does a spline fit, but returns both the spline value and associated uncertainty.
    """
    def __init__(self, x, y, yerr, N=1000, *args, **kwargs):
        """
        See docstring for InterpolatedUnivariateSpline
        """
        yy = np.vstack([y + np.random.normal(loc=0, scale=yerr) for i in range(N)]).T
        self._splines = [spline(x, yy[:, i], *args, **kwargs) for i in range(N)]

    def __call__(self, x, *args, **kwargs):
        """
        Get the spline value and uncertainty at point(s) x. args and kwargs are passed to spline.__call__
        :param x:
        :return: a tuple with the mean value at x and the standard deviation
        """
        x = np.atleast_1d(x)
        s = np.vstack([curve(x, *args, **kwargs) for curve in self._splines])
        return (np.mean(s, axis=0), np.std(s, axis=0))

 

def interpolation_hall_probe(value):
    """Returns the interpolation of the measurement chart for the HallProbe. It uses the cubic spine interpolation from scipy
    to give the interpolation and error associated."""

    #Import the data from the appendix
    #MAKE SURE TO EDIT THIS PATH IF FILE LOCATION CHANGES
    HallProbe_Data=np.loadtxt('Data/CalibrationHallProbe/EQ3485_Calibration.csv',delimiter=',')
    volt=HallProbe_Data[:,0]
    bfield=HallProbe_Data[:,1]*0.1
    #Interpolation 
    interp = ErrorPropagationSpline(volt, bfield, 0.001)
    return interp(value)



def convert_voltage_to_tesla():
    raise NotImplementedError

def plot_data_csv(filename, path = "Data/CalibrationPowerSupply/" , savepath= "Figures/"):
    data = np.loadtxt(path+filename+'.csv', skiprows=1, delimiter=',')
    x = data[:,0]
    y = data[:,1]
    plt.plot(x,y,'.')
    plt.savefig(savepath+filename+'.png')



# x = np.linspace(0,0.35,100)
# y = interpolation_hall_probe(x)
# plt.plot(x,y[0])
# plt.show()

plot_data_csv('1001_1339_PSCalibration')

