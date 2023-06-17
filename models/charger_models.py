from app.extensions import db
from sqlalchemy import DECIMAL
from pydantic import BaseModel


class Record(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    barcode = db.Column(db.Integer, unique=True)
    params_id = db.Column(db.Integer, db.ForeignKey('parameters.id'))
    datetime = db.Column(db.DateTime)
    parameters = db.relationship('Parameters', backref='record')


class Parameters(db.Model):
    __tablename__ = 'parameters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    temp_id = db.Column(db. Integer, db.ForeignKey('temperature.id'))
    voltage_id = db.Column(db. Integer, db.ForeignKey('voltage.id'))
    current_id = db.Column(db. Integer, db.ForeignKey('current.id'))

    temperature = db.relationship('Temperature', backref='parameters')
    voltage = db.relationship('Voltage', backref='parameters')
    current = db.relationship('Current', backref='parameters')


class Temperature(db.Model):
    __tablename__ = 'temperature'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    temperature = db.Column(DECIMAL(precision=4, scale=1))


class Voltage(db.Model):
    __tablename__ = 'voltage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    voltage = db.Column(DECIMAL(precision=3, scale=2))


class Current(db.Model):
    __tablename__ = 'current'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    current = db.Column(db.Integer)
