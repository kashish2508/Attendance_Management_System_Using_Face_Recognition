# Attendance_Management_System_Using_Face_Recognition
Facial recognition student attendance system using OpenCV ,python and flask
This project involves building an attendance system which utilizes facial recognition to mark the presence, time-in, and time-out of employees. It covers areas such as facial detection, alignment, and recognition, along with the development of a web application to cater to various use cases of the system such as registration of new employees. This project intends to serve as an efficient substitute for traditional manual attendance systems. It can be used in corporate offices, schools, and 
organizations where security is essential.This project aims to automate the traditional attendance system where the attendance is marked manually. It also enables an organization to maintain its records like in-time, out time and Bonus. 

## Scope of the project :

Facial recognition is becoming more prominent in our society. It has made major progress in the field of security. It is a very effective tool that can help low 
enforcers to recognize criminals and software companies are leveraging the technology to help users access the technology. This technology can be further developed to be used in other avenues such as ATMs, accessing confidential files, or other sensitive materials. This project servers as a foundation for future projects based on facial detection and recognition. This project also convers web development and database management with a user-friendly UI. Using this system any corporate offices, school and organization can replace their traditional way of maintaining attendance of the employees and also calculate bonus amount for employees daily if they work extra.

## The system mainly works around 2 types of users

1.Admin <br>
2.Employee <br>
ADMIN:- <br>
 The username and password of admin is fixed. <br>
               username-Admin_25 <br>
               password-password@kashu <br>
## Following functionalities can be performed by the admin:
• Login <br>
• Register new employees to the system. <br>
• Set the username and password of employee. <br>

EMPLOYEE:- <br>
 username of employee 1=Kashish_20001 <br>
              password =kashish@123 <br>
## Following functionalities can be performed by the employee: <br>
• Login <br>
• Mark his/her time-in and time-out by scanning their face <br>

## steps to register new employee: <br>
1.upload the image of employee in folder Employee_images present in folder Data_files in directory attendance. <br>
2.upload the audio of employee in folder Employee_images present in folder Data_files in directory attendance. <br>
3.now enter the details of employee in CSV file (Employee_details)present in folder Data_files in directory attendance. <br>
   NOTE:carefully copy the complete path of employee image and audio in csv file. <br>
4.now admin will register the employee using registration page and set username and password of the employee. v
  employee will use that username and password for login to mark their attendance. <br>
  
## steps to view tables store in sqlite3 databse
1.https://inloop.github.io/sqlite-viewer/ go to this link. <br>
2.upload data.db here which is present inside attendace folder. you will get 4 tables.(employeesuser,attendance_in,attendance_out,bonus). <br>
  
## How To Run ?  
1.download the folder Final_project on your computer(in desktop) <br>
2.open directory Final_project incommand prompt. <br>
3.run **``` pip install -r requirements.txt inside Final_project ```** directory <br>
4.Run **``` python run.py ```** inside **``` Final_project ```** directory to run the project <br>
  imp note:- carefully check all the path of files in main_in.py and main_out.py and set them according to the complete path of your folders Or file.
