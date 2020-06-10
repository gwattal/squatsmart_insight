import os
#import magic
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import numpy as np
import pickle
import pyopenpose as op
import cv2

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route('/')
def upload_form():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'giphy.gif')
    return render_template('upload.html', user_image = full_filename)

def get_keypoints(filename):
    params = dict()
    params["model_folder"] = "/home/ubuntu/openpose/models"
    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()
    datum = op.Datum()
    imageToProcess = cv2.imread(filename)
    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop([datum])
    keypoints=datum.poseKeypoints[0]
    filename_annotated=filename+"_annotated.jpg"
    cv2.imwrite(filename_annotated,datum.cvOutputData)
    xi=keypoints[:,0]
    yi=keypoints[:,1]
    opWrapper.stop()
    #xi, yi, c = np.loadtxt(filename).T
    x_test=(np.hstack((xi,yi))/max(np.hstack((xi,yi))))
    x_new_test = np.zeros(x_test.shape[0]+1)
    x_new_test[ :-1] = x_test
    x_new_test[-1]=(x_test[14]-x_test[11])/(x_test[5]-x_test[2])
    x_new_test[np.isinf(x_new_test)]=0.0
    return x_new_test,filename_annotated

@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            flash('File successfully uploaded') 
            flash('Analysing keypoints ....')
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            x_new_test,filename_annotated=get_keypoints(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            ### load the ovr logistic classifier now
            # load the model from disk
            loaded_model = pickle.load(open("ovr_logistic_regression_model.sav", 'rb'))
            result = loaded_model.predict(x_new_test.reshape(1,-1))
            feedback= "Your squat foot stance is " + result[0]
            #print(result)
            #return redirect('/')
            #feedback="your Squat form is "
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            return render_template("result.html",prediction=feedback,user_image=full_filename,
                user_image2=filename_annotated)
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)

if __name__ == "__main__":
    app.run()
