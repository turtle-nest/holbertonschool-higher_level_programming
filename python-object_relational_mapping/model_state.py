#!/usr/bin/python3
"""
Module that contains class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    """int: Unique identifier for the state. Primary key, cannot be null."""
    name = Column(String(128), nullable=False)
    """str: Name of the state. Cannot be null."""

