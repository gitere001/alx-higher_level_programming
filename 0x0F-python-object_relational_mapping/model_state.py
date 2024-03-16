#!/usr/bin/python3
"""
Defines State class and Base class to work with SQLAlchemy ORM
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class

    Attributes:
    __tablename__ (str): The table name of the class
    id (int): The state ID of the class
    name (str): The state name of the class
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
