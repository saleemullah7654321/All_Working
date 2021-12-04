import os
import json
import face_recognition

def face_recognization(path):
    unknown_picture = face_recognition.load_image_file(path)
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    data_to_return=['','']
    for i in os.listdir('./static/images'):
        picture_of_me = face_recognition.load_image_file(f'./static/images/{i}')
        my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding,tolerance=0.5)
        if results[0] == True:
            data=json.load(open(f'./static/text/{i.split(".")[0]}.json'))
            data_to_return[0]=path    
            if data:
                data_to_return[1]=data
            break
    return data_to_return
