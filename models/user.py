#!/usr/bin/python3
"""User inherits from BaseModel and Base (respect the order)"""
from sqlalchemy import Column, String
from .base_model import BaseModel, Base


class User(BaseModel, Base):
    """
    Represents a user in the system.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str, optional): The first name of the user.
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
