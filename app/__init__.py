import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://pro2:pro2@localhost/pro2'

db = SQLAlchemy(app)
db.create_all()

from app import views, models