from flask import Flask,render_template,Response,request,url_for,redirect
import os
import main
from manage import Manager

app=Flask(__name__)
app.config['UPLOAD_PATH'] = './static/testing_images'

manager=Manager()


@app.route('/')
def index():
    manager.release_camera()
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(manager.generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')
    
@app.route('/videopage')
def videopage():
    return render_template('videopage.html')

@app.route('/result')
def result():
    manager.release_camera()
    _data=main.result_data()   
    return final_result(_data)

@app.route('/predresult', methods=['GET', 'POST'])
def pred_result():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            img=os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename)
            uploaded_file.save(img)
            _data=manager.face_rec(img)
            _data[0]=img
            return final_result(_data)
    else:
        return redirect(url_for('index'))

def final_result(_data):
    print(_data)
    return render_template('result.html',data=_data)

if __name__=="__main__":
    app.run(debug=True)
