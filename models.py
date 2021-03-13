  
import os
from flask import Flask
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate

database_name = "agency"
database_path = os.environ['DATABASE_URL']
db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    
    migrate = Migrate(app, db)
    migrate.init_app(app, db)
    db.create_all()

class Movies(db.Model):  
  __tablename__ = 'movie'

  id = Column(Integer, primary_key=True)
  title = Column(String,unique=True)
  release_date = Column(String)


  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date


  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date,
    }

class Actors(db.Model):  
  __tablename__ = 'actor'

  id = Column(Integer, primary_key=True)
  name = Column(String,unique=True)
  gender = Column(String)
  age = Column(String)


  def __init__(self, name, gender,age):
    self.name = name
    self.gender = gender
    self.age = age


  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'gender': self.gender,
      'age':self.age,
    }

