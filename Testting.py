import cv2
import numpy as np

# optional argument for trackbars
def nothing(x):
    pass

# named ites for easy reference
barsWindow = 'Color test'
hl = 'H Low'
hh = 'H High'
sl = 'S Low'
sh = 'S High'
vl = 'V Low'
vh = 'V High'

# create window for the slidebars
cv2.namedWindow(barsWindow, flags = cv2.WINDOW_AUTOSIZE)

# create the sliders
cv2.createTrackbar(hl, barsWindow, 0, 179, nothing)
cv2.createTrackbar(hh, barsWindow, 0, 179, nothing)
cv2.createTrackbar(sl, barsWindow, 0, 255, nothing)
cv2.createTrackbar(sh, barsWindow, 0, 255, nothing)
cv2.createTrackbar(vl, barsWindow, 0, 255, nothing)
cv2.createTrackbar(vh, barsWindow, 0, 255, nothing)
'''
# set initial values for sliders
cv2.setTrackbarPos(hl, barsWindow, 0)
cv2.setTrackbarPos(hh, barsWindow, 179)
cv2.setTrackbarPos(sl, barsWindow, 0)
cv2.setTrackbarPos(sh, barsWindow, 255)
cv2.setTrackbarPos(vl, barsWindow, 0)
cv2.setTrackbarPos(vh, barsWindow, 255)

#initial value YELLOW
cv2.setTrackbarPos(hl, barsWindow, 10)
cv2.setTrackbarPos(hh, barsWindow, 66)
cv2.setTrackbarPos(sl, barsWindow, 166)
cv2.setTrackbarPos(sh, barsWindow, 255)
cv2.setTrackbarPos(vl, barsWindow, 131)
cv2.setTrackbarPos(vh, barsWindow, 255)
'''
#initial value GREEN
cv2.setTrackbarPos(hl, barsWindow, 12)
cv2.setTrackbarPos(hh, barsWindow, 140)
cv2.setTrackbarPos(sl, barsWindow, 0)
cv2.setTrackbarPos(sh, barsWindow, 255)
cv2.setTrackbarPos(vl, barsWindow, 0)
cv2.setTrackbarPos(vh, barsWindow, 158)


