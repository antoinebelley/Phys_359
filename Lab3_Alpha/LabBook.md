Alpha
=============

09/03/2020
__________
* **14:07**: Verified the list of equipments. We verify the value of lambda1 and lambda2 to choose our time steps. We find that the half-life 212Pb 10.64(1) h and the half-life of 212Bi 60.60 min so we get that lam_Pb = ln(2)/38304 = 0.00001809594 1/s, and lam_Bi = ln(2)/3636 = 0.00019063453 1/s.

* **14:27**: From the plot of the A2 we can see the peaks to be a bit before 4 hours. 

* **15:15**: Assembled the set-up. Placed the preamplifier as close as possible to the detector. Will proceed to do the calibration with the Am241 source.

* **15:32**: Put source 64 of Am241 Started the pump. We reached a pressure of 80 mTorr. We plug the preamp directly inside the oscilloscope and we can observe a peak of approx. 100mv and a width of 4 ms. When turning on the desired 65 V bias, we indeed obsereve the baseline bias on the oscilloscope.

* **15:48**: We now plug the preamp into the amplifier and the amplifier is plugged into both the oscilloscope and the CPU using a tee. We trigger on the oscilloscope to get a much cleaner signal now. We first look at the signal in the  We try and see if we can obtain data (and a single peak) on the maestro program.

* **15:53**: We now record the peak for the calibraiton without the pulser. I think the high pitch noise will kill me. We placed the gain to coarse 32 and fine slightly over 3. Bias voltage = 65V. We see the peak of Am 241 at marker 1218. We try and add a pulse in order to observe a second peak. At first, the second peak really grows faster. We try and attenuate it.

* **16:10**: We start calibrating by recording the association between the voltage in the pulse generator and the channel number in the spectrum. The data is stored in csv format in the file calibration_pulse.txt . We plot as we go to verify the linear relationship using the file plot_calib.py . 

* **16:35**: We finished calibrating (reached a saturation in our plot). We save a preliminary plot for the calibration as calibration_v1.png. We turn off all apparatus. We give back the Am source and we leave for the day. 


11/03/2020
__________
* **14:20**: We fit a straight line to our calibration data points channel vs pulse from last time. By using a Chi Squared minimization, we drop our last 3 data points and get an estimate for the real zero of the line of -7.67216754 and the reduced Chi2 is 1.658089796546017. This was done with the plot_calib.py file. 
	- Results 1.658089796546017
	[ 2.10841569 -7.67216754]
![Calibration plot](https://github.com/antoinebelley/Phys_359/blob/master/Lab3_Alpha/calibration_v1.png)

* **14:37**: Saverio disappeared. We have to wait for him in order to create our Pb source. Hence, we use the Am source again to save a data of the spectrum which we will fit will gaussian peaks in order to be more precise. 

* **14:53**: Finally we will let the calibration spectrum run overnight. For the pressure varying measurements, we start by looking at the effect of changing the pressur on the Am peak roughly through the pressure range. To let air in the chamber, close the vacuum valve and tweak (shortly open) the down valve.

* **15:15**: we start recording the data. At each pressure we save a spectrum on the desktop with name Am241_(Pressure)mB. We make 20 mB jumps between each measurement.  
* **15:50**: We did 20 mb jumps from 0 to 120 mB. Now following Dominic's idea, we get rid of the bias and in one run, we record multiple peaks at different pressures. The peaks move to the left on the spectrum. From left to right, the peaks are taken at pressure : 
	pressure (mB)
	120 
	200
	310 
	400
	500 -> no more detection. 

* **16:00**: We now know that at 500 mB (no bias), we lose the signal. We will take other pressure varying data later knowing that!

* We put back the low pressure in the tank and let a spectrum measurement run overnight (until friday). 



