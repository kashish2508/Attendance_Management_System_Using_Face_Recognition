from django.shortcuts import redirect
from requests import request
from attendance import app
from attendance import db
from attendance.main_out import attendanceout
from attendance.models import Employeeusers
from flask import session,render_template,request,redirect,g,url_for,flash
from attendance.forms import RegisterForm,LoginForm
from flask_login import login_user,login_required
from attendance.main_in import attendancein
from attendance.main_out import attendanceout

@app.route("/")
def home_page():
   return render_template('home.html')

@app.route("/attendance/IN")
def attendance_in():
   return attendancein()

@app.route("/attendance/OUT")
def attendance_out():
   return attendanceout()

@app.route("/done")
@login_required
def done_page():
   return render_template('done.html')

   
@app.route("/adminlogin",methods=['GET','POST'])
def  adminlogin():
   if request.method== 'POST':
      session.pop('user',None)

      if request.form['password']=='password@kashu':
         session['user'] = request.form['username']
         flash(f'Success! You are logged in as Admin_25', category='success')
         return redirect(url_for('registration'))
      else:
            flash('Username and password are not match! Please try again', category='danger')   
   
   return render_template('adminlogin.html')

@app.route('/registration',methods=['GET','POST'])
def registration():
   form = RegisterForm()
   if g.user:
      if form.validate_on_submit():
        user_to_create = Employeeusers(emp_no=form.emp_no.data,emp_firstname=form.emp_firstname.data,emp_lastname=form.emp_lastname.data,emp_photolocation=form.emp_photolocation.data,emp_audiolocation=form.emp_audiolocation.data,username=form.username.data,password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        flash(f'Successfully registered new employee!', category='success')
        return redirect(url_for('registration'))
      if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')
      return render_template('registration.html', user=session['user'], form=form)
   return redirect(url_for('adminlogin'))
     

@app.before_request
def before_request():
   g.user = None

   if 'user' in session:
      g.user = session['user']

@app.route('/dropsession')
def dropsession():
   session.pop('user',None)
   flash("You have been logged out!", category='info')
   return render_template('home.html')      


@app.route('/employeelogin', methods=['GET', 'POST'])
def employeelogin():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Employeeusers.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('done_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('employeelogin.html', form=form)



