from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

petApp = Flask(__name__)
petApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(petApp)
manager = APIManager(petApp, flask_sqlalchemy_db=db)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    species = db.Column(db.Unicode)
    weight = db.Column(db.Integer)
    age = db.Column(db.Integer)

db.create_all()
manager.create_api(Pet, methods=['GET', 'POST', 'DELETE'])
petApp.run()
