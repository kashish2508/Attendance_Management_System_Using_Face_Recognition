from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FileField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError
from attendance.models import Employeeusers


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = Employeeusers.query.filter_by(
            username=username_to_check.data).first()
        if user:
            raise ValidationError(
                'Username already exists! Please try a different username')
    emp_no = IntegerField(label='Employee Number:',
                          validators=[DataRequired()])
    emp_firstname = StringField(
        label='First Name:', validators=[DataRequired()])
    emp_lastname = StringField(label='Last Name:', validators=[DataRequired()])
    emp_photolocation = FileField(
        label='Upload Photo:', validators=[DataRequired()])
    emp_audiolocation = FileField(
        label='Upload Audio:', validators=[DataRequired()])
    username = StringField(label='User Name:', validators=[
                           Length(min=2, max=30), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[
                              Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[
                              EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Register')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
