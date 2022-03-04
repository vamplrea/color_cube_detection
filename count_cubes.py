import cv2
import numpy as np

#TODO: Modify these values for yellow color range. Add thresholds for detecting green also.
'''
yellow_lower = np.array([10, 166, 131])
yellow_upper = np.array([66, 255, 255])

green_lower = np.array([12, 0, 0])
green_upper = np.array([140, 255, 158])
'''
#new range of file
yellow_lower = np.array([9, 115, 151])
yellow_upper = np.array([179, 215, 255])
green_lower = np.array([0,0,0])
green_upper = np.array([179, 255, 60])

def filter_image(img, hsv_lower, hsv_upper):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
    return mask

def detect_blob(mask):
    img = cv2.medianBlur(mask, 5)

   # Set up the SimpleBlobdetector with default parameters with specific values.
    params = cv2.SimpleBlobDetector_Params()
    # Color
    params.filterByColor = True;
    params.blobColor = 255
    # shape
    params.filterByCircularity = 0
    params.minCircularity = 0.7
    # Filter by Area.
    params.filterByArea = 1
    params.minArea = 200

    params.filterByConvexity = True
    params.minConvexity = 0.5

    # builds a blob detector with the given parameters 
    detector = cv2.SimpleBlobDetector_create(params)

    # use the detector to detect blobs.
    keypoints = detector.detect(img)

    return len(keypoints)

def count_cubes(img):
    mask_yellow = filter_image(img, yellow_lower, yellow_upper)
    num_yellow = detect_blob(mask_yellow)
    mask_green = filter_image(img, green_lower, green_upper)
    num_green = detect_blob(mask_green)
    #TODO: Modify to return number of detected cubes for both yellow and green (instead of 0)
    return num_yellow, num_green