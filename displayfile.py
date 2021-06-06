import cv2
img = cv2.imread('trump.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
if ( len( gray) ==0 ):
	print ("image is empty")
else :
	print ("Image is good")
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
