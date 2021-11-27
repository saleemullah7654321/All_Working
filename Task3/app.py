from flask import Flask,render_template,Response
import cv2
import json
import os
import main


app=Flask(__name__)

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
    main.result_data()
    if os.path.exists('./static/text/data.json'):
        f=json.load(open('./static/text/data.json'))
    else:
        f=''
    return render_template('result.html',data=f)

if __name__=="__main__":
    app.run(debug=True)
