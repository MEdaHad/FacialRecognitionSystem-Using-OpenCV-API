# Code to detect face, and train them so that they can be used during prediction.
#
# The path to the opencv has to be customized according to your installation of OpenCV package.
#
#

import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()

classifier = 'lbpcascade_frontalface.xml'
# Your path may differ ,depending on where you have installed the cv library
# old path - now it could be different.
#classifier_path='/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/cv2/data/'

classifier_path='/Users/shashikiran/nodetest/opencv/opencv/data/haarcascades/'


detector= cv2.CascadeClassifier('/Users/shashikiran/nodetest/opencvsources/opencv/data/lbpcascades/lbpcascade_frontalface.xml')

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print ("imagepaths ", imagePaths, "\n\n\n" )
    #create empth face list
    faceSamples=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        print ("Working on ...", imagePath) 
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        print ("Id =", Id, ", imagePath ", imagePath )
        # extract the face from the training image sample
        faces=detector.detectMultiScale(imageNp)
        #If a face is there then append that in the list as well as Id of it
        if (len(faces) == 0):
            print ("There was no face detected in ", imagePath)
            # Skip processing the image. Go to next one.
            next
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            #print ("appending ", Id)
            Ids.append(Id)
    print ( "Final Ids", Ids ) 
    return faceSamples,Ids


faces,Ids = getImagesAndLabels('dataSet')
recognizer.train(faces, np.array(Ids))

recognizer.save('trainner.yml')
