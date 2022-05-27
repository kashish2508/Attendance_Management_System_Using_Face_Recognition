from attendance import db, login_manager
from flask_login import UserMixin
from attendance import bcrypt


@login_manager.user_loader
def load_user(user_id):
    return Employeeusers.query.get(int(user_id))


class Employeeusers(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    emp_no = db.Column(db.Integer(), nullable=False, unique=True)
    emp_firstname = db.Column(db.String(length=30),
                              nullable=False, unique=True)
    emp_lastname = db.Column(db.String(length=30), nullable=False, unique=True)
    emp_photolocation = db.Column(db.String(length=10), nullable=False)
    emp_audiolocation = db.Column(db.String(length=10), nullable=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Attendance_IN(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    emp_no = db.Column(db.Integer(), nullable=False)
    emp_firstname = db.Column(db.String(length=30), nullable=False)
    emp_lastname = db.Column(db.String(length=30), nullable=False)
    date = db.Column(db.String(length=90), nullable=False)
    IN_time = db.Column(db.String(length=90), nullable=False)


class Attendance_OUT(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    emp_no = db.Column(db.Integer(), nullable=False)
    emp_firstname = db.Column(db.String(length=30), nullable=False)
    emp_lastname = db.Column(db.String(length=30), nullable=False)
    date = db.Column(db.String(length=90), nullable=False)
    OUT_time = db.Column(db.String(length=90), nullable=False)


class Bonus(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    emp_no = db.Column(db.Integer(), nullable=True)
    emp_firstname = db.Column(db.String(length=30), nullable=True)
    emp_lastname = db.Column(db.String(length=30), nullable=True)
    extra_hours = db.Column(db.Integer(), nullable=True)
    bonus = db.Column(db.Integer(), nullable=True)
