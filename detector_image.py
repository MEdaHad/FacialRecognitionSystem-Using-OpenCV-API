# 
# This is the trainer code, when run it will create a trainner.yml external file.
# The trainner.yml will contain the images being trained and it's parameters,
# and will be stored in the current folder
#
# To run:
# Python3 detector.py  <image.jpeg>
# 
import cv2
import numpy as np
import sys

# Feed in the name of the image to be processed as an argument.

if (len ( sys.argv) > 1) :
	image_name=sys.argv[1]
	print ("Image being processed : ", image_name)
else :
	print (" Please provide the name of the image to detect face.")
	quit()

# Function to print text in the final image.
def print_text(text_to_print):
                print (  text_to_print )
                font                   = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,300)
                fontScale              = 1
                fontColor              = (255,255,255)
                lineType               = 2

                cv2.putText(img,text_to_print,
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)
                cv2.imshow('image',img)
                cv2.waitKey()
                #cv2.waitKey(0)

# End of function.

# Code starts from here.	
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')

#classifier = 'lbpcascade_frontalface.xml'
#classifier_path='/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/'

faceCascade= cv2.CascadeClassifier('/Users/shashikiran/nodetest/opencvsources/opencv/data/lbpcascades/lbpcascade_frontalface.xml')

img = cv2.imread(image_name)
font = cv2.FONT_HERSHEY_SIMPLEX

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(gray, 1.2,5)

if ( len (faces ) == 0) :
	print( "No identifiable faces found, Please select a correct image as input !")
	print( "Please check on the quality of the print, clarity of data in the image")
	print ("Try another image that is a little more clearer")
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()	
	quit()

for(x,y,w,h) in faces:
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        
        print ("Confidence level = " ,conf, " Id = ", Id )

        if ( conf > 50 ):
            print (" Cannot recognize this image, Check if the label[] has been assigned to this image in this code ");	
            print (" e.g:  dataSet folder to contain some training images")
            quit()
        elif (conf < 50):
            if ( Id == 9) :
                Id="DalaiLama"
                print_text ( "HH Dalai Lama")

            elif (Id==1):
                print_text ( "Donald Trump")

            else:
                print ( "This is NOT identified ! ")
                Id="Unknown"
                font                   = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,300)
                fontScale              = 1
                fontColor              = (255,255,255)
                lineType               = 2

                cv2.putText(img,'Unknown User !',
                        bottomLeftCornerOfText,
                        font,
                        fontScale,
                        fontColor,
                        lineType)
                cv2.imshow('im',img) 
                cv2.waitKey(10)


cv2.destroyAllWindows()
