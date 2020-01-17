#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

# # Read image
# im = cv2.imread("/Users/antoine/Documents/McGill/Winter_2020/Phys_359/Lab1_Zeeman/Pictures/Pattern_00.jpg")


# # Setup SimpleBlobDetector parameters.
# params = cv2.SimpleBlobDetector_Params()

# # Change thresholds
# params.minThreshold = 10
# params.maxThreshold = 200


# # Filter by Area.
# params.filterByArea = True
# params.minArea = 1500

# # Filter by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.1

# # Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.87
    
# # Filter by Inertia
# params.filterByInertia = True
# params.minInertiaRatio = 0.01



# # Create a detector with the parameters
# ver = (cv2.__version__).split('.')
# if int(ver[0]) < 3 :
#    detector = cv2.SimpleBlobDetector(params)
# else : 
#    detector = cv2.SimpleBlobDetector_create(params)


# # Detect blobs.
# keypoints = detector.detect(im)


# # Draw detected blobs as red circles.
# # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# # the size of the circle corresponds to the size of blob

# im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# imS = cv2.resize(im_with_keypoints, (960, 540))  
# # Show blobs
# cv2.imshow("Keypoints", imS)
# cv2.waitKey(0)

import cv2 
import numpy as np 
  
# Load image 
image = cv2.imread('/Users/antoine/Documents/McGill/Winter_2020/Phys_359/Lab1_Zeeman/Pictures/Pattern_20.0.jpg', 0) 
  
# Set our filtering parameters 
# Initialize parameter settiing using cv2.SimpleBlobDetector 
params = cv2.SimpleBlobDetector_Params() 
  
# Set Area filtering parameters 
params.filterByArea = True
params.minArea = 1000
  
# # Set Circularity filtering parameters 
# params.filterByCircularity = True 
# params.minCircularity = 0.1
  
# # Set Convexity filtering parameters 
# params.filterByConvexity = True
# params.minConvexity = 0.2
      
# # Set inertia filtering parameters 
# params.filterByInertia = True
# params.minInertiaRatio = 0.5
  
# Create a detector with the parameters 
detector = cv2.SimpleBlobDetector_create(params) 
      
# Detect blobs 
keypoints = detector.detect(image) 
  
# Draw blobs on our image as red circles 
blank = np.zeros((1, 1))  
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), 
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 
  
number_of_blobs = len(keypoints) 
text = "Number of Circular Blobs: " + str(len(keypoints)) 
cv2.putText(blobs, text, (20, 550), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2) 
  
# Show blobs 
imS = cv2.resize(blobs, (1600,900))  
cv2.imshow("Filtering Circular Blobs Only", imS) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
exit()