import face_recognition
import cv2
import numpy as np 
import csv
import os
from datetime import datetime

video_capture = cv2.VideoCapture(0)

image1 = face_recognition.load_image_file("C:\\Users\\Himanshu Singh\\OneDrive\\Desktop\\CODES\\Python codes\\Mini_Python_Projects\\Project 7\\gandhi_ji.jpg")
image_1 = face_recognition.face_encodings(image1)[0]

image2 = face_recognition.load_image_file("C:\\Users\\Himanshu Singh\\OneDrive\\Desktop\\CODES\\Python codes\\Mini_Python_Projects\\Project 7\\narendra_modi.jpg")
image_2 = face_recognition.face_encodings(image2)[0]

known_face_encoding = [
    image_1,
    image_2
]

known_face_names = [
    "narendra_modi",
    "gandhi_ji"
]

students = known_face_names.copy()

face_location = []
face_encodings = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date+'.csv','w+',newline='')
lnwriter = csv.writer(f)

while True:
    # frame = video_capture.read()
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_location = face_recognition.face_locations(rgb_small_frame)
        face_encoding = face_recognition.face_encodings(rgb_small_frame, face_location)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
            if name in known_face_names:
                students.remove(name)
                print(students)
                current_time = now.strftime("%H-%M-%S")   
                lnwriter.writerow([name,current_time])
    cv2.imshow("attendance system",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
f.close()

