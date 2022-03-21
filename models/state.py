#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              cascade="all, delete-orphan",
                              backref="state")
    else:
        @property
        def cities(self):
            """
            returns a list of all cities in state
            """
            return [c for c in models.storage.all(City).values()
                    if c.state_id == self.id]

