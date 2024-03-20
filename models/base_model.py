#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import models
__tablename__ = 'base_models'

Base = declarative_base()

class BaseModel(Base):
    """Create Base = declarative_base() before the class definition of BaseModel"""
    __tablename__ = base_models
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)

    def __init__(self, *args, **kwargs):
        """ init constructor"""
        super().__init__(*args, **kwargs)

    def save(self):
        """save storage """
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ to dictionary """
        dict_obj = self.__dict__.copy()
        dict_obj.pop(_sa_instance_state, None)
        return dict_obj

    def delete(self):
        """ delete a storage """
        models.storage.delete(self)
