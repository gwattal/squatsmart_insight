# SquatSmart - insight
Welcome to SquatSmart - Your virtual squat spotter. 

## What is SquatSmart?
People are getting more aware about fitness and are investing more time and money on it. Weight training is an essential part of fitness as it builds strength and bone density. Strength training is useful in countering the affects of ageing and is important especially for women and the elderly. Barbell squats are an important weight training exercise as it builds strength in the lower body, the core and arms.  

To get the most out of a squat workout and to avoid injuries, the squat needs to be done with proper form. It can be hard to judge your own form while performing a demanding exercise like barbell squats, especially when one is a beginner. Many people take the help of a personal trainer or spotter to get feedback on their squat form, however this can be a little expensive. Moreover in the times of the Covid pandemic people might not have access to personal trainers or spotters.

Here is where SquatSmart comes in! With SquatSmart (http://analyticsanddata.me/) a user can simply upload a picture of them performing the squat and get feedback on their squat form.

## Using SquatSmart

The user can upload the picture of them performing the squat either front facing or side facing. It can be taken from a phone camera. The camera should be in the centre with respect to the person and the camera angle should be aligned so that the image plane is parallel to the vertical direction. 
When they upload the image the model runs in the background and analyses the image and returns feedback to the user. The model can take unto 15 seconds to run.
![alt text](</squatsmart/uploads/webapp1.png>)
![alt text](</squatsmart/uploads/webapp2.png>)

## How SquatSmart Works
 When the user uploads an image the model first extracts the pose information is extracted using the Openpose library. The pose keypoints are then used to determine the image orientation, ie front facing or side facing. If the image is deemed to be front facing then the model looks at the foot stance and determines if it is a wide, normal or narrow foot stance. If the image is side facing then the model evaluates the squat depth and determines whether the right squat depth is being achieved. 
 
## Pipeline
![alt text](</squatsmart/uploads/pipeline.svg>)


## AWS

Instructions to get install and run squatsmart on an AWS EC2 instance.

Start with the [AWS Ubuntu Deep Learning Base AMI](https://aws.amazon.com/marketplace/pp/B07Y3VDBNS?qid=1591551938734&sr=0-1&ref_=srh_res_product_title).

Check the version of CUDA once you are logged in to the instance:

```
ubuntu@ip-172-31-25-30:~$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2018 NVIDIA Corporation
Built on Sat_Aug_25_21:08:01_CDT_2018
Cuda compilation tools, release 10.0, V10.0.130
```

Update packages and install openpose:

```
./install_deps.sh
```

Put this in `~/.bashrc`

```
export PATH="${HOME}/opt/cmake-3.16.0-Linux-x86_64/bin:${PATH}"
export PYTHONPATH="${HOME}/openpose/build/python/openpose:${PYTHONPATH}"
```
