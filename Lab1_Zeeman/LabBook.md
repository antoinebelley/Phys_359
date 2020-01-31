ZEEMAN EFFECT
============

06/01/2020
__________

* **15:15** : Reading the labooks for the experiment and setting-up the github repository and planing our the working schedule.

08/01/2020
__________

* **14:15**: Going through the list of equipment. So far, it looks like we are missing:
    * -EQ3494
    * -EQ3497 shunt 0.01 ohm/30 amps UPDATE found it! it is on top of the power supply
    * -Transparent tape
    * -D shaped lens

* **14:45**: We are starting the calibration

* **15:10**: Uploaded the calibration ccv file for EQ3485 + plot

* **15:23**: Trying to measure residual magnetic field with the Hall probe HR-66 (EQ3485). Not exposed to magnetic field, the probe yields 0.7mV with Fluke 77 multimeter (see error) which via linear extrapolation yields a residual magnetic field of 9.73 ~ 10 G = 0.001Tesla. Is this Earth's Magnetic Field? (0.0025-0.0065 Teslas) or is it just a resdual electronic current?

* **15:58**: Interpolation plot for the Hall Probe from the data given in appendix
![Interpolation Hall probe](https://github.com/antoinebelley/Phys_359/blob/master/Lab1_Zeeman/Figures/Calibration_of_Hall_Probe.png)

* **16:02**: We are currently aligning the Hall probe in the middle of the electromagnet by looking at the voltmeter and finding the highest voltage read.
Everytime we come to the lab, we should be doing a calibration measurement so that we acquire as much data as possible

* **16:15**: We are measuring power supply voltage vs Hall probe voltage (all in mv). The power supply is measured with the multimeter Hitachi EQ1692 on the setting 200mv, and the Hall probe voltage is measured with the multimeter Fluke77 on the 300mv setting. We took increments of 2.5mv to see the behaviour. It seems pretty linear so far. Saved data in [0801_1633_Powersupply_Calibration.csv](https://github.com/antoinebelley/Phys_359/blob/master/Lab1_Zeeman/Data/CalibrationPowerSupply/0801_1663_PSCalibraiton.csv).
Plot is here:

![0801_1633_Calibration_of_power_source.pdf](https://github.com/antoinebelley/Phys_359/blob/master/Lab1_Zeeman/Figures/0801_1633_Calibration_of_power_source.png)


08/01/2020
__________
* **13:39**: Calibrating power supply,we took pictures of our setup (picture). Centering the probe and taking new data.(See 08/01 for more details). On this calibration, we went up to 60mv, data in the file [1001_1339_Powersupply_Calibration.csv](https://github.com/antoinebelley/Phys_359/blob/master/Lab1_Zeeman/Data/CalibrationPowerSupply/1001_1339_PSCalibration.csv). 
![Hall probe](https://github.com/antoinebelley/Phys_359/blob/master/Lab1_Zeeman/Pictures/Hall_Probe.png)



* **14:03**: Plot the calibration to make sure it makes sense. Plot is shown below


![1001_1339_PSCalibration.png](https://github.com/antoinebelley/Phys_359/blob/master/Lab1_Zeeman/Figures/1001_1339_PSCalibration.png)
Also, a plotting method for csv files has been added to util.py

* **14:10**: We start setting up part 3.2.2 of the experiment (LG interferometer). We place the cadmium lamp between the coils (picture). We try and observe.
![Cd Lamp](https://github.com/antoinebelley/Phys_359/blob/master/Lab1_Zeeman/Pictures/Cd_Lamp.png)

* **15:35**: After a lot of effort we manage to see the band and to observe the diffraction pattern (pictures). We use the D-shaped lens to focus the light on the slit, which we made relatively small for its range. The slit is found when we adjust the screw controling the prism to about 55.6. 
![Lens](https://github.com/antoinebelley/Phys_359/blob/master/Lab1_Zeeman/Pictures/Focusing_Lens_Setup.png)
![Diffraction Pattern](https://github.com/antoinebelley/Phys_359/blob/master/Lab1_Zeeman/Pictures/Diffraction_Pattern.png)


13/01/2020
__________
* **10:40**:
    * Opening the cadmium lamp to let it warm up. It takes around 2-3 min for it to start produce its maximum intensity. 
    * Verifying that we can still see the diffraction ray using the telescope before placing the camera. 
    * Need to verify if the coil are in parallel or in series: it is written on them that we cannot pass more than 5 amp per coil continuously but we need to verify of that means 10 amp from the power supply. ->**After check they are in parallel.**

* **10:59**: Removing the telescope from the support and placing the CCD camera instead.

* **11:22**: Adjusting the camera to find optimal settings for pictures. Use Manual settings + focus at infinity for best results. We're setting the shutterspeed at 15" and the aperture at 5.7. 

* **11:36**: Taking our first picture -- having trouble with the blue reflects on the pictures. We believe this is caused by the long exposure (15").

* **11:42**: Stand for camera is loose. We're putting a sheet of paper around it to stabilize it as shown below
![Camera Set Up](https://github.com/antoinebelley/Phys_359/blob/master/Lab1_Zeeman/Pictures/Camera_Set_up.png)

* **11:43**: We're now trying 8". Not conclusive. We're changing the aperture to 8.0 (previously 5.7). Not much better, although we get rid of some reflects when putting the black sheet on top of the apparatus.

* **11:50**: We reduced ISO from 1600 to 80. We have a lot less reflections in our pictures. 

* **11:54**: We believed we found somewhat proper settings to take a picture. It is the 8th picture on the camera, the settings are: ISO 80, 15", F8.0, focus at infinity. WARNING when the camera falls in sleep mode, the focus changes.

* **11:57**: We have now started the power source and we are taking pictures at these different power supply voltages (in order) + hour shown on camera:
    * 0.0 mV (13:01)
    * 2.5 mV (13:02)
    * 5.0 mV (13:04)
    * 7.5 mV (13:05)
    * 10.0 mV (13:06)
    * 12.5 mV (13:07)
    * 15.0 mV (13:09)
    * 17.5 mV (13:11)
    * 20.0 mV (13:12)
    * 22.5 mV (13:13)
    * 25.1 mV (13:15)
    * 27.5 mV (13:16)
    * 30.0 mV (13:18)
    * 32.5 mV (13:19)
    * 35.0 mV (13:20)
    * 37.4 mV (13:21)
    * 40.2 mV (13:23)
    * 42.5 mV (13:24)
    * 45.0 mV (13:25)
    * 47.5 mV (13:27)
    * 50.1 mV (13:28)
    * 52.6 mV (13:30)
    * 55.0 mV (13:31)
    * 57.5 mV (13:32)
    * 60.1 mV (13:33)
    * 62.5 mV (13:34)
    * 65.1 mV (13:35)
    * 67.5 mV (13:37)
    * 70.1 mV (13:38)
    * 72.6 mV (13:39)
    * 95.5 mV (13:40)

* **12:41**: Lunch break

* **13:49**: We will look at the images took this moorning on the desktop in the lab. We try and use EyeSpy. We follow the lab manual and transform the pictures in '.bmp' format. 

* **14:02**: We converted the 2 first images in bmp format to test EyeSpy. To log in to EyeSpy, click on the Junk icon on the desktop (to access Saverio's keys) and then launch EyeSpy.

* **14:07**: We tested EyeSpy with the first Image (13:01), we can indeed place a line on the diffraction ray and get an intensity signal that we can export in .txt format (Line profile). Follow the instructions in the lab manual page 9 to use EyeSpy. Since it seems to work, we go ahead and do this with each image.  

* **14:10**: We rename the images in the fashion 'Ray_{voltage(mV)}' example Ray_0.0.jpg. We then change each of them in '.bmp' format. We made different folders 'JPEG_Images', 'BMP_Images' and 'Line_Profile'. We change the format of all the data and store it accordingly. 

* **16:15**: The data does not look conclusive. The damage on the LG plate might be too big for us to recover any usable data from the apparatus. We are presently trying to put the red filter in front of the LG plate to see if it gives us any better results.

* **16:27**: Adding the filter did not help. We will switch to the Fabry-Pérot next time to try to see if we can observe the Zeeman effect correclty.



15/01/2020
__________

**Fabry-Pérot**

* **14:21**: We are now changing to do FB experiment. We are undoing the setup for the LG experiment first. We observe that there seem to be missing a full part of the LG plate (The oblic part at the end) which could explain why it doesn't work...

* **14:37**: We placed the FB apparatus on (after the prism) and put a red filter between the prism and the FB apparatus (with tape). We can see the rings for the interference pattern but we can see a line with a lot more intensity because of the slit near the lamp...

* **14:46**: We place the center of the diffraction pattern near the bottom right corner of the camera. This allows us to see a lot more 3/4 of circles. We take a picture : no magnetic field (14:46). We are wondering if we can remove the slit-collimator apparatus in order to get rid of the slit effect in our pattern.   

* **14:55** We get a pattern much more uniform inintensity. Although, we get a point of light corresponding to the source itself and some reflects of it. We take a picture with this setting (No B-field, 14:57)

    * When comparing with the image with the collimator, we get a much clearer image without the collimator (more circles) outside of some blue reflects coming from the prism.

    * We rotate the prism so we get rid of noisy blue reflects. --> Maybe its just the prism being dirty. We try and clean it with wipes, but it doesnt change much. 

    * We get a nice image now.

* **15:11**: We try to put the lamp in a magnetic field to see if it has an effect on the diffraction pattern. Good news, it does! When we put the lamp in a big magnetic field (around 10 A in the power source), we see a lot more lines appear in the pattern.

    * We change the batteries of the camera, but after that we should be able to take some data.

* **15:17**: We are starting to take pictures for the FP setup. We will take pictures at increments of 10mV (settings: 80 ISO, Focus infinity, F8.0, 15"):
    * 0mV (15:17)
    * 10.0mV (15:18)
    * 20.0mV (15:20)
    * 30.1mV (15:21)
    * 40.0mV (15:22)
    * 50.0mV (15:23)
    * 60.0mV (15:25)
    * 70.0mV (15:27)
    * 80.1mV (15:28)
    * 89.9mV (15:30)

* **15:40**: in the samme manner as for the LG experiment, we put the images in JPEG_FP, the bmp formatted images in BMP_FP and the line profiles in Line_Profile_FP. The line profiles are obtained with each the same settings : the whole vertical length of the image (angle 90), 10 pixels of width and as through the center as possible (by eye). All of this is stored in the folder jan15 of our data.

20/01/2020
__________

* **12:05**: We start by performing a thorough calibration. This time, we will make sure to cover the whole range (0 - 90 mV) in one go. We start by finding the center using the same method as described in earlier calibration. This time, the universal stand is placed in between the coils and the prism --> it makes it easier to move the Hall probe. The data is stored in [2001_1214_Powersupply_Calibration.csv](https://github.com/antoinebelley/Phys_359/blob/master/Lab1_Zeeman/Data/CalibrationPowerSupply/2001_1214_PSCalibration.csv)
 	* **NOTE** After 75mV, we went over the 300mV range of the fine tuning of the voltmeter, hence we switch the volmeter to normal V measuring --> We lost a decimal digit of accuracy. 


* **13:00**: Lunch Break

* **15:04**: We set up the apparatus to perform the FB experiment. We are again going to take images of the diffraction pattern for a similar voltage range at the power source, but this time we will proceed a bit differently. Rather than taking images at each 10mV (or other constant voltage value), we will take pictures when the camera displays a nice focused diffraction pattern. Last time, we ended up with some images being blurry, maybe because some diffraction orders were too close to one another. 
	* Modus operandi:
	* Take a picture when the focus is good. 
	* Then increase voltage in the power source by a small amount --> and keep it such that we get a clear focused diffraction pattern. 
	* Take the picture
	* Repeat

* **15:14**: The set up is ready. We will be taking pictures with the same settings as before (ISO 80, focus at infinity, F8.0, 15"):
    * 0mv (15:17)
    * 5.0mV (15:19)
    * 15.2 mV (15:20)
    * 22.5 mV (15:22)
    * 35.0 mV (15:24)
    * 65.0 mV (15:28) **note** the splitting seems to be occuring between 35.0mV and 65.0 mV. Therefore, the images are blurry.
    * 83.0 mV (15:32)
    * 90.0 mV (15:33)

* **15:38**: we are running tests. When we put the collimator in the fabry perot setup, we're able to get rid of the big blob at the middle of the circle. However, a big white line now crosses the picture. We're taking pictures with the collimator, going downwards in the voltage.
    * 90.2mV (15:39) (without the wooden cover on the apparatus)
    * 90.2mV (15:43) (now we put the cover on)
    * 82.3 mV (15:47)
    * 75.1 mV (15:49)
    * 65.2 mV (15:51)
    * 55.0 mV (15:53)
    * 45.2 mV (15:54)
    * 34.8 mV (15:56)
    * 25.2 mV (15:59)

* **16:14**: We upload our data in the drive as jan20/JPEG_FP_Collimator and jan20/JPEG_FP_NoCollimator

22/01/2020
__________

* **13:53**: Discussion with Thomas -- Dont over complicate the circle analysis and we maybe have another LG plate

* **14:07**: We try one picture without the FP étalon (to get an image of the source alone) and we take one picture with the FP apparatus and take a picture with the diffraction pattern. We will try to substract them to get rid of the source image and just get the diffraction circles.

* **14:16**: We are doing the same thing as above but we're now removing the collimator. The first try was quite unsuccessful.


27/01/2020
__________

* **13:46**: We found a way to find the center of the circle using cross-corelation. Also build a code that extracts the line profile in x and y passing through the center found by the cross correlation and detects peaks and fit gaussians to them. We are veryfing that we can obtain the right value for the bohr magneton with the fitting. It is in the same order of magnitude, but it seems that the zeeman split lines are one of top of the other. 

* **15:15**: Found the error for the intensity of the pixels by taking two pictures (FP, 0mV), substracting them and taking the average. Found an error of 0.6.

* **15:45**: Trying to add the polarizer to isolate the split lines better.
    * 90.0 mV (15:46) Polarizer at 0 degree
    * 90.0 mv (15:53) Polarizer at -45 degree
    * 90.0 mV (15:54) Polarizer at 45 degree
* **16:28**: The polarizer does not help. It only dims the light
    * 0.0 mV (16:33) - taking a picture for further analysis
* **16:36**: We think the tape was the culprit
* **16:37**: The tape was indeed guilty. 
* **16:38**: Let's put back the polarizer and see what it gives
* **16:45**: can ignore that picture we just took
* **16:50**: We cannot obtain results with enough intensity with the polarizer so we gave up... Trying to do LG with the new plate.
* **17:08**: We setup the LG apparatus. We are taking a picture with no voltage
* **17:09**: We're applying some voltage to see if the splitting is better. We're at 90.1mv and we are taking a picture
* **17:28**: We are trying to get a clearer picture since at high voltage, the images are still blurry.
* **17:30**: Pictures taken but not so conclusive...


28/01/2020
__________

* **10:20**: After an analysis of all pictures for FP last night, we want to try and take clearer pictures that isolate the different splitting rays.
	* We clean up the set up (wipe the prism, set up FP experiment). 

* **10:29**: We change the red filter to a new one, the old one was pretty damaged.and dirty. 
* **10:37**: We cleaned up the camera. Turns out, it the images are much more clear. The camera was probably really dirty. 
* **10:52**: We change the batteries and prepare to take some pictures. 

* **10:55**: Camera Settings : 3.2", F5.6 aperture, ISO 80. 

	**Images**
	* 0.0 mV, 10:57
	* 89.0 mV, not clear enough to take a picture. 
* **11:44**: Try to place the lens near the camera : Does not help

* **12:05**: The knobs on the FP etalon can be used to adjust the angle and the image. 

* **12:07**: Taking images. 
	* 1.5 mV, 12:07
	* 89.9 mV, 12:11 , focus reduced
	* 89.9 mV, 12:13, polarizer blocking splitting rays
	* 89.9 mV, 12:16, polarizer letting splitting rays
	* 91.6 mV, 12:21, blocking split
	* 91.6 mV, 12:24, let what seems to be primary lines (j=0)
	* 91.6 mV, 12:25, let j=+-1

* **12:45**: Save them on drive under jan28/ and with eloquent names. Maybe if we take 3 pictures, no polarizer, polarizer j0 and polarizer j1, that would do the trick?

29/01/2020
__________

* **13:51**: Today we decided to evaluate possible systematic errors. 
* **13:54**: Update. We are seeing the lines a lot better today, following the adjustments made yesterday
* **13:55**: We took a picture at 0mv ish.
* **13:56**: We now take a picture really at 0mV. We have no polarizers

* **14:01**: We are starting to take data. We will take two pictures under the same settings using a polarizer. We are presently taking pictures at 89.0mV, at two different angles so that we see different rays of light. Here are the pictures we took at 89.0mV:
    * Two pictures with no polarizers (3.2",F8.0)
    * Two pictures with polarizer at a certain angle to focus on certain lines (8",F8.0)
    * Two pictures with polarizer at a different angle to focus on other lines (8",F8.0)
    * Two pictures with no polarizers at 0mV without moving the camera (3.2",F8.0)

* **14:06**: Note to the reader. The goal of taking two pictures with same settings everytime is to eventually derive an estimate for the systematic error.

* **14:07**: We are uploading the images in Antoine's computer.

* **14:27**: We now take pictures to evaluate the systematic error on the pixel intensity of the camera. We take successive pictures of a white sheet in our usual camera settings (8",F8.0 and 3.2",F8.0), so that we can quantify the systematic uncertainty. We took 5 pictures around 14:30.

* **15:25**: We start taking pictures again. We take two pictures every time, with the settings (8", F8.0, focus at inf). We start at 0 mV and we go up. We try to obtain clearer splitting between the +1 and -1 states. 
    * 0.1mV Two pictures
    * 60.7mV Two pictures with polarizer in one sense
    * 60.7mV Two pictures with polarizer in the other sense









  

