ZEEMAN EFFECT
============

06/01/2020
__________

* **15:15** : Reading the labooks for the experiment and setting-up the github repository and planing our the working schedule.

08/01/2020
__________

* **14:15**: Going through the list of equipment. So far, it looks like we are missing:
-EQ3494
-EQ3497 shunt 0.01 ohm/30 amps UPDATE found it! it is on top of the power supply
-Transparent tape
-D shaped lens

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
* **13:39**: Calibrating power supply,we took pictures of our setup (picture). Centering the probe and taking new data.(See 08/01 for more details). On this calibration, we went up to 60mv, data in the file [1001_1339_Powersupply_Calibration.csv](https://github.com/antoinebelley/Phys_359/blob/master/Lab1_Zeeman/Data/CalibrationPowerSupply/1001_1339_PSCalibraiton.csv). 
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
![Camera Set Up](https://github.com/antoinebelley/Phys_359/blob/master/Lab1_Zeeman/Pictures/Camera_Set_up.png.png)

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





