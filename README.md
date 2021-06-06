# Facial Recognition using Open CV APIs in Python
This article is about how to recognize faces, train and predict faces in images/photos (Jpeg, jpg) using OpenCV Python APis.

To learn more about the Open CV APIs refer : https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html

The Python code can be modified to recognize faces in Video streams as well.

Here I have used the most commonly used face detection algorigthm called LBPH (Local Binary Patterns Histogram) to recognize, train faces and predict faces.

**Note:** This does not detect images with no faces in them.

The code is simple and is split into 2 parts.

1) Set up training mode so that the face gets recognized and gets saved in some format understood by the API. The training involves reading the facial patterns and storing it in a flat file ( .yml file )

2) Predict and Recognize the new face that is provided.
User will have to provide the input to be predicted and if the image matches the data in trained data, then the image and the corresponding label gets displayed on the screen. 


### Prerequisites :

Install Python 3.x ( http://docs.python-guide.org/en/latest/starting/install3/linux/)

Install Pip 

Install cv2 ( Google for installing instructions. )

The dataset/ folder in the curent folder should contain images to be trained. 


### Code :

Currently the images (jpegs) belong to that of Trump and HH Dalai Lama are stored in the ```dataSet``` folder in the current directory.

You will notice that the file names/Ids on the Trump data set has a common '1' and HH Dalai Lama's images are set to '9', This distinguishes the labels for the faces and will help during prediction.
More the images - more accurate the prediction. Ensure that the images have visible face profiles of the person you wish to identify and predict.

If a new data set is to be created then enter an unique id/label for it as part of the file name in the dataSet. (Again, ensure that you have sufficient images for better accuracy of prediction)

e.g:  
1. Einstein.8.1.jpeg
2. Einstein.8.2.jpeg
3. Einstein.8.3.jpeg


### Execute

	1. python3 trainer.py

This will create the ```trainner.yml``` flat file containing the parameters of the images.

	2. python3 detector_image.py  <trump.jpeg>

This will detect the image in the trained library and if it can recognize then a rectangle is printed on the face, along with the name.

This can be further customized to user's specs. ( Just change the Id in the image.jpeg to whatever number you want.  e.g: Edison could have a label as  11, Think of this as a common label to the images. )

The blue box around the face is what gets detected by the Python Open CV API.

![screen shot 2018-05-16 at 3 20 06 pm](https://user-images.githubusercontent.com/14288989/40110079-b66f67f4-591c-11e8-85ce-f4470d511395.png)


Another sample :

![screen shot 2018-05-16 at 3 18 41 pm](https://user-images.githubusercontent.com/14288989/40110080-b69abe72-591c-11e8-8a42-5feba8d3a323.png)


### Troubleshooting:

Check that the input image is present and valid in the current folder when running the detector_image.py code.

Check that the trainner.yml exists after the images are trained before predicting a face.

If this error message shows up - that means the input file is incorrect.

	Image being processed :  dalailama.jpeg
	OpenCV Error: Assertion failed (scn == 3 || scn == 4) in cvtColor, file /Users/travis/build/skvark/opencv-python/opencv/modules/imgproc/src/color.cpp, line 11111
	Traceback (most recent call last):
	  File "detector_image.py", line 30, in <module>
	    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	cv2.error: /Users/travis/build/skvark/opencv-python/opencv/modules/imgproc/src/color.cpp:11111: error: (-215) scn == 3 || scn == 4 in function cvtColor



If this error message shows up - that means PIL is not installed.


		pip3 install image
		Collecting image
		  Downloading https://files.pythonhosted.org/packages/0c/ec/51969468a8b87f631cc0e60a6bf1e5f6eec8ef3fd2ee45dc760d5a93b82a/image-1.5.27-py2.py3-none-any.whl
		Collecting pillow (from image)
		  Downloading https://files.pythonhosted.org/packages/8f/f3/c6d351d7e582e4f2ef4343c9be1f0472cb249fb69695e68631e337f4b6e9/Pillow-6.1.0-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (3.8MB)
		     |████████████████████████████████| 3.9MB 2.4MB/s 
		Collecting django (from image)
		  Downloading https://files.pythonhosted.org/packages/94/9f/a56f7893b1280e5019482260e246ab944d54a9a633a01ed04683d9ce5078/Django-2.2.5-py3-none-any.whl (7.5MB)
		     |████████████████████████████████| 7.5MB 1.8MB/s 
		Collecting sqlparse (from django->image)
		  Downloading https://files.pythonhosted.org/packages/ef/53/900f7d2a54557c6a37886585a91336520e5539e3ae2423ff1102daf4f3a7/sqlparse-0.3.0-py2.py3-none-any.whl
		Collecting pytz (from django->image)
		  Using cached https://files.pythonhosted.org/packages/87/76/46d697698a143e05f77bec5a526bf4e56a0be61d63425b68f4ba553b51f2/pytz-2019.2-py2.py3-none-any.whl
		Installing collected packages: pillow, sqlparse, pytz, django, image
		Successfully installed django-2.2.5 image-1.5.27 pillow-6.1.0 pytz-2019.2 sqlparse-0.3.0
