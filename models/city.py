#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
import models
from os import environ
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

<<<<<<< HEAD
=======

>>>>>>> 168a0ba9cb1e28b9d47a30884a73d0e53bbb58a8
class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship('Place', backref='cities', cascade='all, delete-orphan')
    else:
        state_id = ""
        name = ""
=======
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    places = relationship('Places', backref='cities', cascade='all')
>>>>>>> 23930bb2b4653485181bdb5643d77ce988e6e53f
