#!/usr/bin/env python
import sys
import cv2
import os
from sys import platform
import argparse
import time
import numpy as np
import matplotlib.pyplot as plt
import pyopenpose as op

# Custom Params for OpenPose(refer to include/openpose/flags.hpp for more parameters)
params = dict()
params["model_folder"] = "/home/ubuntu/openpose/models"

# Starting OpenPose
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()
start = time.time()
def get_pose_keypoints(input_image_path):

    output_image_path="/home/ubuntu/side_output_images/"
    output_keypoints_path="/home/ubuntu/side_output_keypoints/" 
    files = os.listdir(input_image_path)
    imagePaths = [os.path.join(input_image_path, f) for f in files if '.jpg' in f]
    #
    for imagePath in imagePaths:
        image_name=imagePath.replace(input_image_path,"")
        image_name=image_name.replace(".jpg",'')
        print(image_name)
        #Datum to send image to OpenPose wrapper
        datum = op.Datum()
        imageToProcess = cv2.imread(imagePath)
        datum.cvInputData = imageToProcess
        opWrapper.emplaceAndPop([datum])
        #Save the rendered output file
        cv2.imwrite(output_image_path+image_name+"_annotated.jpg",datum.cvOutputData)
        #Save the Keypoints
        np.savetxt(output_keypoints_path+image_name+"_keypoints.txt",datum.poseKeypoints[0]) 
        #print("Body keypoints: \n" + str(datum.poseKeypoints))
        print("Done with " + image_name)
#############################################################################################
input_image_folder_path="/Users/gwattal/squatsmart/frames_from_movies/"
folders = os.listdir(input_image_folder_path)
folderPaths = [os.path.join(input_image_folder_path, f) +"/" for f in folders if 'MOV' in f]
for folder in folderPaths:
    get_pose_keypoints(folder)

########## Done
opWrapper.stop()

end = time.time()
print(end - start)
########################################################################################################

print('Finished')
