#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            'City', backref='states',
            cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """
            returns a list of all City instances
            """
            return models.storage.all(City).values()
