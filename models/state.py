#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    state = relationship('City', cascade='all, delete') backref="state")

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
    @property
    def cities(self):
        """Getter attribute for cities in FileStorage"""
        from models import storage
        cities_list = []
        for city in storage.all("City").values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list

