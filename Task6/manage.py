
import cv2
import os
import face_recognition_file


class Manager:
    def __init__(self):
        self.camera = False
        self.mk_dir('static/images')
        self.mk_dir('static/testing_images')
        self.mk_dir('static/text')
        self.mk_dir('videos')

    def mk_dir(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

    def use_camera(self):
        if not self.camera:
            self.cam = cv2.VideoCapture(0)
            self.camera = True
        return self.cam

    def release_camera(self):
        if self.camera:
            self.cam.release()
            self.camera = False

    def generate_frames(self):
        self.use_camera()
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('./videos/output2.avi', fourcc, 20.0, (640, 480))
        while True:

            success, frame = self.cam.read()
            out.write(frame)
            cv2.waitKey(41)
            if not success:
                break
            else:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()

            yield(b'--frame\r\n'
                  b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


    def face_rec(self, img):
        return face_recognition_file.face_recognization(img)
