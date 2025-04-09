#WEB library
import streamlit.components.v1 as components
from secrets import choice
import streamlit as st

#opencv library
import face_recognition
from datetime import datetime
from PIL import Image
import pandas as pd
import numpy as np
import cv2
import os
import time

st.markdown("""
<div class="container" style="background-color: #33FFFF; width: 800px; ">
<nav class="navbar navbar-expand-lg bg-light" style="background-color: #33FFFF">
  <div class="container-fluid" style="background-color: #33FFFF">
    <a class="navbar-brand" href="index.php"></a> <button onclick="topFunction()" id="myBtn" class="myBtn" title="Go to top"><i style="color: black;" class="fa-solid fa-bars"></i></button>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" style="color: #000; font-weight: bold; margin-right: 20px;"><img src="https://img.icons8.com/fluency-systems-filled/48/000000/about-us-male.png" style="width: 24px;"/>@--______________________________ Advance Attendance System ______________________________--</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
</div>

""", unsafe_allow_html=True)

FRAME_WINDOW = st.image([]) #frame window

hhide_st_style = """ 
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hhide_st_style, unsafe_allow_html=True) #hide streamlit menu


menu = ["HOME","MARK ATTENDANCE", "REGISTER", "ATTENDANCE SHEET", "KNOW MORE"] #menu
choice = st.sidebar.selectbox("Menu", menu) #sidebar menu

path = 'Register_Data' #path to save image
images = [] #list of image
classNames = [] #list of class
myList = os.listdir(path) #list of image


col1, col2, col3 = st.columns(3) #columns
cap = cv2.VideoCapture(0) #capture video
if choice == 'MARK ATTENDANCE': 
    st.markdown("<h2 style='text-align: center; color: black;'>ATTEDANCE  SYSTEM</h2>", unsafe_allow_html=True) #title
    with col1: #column 1
        st.subheader("MARK ATTENDANCE")
        run = st.checkbox("MARK YOUR PRESENCE") #checkbox
    if run == True:
        for cl in myList: #loop
            curlImg = cv2.imread(f'{path}/{cl}') #read image
            images.append(curlImg)
            classNames.append(os.path.splitext(cl)[0]) #split image name
        print(classNames)

        def findEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encodings = face_recognition.face_encodings(img)
                if encodings:  # check if list is not empty
                    encodeList.append(encodings[0])
                else:
                    print("No face found in image, skipping.")
            return encodeList


        def faceList(name):
            with open('Attendance_Sheet.csv', 'r+') as f:
                myDataList = f.readlines()
                nameList = []
                for line in myDataList:
                    entry = line.split(',')
                    nameList.append(entry[0])
                if name not in nameList:
                    now = datetime.now()
                    dtString = now.strftime('%H:%M:%S')
                    dStr = now.strftime('%d:%m:%Y')
                    f.writelines(f'\n{name},{dtString},{dStr}')

        encodeListUnkown = findEncodings(images)
        print('encoding complate!')
        while True:
            success, img = cap.read()
            imgS = cv2.resize(img,(0,0),None,0.25,0.25)
            imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
            faceCurFrame = face_recognition.face_locations(imgS)
            encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)

            for encodeFace,faceLoc in zip(encodeCurFrame,faceCurFrame):
                matches = face_recognition.compare_faces(encodeListUnkown,encodeFace)
                faceDis = face_recognition.face_distance(encodeListUnkown,encodeFace)
                #print(faceDis)
                matchesIndex = np.argmin(faceDis)
                
                y1,x2,y2,x1 = faceLoc
                y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4

                if matches[matchesIndex]:
                    name = classNames[matchesIndex].upper()
                    print(name)
                    cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,150),2)
                    cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,150),cv2.FILLED)
                    cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
                    faceList(name)

                    time.sleep(3)
                
                else:
                    y1,x2,y2,x1 = faceLoc
                    y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                    cv2.rectangle(img,(x1,y1),(x2,y2),(255,102,102),2)
                    cv2.rectangle(img,(x1,y2-35),(x2,y2),(255,102,102),cv2.FILLED)
                    cv2.putText(img,"Unknown",(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
            FRAME_WINDOW.image(img)
            cv2.waitKey(1)
    else:
        pass
#register menu
elif choice == 'REGISTER':
    with col2:
        st.subheader("REGISTER")
    def load_image(image_file):
        img = Image.open(image_file)
        return img

    image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
    if image_file is not None:
        file_details = {"FileName":image_file.name,"FileType":image_file.type}
        st.write(file_details)
        img = load_image(image_file)
        with open(os.path.join("Register_Data",image_file.name),"wb") as f: 
            f.write(image_file.getbuffer())         
        st.success("Saved File")

#read data menu
elif choice == 'ATTENDANCE SHEET':
    with col2:
        df = pd.read_csv('Attendance_Sheet.csv')
        st.subheader("READ ATTENDANCE SHEET")
        df = pd.read_csv('Attendance_Sheet.csv')
        st.write(df)
elif choice == 'HOME':
    st.markdown("""
<div class="container" style="background-color: #33FFFF; width: 800px; ">
<nav class="navbar navbar-expand-lg bg-light" style="background-color: #33FFFF">
  <div class="container-fluid" style="background-color: #33FFFF">
    <a class="navbar-brand" href="index.php"></a> <button onclick="topFunction()" id="myBtn" class="myBtn" title="Go to top"><i style="color: black;" class="fa-solid fa-bars"></i></button>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" style="color: #000; font-weight: bold; margin-right: 20px;"><img src="https://img.icons8.com/fluency-systems-filled/48/000000/about-us-male.png" style="width: 24px;"/>@--______________________________ Advance Attendance System ______________________________--</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
</div>

""", unsafe_allow_html=True)
    with col1:
        st.image("face-recogination.jpg",width=800, caption="Advance Attendance System Using Face Recognition") 

elif choice == "KNOW MORE":
    st.subheader("KNOW HERE HOW TO USE THIS SYSTEM")
    st.subheader("o- On HOME page you find sidebar, from there you can nevigate to other pages.")
    st.subheader("o- First you need to go to REGISTER HERE page and there you need to upload your beautiful and handsome image with clear face and the file name of you image should be your name which you want to display in attendance sheet.")
    st.subheader("o- Then to mark your attendance you need to go to MARK ATTENDANCE page and click on MARK YOUR PRESENCE button to open camera (Make sure system camera is proper) and then wait until you see a rectangle around your face and your name over it in camera frame, this mark your attendance. If you see Unknown Face, it means you didn't register yet or you are failed to upload your clear image.")
    st.subheader("o- Then click on ATTENDANCE SHEET page from sidebar and there you will see your attendance get marked, if do all the step correctly. Please do not remove NAME,TIME field from Attendance_Sheet.csv file if your operating site from your system and not from server else you will see error.")
    st.subheader("o- This system is one time use system for now, so if you want to take attendance again so, you need to remove previous attendance sheet data and store it in another sheet else you can't take attendance of same person 2nd time.")
    st.subheader("o- I am planning to add attendance_in and attendance_out to measure the time for which a person are presence and also login system to watch the attendance sheet in near future, but for evaluation purpose I skip that part.")
    st.subheader("o- Thank you for using this Attendance Syatem.")
        
