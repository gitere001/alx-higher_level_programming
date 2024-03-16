#!/usr/bin/python3
"""
contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base


class City(Base):
    """City class

    Attributes:
        __tablename__(str): the table name of class
        id(int):the id of the class
        name (str): the name the class
        state_id (int): the state id the city belong

    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
