import re
from flask import Flask,render_template,Response,request
import cv2
import json
import os

import flask
from flask.helpers import url_for
from werkzeug.utils import redirect
import main
import face_recognition_file

app=Flask(__name__)
app.config['UPLOAD_PATH'] = './static/testing_images'


camera=cv2.VideoCapture()
def use_camera():
    global camera
    camera=cv2.VideoCapture(0)
    
def release_camera():
    if camera.isOpened():
        camera.release()

def generate_frames():
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter('./videos/output2.avi',fourcc,20.0,(640,480))
    while True:
            
        success,frame=camera.read()
        out.write(frame)
        cv2.waitKey(41)
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
     
        yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@app.route('/')
def index():
    release_camera()
    return render_template('index.html')

@app.route('/video')
def video():
    use_camera()
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/videopage')
def videopage():
    return render_template('videopage.html')

@app.route('/result')
def result():
    release_camera()
    _data=main.result_data()   
    return final_result(_data)

@app.route('/predresult', methods=['GET', 'POST'])
def pred_result():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        print(uploaded_file.filename)

    if uploaded_file.filename != '':
        img=os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename)
        uploaded_file.save(img)
        _data=face_recognition_file.face_recognization(img)
        _data[0]=img
        return final_result(_data)
    else:
        return redirect(url_for('index'))
def final_result(_data):
    print(_data)
    return render_template('result.html',data=_data)

if __name__=="__main__":
    app.run(debug=True)