while(True):
    hinh1='img81.jpg'
    hinh2='img83.jpg'
    hinh3='img85.jpg'
    hinh4='img87.jpg'
    hinh5='img89.jpg'
    hinh6='img91.jpg'
    hinh7='img93.jpg'
    hinh8='img95.jpg'
    hinh9='img97.jpg'
    hinh10='img99.jpg'

    img1 = cv2.imread(hinh1)
    img2 = cv2.imread(hinh2)
    img3 = cv2.imread(hinh3)
    img4 = cv2.imread(hinh4)
    img5 = cv2.imread(hinh5)
    img6 = cv2.imread(hinh6)
    img7 = cv2.imread(hinh7)
    img8 = cv2.imread(hinh8)
    img9 = cv2.imread(hinh9)
    img10 = cv2.imread(hinh10)
    #hvs = cv2.imread("img01.jpg", cv2.IMREAD_GRAYSCALE)

    hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
    hsv3 = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)
    hsv4 = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV)
    hsv5 = cv2.cvtColor(img5, cv2.COLOR_BGR2HSV)
    hsv6 = cv2.cvtColor(img6, cv2.COLOR_BGR2HSV)
    hsv7 = cv2.cvtColor(img7, cv2.COLOR_BGR2HSV)
    hsv8 = cv2.cvtColor(img8, cv2.COLOR_BGR2HSV)
    hsv9 = cv2.cvtColor(img9, cv2.COLOR_BGR2HSV)
    hsv10 = cv2.cvtColor(img10, cv2.COLOR_BGR2HSV)
    #hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

    hul = cv2.getTrackbarPos(hl, barsWindow)
    huh = cv2.getTrackbarPos(hh, barsWindow)
    sal = cv2.getTrackbarPos(sl, barsWindow)
    sah = cv2.getTrackbarPos(sh, barsWindow)
    val = cv2.getTrackbarPos(vl, barsWindow)
    vah = cv2.getTrackbarPos(vh, barsWindow)

    # make array for final values
    HSVLOW = np.array([hul, sal, val])
    HSVHIGH = np.array([huh, sah, vah])

    # apply the range on a mask
    mas1 = cv2.inRange(hsv1, HSVLOW, HSVHIGH)
    mas2 = cv2.inRange(hsv2, HSVLOW, HSVHIGH)
    mas3 = cv2.inRange(hsv3, HSVLOW, HSVHIGH)
    mas4 = cv2.inRange(hsv4, HSVLOW, HSVHIGH)
    mas5 = cv2.inRange(hsv5, HSVLOW, HSVHIGH)
    mas6 = cv2.inRange(hsv6, HSVLOW, HSVHIGH)
    mas7 = cv2.inRange(hsv7, HSVLOW, HSVHIGH)
    mas8 = cv2.inRange(hsv8, HSVLOW, HSVHIGH)
    mas9 = cv2.inRange(hsv9, HSVLOW, HSVHIGH)
    mas10 = cv2.inRange(hsv10, HSVLOW, HSVHIGH)
    mask1 = cv2.medianBlur(mas1, 5)
    mask2 = cv2.medianBlur(mas2, 5)
    mask3 = cv2.medianBlur(mas3, 5)
    mask4 = cv2.medianBlur(mas4, 5)
    mask5 = cv2.medianBlur(mas5, 5)
    mask6 = cv2.medianBlur(mas6, 5)
    mask7 = cv2.medianBlur(mas7, 5)
    mask8 = cv2.medianBlur(mas8, 5)
    mask9 = cv2.medianBlur(mas9, 5)
    mask10 = cv2.medianBlur(mas10, 5)
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

    # Set up the detector with default parameters.
    detector = cv2.SimpleBlobDetector_create(params)
 

    # Detect blobs.
    keypoints1 = detector.detect(mask1)
    keypoints2 = detector.detect(mask2)
    keypoints3 = detector.detect(mask3)
    keypoints4 = detector.detect(mask4)
    keypoints5 = detector.detect(mask5)
    keypoints6 = detector.detect(mask6)
    keypoints7 = detector.detect(mask7)
    keypoints8 = detector.detect(mask8)
    keypoints9 = detector.detect(mask9)
    keypoints10 = detector.detect(mask10)
    
 
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints1 = cv2.drawKeypoints(mask1, keypoints1, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints2 = cv2.drawKeypoints(mask2, keypoints2, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints3 = cv2.drawKeypoints(mask3, keypoints3, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints4 = cv2.drawKeypoints(mask4, keypoints4, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints5 = cv2.drawKeypoints(mask5, keypoints5, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints6 = cv2.drawKeypoints(mask6, keypoints6, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints7 = cv2.drawKeypoints(mask7, keypoints7, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints8 = cv2.drawKeypoints(mask8, keypoints8, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints9 = cv2.drawKeypoints(mask9, keypoints9, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    im_with_keypoints10 = cv2.drawKeypoints(mask10, keypoints10, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
   
    # display the camera and masked images
    cv2.imshow(hinh1, im_with_keypoints1)
    cv2.imshow(hinh2, im_with_keypoints2)
    cv2.imshow(hinh3, im_with_keypoints3)
    cv2.imshow(hinh4, im_with_keypoints4)
    cv2.imshow(hinh5, im_with_keypoints5)
    cv2.imshow(hinh6, im_with_keypoints6)
    cv2.imshow(hinh7, im_with_keypoints7)
    cv2.imshow(hinh8, im_with_keypoints8)
    cv2.imshow(hinh9, im_with_keypoints9)
    cv2.imshow(hinh10, im_with_keypoints10)
    sum = len(keypoints1)+len(keypoints2)+len(keypoints3)+len(keypoints4)+len(keypoints5)+len(keypoints6)+len(keypoints7)+len(keypoints8)+len(keypoints9)+len(keypoints10)   
    print(sum)
    # Show keypoints
    #cv2.imshow("Keypoints", im_with_keypoints)

    #print("First one: %d" % len(keypoints1)) 
    #print(len(keypoints)) 
	# check for q to quit program with 5ms delay
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


# clean up our resources
cap.release()
cv2.destroyAllWindows()