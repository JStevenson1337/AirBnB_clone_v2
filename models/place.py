#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String, Float, Table


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place")
    amenities = relationship("Amenity", secondary='place_amenity',
                             viewonly=False, backref='place_amenities')
    amenity_ids = []

    @property
    def amenities(self):
        """returns list of amentity ids"""
        return self.amenity_ids

    @amenities.setter
    def amenities(self, val):
        """appends to amenity_id list"""
        self.amenity_id.append(val)

    @property
    def reviews(self):
        """returns list of revies with shared pace_ids"""
        return self.reviews
