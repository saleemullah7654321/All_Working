import cv2
import easyocr
import os
import text_get
import json

def result_data():
    reader=easyocr.Reader(['en'])
    def detect_face(video):
        cap = cv2.VideoCapture(video)
        skip_frame_rate=0
        while True:
            ret,frame=cap.read()
            if not ret:
                break

            __face_detection(frame) 
            if skip_frame_rate%20==0:
                text_detection(frame)
            skip_frame_rate+=1

    def text_detection(frame):
        im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if not os.path.exists('./static/text/data.json'):
            data_dic=get_data_dic(im)
            file=json.dumps(data_dic,indent=4)
            with open('./static/text/data.json','w') as f:
                f.write(file)
        else:
            f=json.load(open('./static/text/data.json'))
            count=0
            dic={}
            keys_to_find=[]
            for k,v in f.items():
                if v=='-':
                    count+=1
                    keys_to_find.append(k)
            if count>0:
                data_dic=get_data_dic(im)
                for keys in keys_to_find:
                    f[keys]=data_dic[keys]
                    print(keys,f[keys])
                file=json.dumps(f,indent=4)
                with open('./static/text/data.json','w') as f:
                    f.write(file)
                  
    def get_data_dic(im):
        result=reader.readtext(im)
        data_list=[]
        for pos,data,pred in result:
            data_list.append(data)
        data= text_get.get_data(data_list)
        return data               




    def __face_detection(img):
        if os.path.exists('./static/images/face.png'):
            return img
        face_cascade = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        box,detections = face_cascade.detectMultiScale2(gray,minNeighbors=8)
        if len(detections)>0 and detections[0]>=80:
            for x,y,w,h in box:
                face = img[y-50:y + h+20, x-30:x + w+30]
                cv2.resize(face,(200,200),interpolation=cv2.INTER_AREA)
            cv2.imwrite('./static/images/face.png',face)
            return face
        else:
            print(detections)
            return img
    if os.path.exists('./static/images/face.png'):
        os.remove('./static/images/face.png')
    if os.path.exists('./static/text/data.json'):
            os.remove('./static/text/data.json')

    detect_face(video='./videos/output2.avi')
