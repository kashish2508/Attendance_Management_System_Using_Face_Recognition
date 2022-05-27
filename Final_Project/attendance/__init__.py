from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SECRET_KEY'] = "b'\x07~\x91\xbb\xaa\x10\x82w\xe5G\x01\x1dV\xf0\xcf_\xb8K\xab>S\xc7\x10y'"
login_manager = LoginManager(app)
login_manager.init_app(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from attendance import routes

