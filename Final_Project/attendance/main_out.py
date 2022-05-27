from attendance.models import Bonus
from attendance.models import Attendance_IN
from attendance.models import Attendance_OUT
from attendance import db
from playsound import playsound
import pygame
import datetime
import face_recognition
import cv2
from PIL import Image, ImageDraw, ImageFont
import sys
from flask import render_template
import pandas as pd
from datetime import date
from datetime import datetime
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


# reading data file.

def attendanceout():

    emp_file = pd.read_csv(
        'C:\\Users\\KIIT\\OneDrive\\Desktop\\Final_Project\\attendance\\Data_files\\Employee_details.csv')

# convering each column of data file into python string using tolist() method.

    emp_no = emp_file["EMPLOYEE_NUMBER"].tolist()
    emp_firstname = emp_file["FIRST_NAME"].tolist()
    emp_lastname = emp_file["LAST_NAME"].tolist()
    emp_photolocation = emp_file["PHOTO_LOCATION"].tolist()
    emp_audiolocation = emp_file["AUDIO_LOCATION"].tolist()

    n = len(emp_no)  # total number of employee.

# creating empty string to store image of all employee, encoding of all employee face and audio for all employee respectively.

    emp_image = []
    emp_enco = []
    emp_audio = []

# for all employee from there photo location we are loading image in list emp_image and encoding of each employee in list emp_enco.

    for i in range(n):
        emp_image.append(
            face_recognition.load_image_file(emp_photolocation[i]))
        emp_enco.append(face_recognition.face_encodings(emp_image[i])[0])

# ----------------module2-------------------------

# to capture image and camera object is created

    camera = cv2.VideoCapture(0)

# camera will capture 10 images and then we will select middle image to increase accuracy.

    for i in range(10):
        return_value, image = camera.read()  # capture image
        cv2.imwrite('C:\\Users\\KIIT\\OneDrive\\Desktop\\Final_Project\\captured_images\\Employee' +
                    str(i)+'.png', image)  # store image
    camera.release()
    cv2.destroyAllWindows()
    del(camera)

    captured_image = face_recognition.load_image_file(
        'C:\\Users\\KIIT\\OneDrive\\Desktop\\Final_Project\\captured_images\\Employee5.png', 'RGB')


# method to recognise the captured image and retures the index of matched employee and if employee not found -1 will be returned

    def identify_employee(photo):
        try:
            captured_image_enco = face_recognition.face_encodings(photo)[0]
        except IndexError as e:
            print(e)
            sys.exit(1)
        found = face_recognition.compare_faces(
            emp_enco, captured_image_enco, tolerance=0.5)
        print(found)

        index = -1
        for i in range(n):
            if found[i]:
                index = i
        return(index)

    emp_index = identify_employee(captured_image)  # function call

# Attendance record in a attendance_out and bonus calculation
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    if (emp_index != -1):
        x = str(date.today())
        y = str(current_time)
        t1 = y
        emp1 = Attendance_OUT(emp_no=emp_no[emp_index], emp_firstname=emp_firstname[emp_index],
                              emp_lastname=emp_lastname[emp_index], date=x, OUT_time=y)
        db.session.add(emp1)
        db.session.commit()
        for i in Attendance_IN.query.filter_by(date=x, emp_no=emp_no[emp_index]):
            t2 = i.IN_time

        h = abs(((int(t1[0])*10)+int(t1[1]))-((int(t2[0])*10)+int(t2[1])))
        m = abs(((int(t1[3])*10)+int(t1[4]))-((int(t2[3])*10)+int(t2[4])))

        time = h+m*0.0167
        extra = time-8.00
        tx = "{:.2f}".format(extra)

        if(extra > 0.5):

            bonus = "{:.0f}".format(extra*250)
        if(extra <= 0.5):
            tx = 0
            bonus = 0

        bonus1 = Bonus(emp_no=emp_no[emp_index], emp_firstname=emp_firstname[emp_index],
                       emp_lastname=emp_lastname[emp_index], extra_hours=tx, bonus=bonus)
        db.session.add(bonus1)
        db.session.commit()


# Module 5 Display Attendance Module
    pil_captured_image = Image.fromarray(captured_image)
    draw = ImageDraw.Draw(pil_captured_image)
    fnt = ImageFont.truetype("arial.ttf", 40)

    if emp_index == -1:
        name = "Face NOT Recognized"

    else:

        name = emp_firstname[emp_index]+" "+emp_lastname[emp_index]
        number = "\n"+str(emp_no[emp_index])
    x = 100
    y = captured_image.shape[0] - 100
    draw.text((x, y), name, font=fnt, fill=(255, 0, 0))
    if emp_index != -1:
        draw.text((x, y), number, font=fnt, fill=(255, 0, 0))
    pil_captured_image.show()

# Module 6 Announce Attendance Recorded Module
    audioloc = emp_audiolocation[emp_index]
    pygame.mixer.init()
    if emp_index == -1:
         playsound("C:\\Users\\KIIT\\OneDrive\\Desktop\\Final_Project\\attendance\\Data_files\\Employee_audios\\Fnotrecognised.mp3")
    else:
        playsound(audioloc)

    return render_template('done.html')
