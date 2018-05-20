from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#secret key for csrf
app.config['SECRET_KEY'] = 'd65cee974fbbc376f5d5866c69dade58'
#db setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from porder import routes