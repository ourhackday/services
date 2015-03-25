from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

petApp = Flask(__name__)
petApp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(petApp)
manager = APIManager(petApp, flask_sqlalchemy_db=db)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.Unicode, db.ForeignKey('species.id'))
    owner = db.Column(db.Integer, db.ForeignKey('owner.id'))
    name = db.Column(db.Unicode)
    weight = db.Column(db.Integer)
    age = db.Column(db.Integer)
    description = db.Column(db.Unicode)
    favefood = db.Column(db.Unicode)
    favetoy = db.Column(db.Unicode)

class Species(db.Model):
    id = db.Column(db.Unicode, primary_key=True)
    description = db.Column(db.Unicode)

class Tracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet = db.Column(db.Integer, db.ForeignKey('pet.id'))
    time = db.Column(db.DateTime)
    lat_start = db.Column(db.Integer)
    long_start = db.Column(db.Integer)
    lat_end = db.Column(db.Integer)
    long_end = db.Column(db.Integer)
    distance = db.Column(db.Float)

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    town = db.Column(db.Unicode)
    age = db.Column(db.Unicode)

class Advice(db.Model):
    id = db.Column(db.Unicode, primary_key=True)
    species = db.Column(db.Unicode, db.ForeignKey('species.id'))
    question = db.Column(db.Unicode)
    answer = db.Column(db.Unicode)

db.create_all()
manager.create_api(Pet, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Species, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Tracking, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Owner, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Advice, methods=['GET', 'POST', 'DELETE'])
petApp.debug = True
petApp.run(host="0.0.0.0", port=5000)
