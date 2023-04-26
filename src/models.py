import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    eyes_color = Column(String(50), nullable=False)
    skin = Column(String(50), nullable=False)
    height = Column(String(50), nullable=False)
    pass

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gravity = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    orbital_period = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)
    diameter = Column(String(50), nullable=False)
    pass

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String(50), nullable=False)
    length = Column(String(50), nullable=False)
    max_speed = Column(String(50), nullable=False)
    cargo_capacity = Column(String(50), nullable=False)
    class_ = Column(String(50), nullable=False)
    manufacture = Column(String(100), nullable=False)
    pass

class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('Characters.id'))
    planets_id = Column(Integer, ForeignKey('Planets.id'))
    vehicles_id = Column(Integer, ForeignKey('Vehicles.id'))
    pass


class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    user_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password= Column(Integer, primary_key=True)
    favorites_id = Column(Integer, ForeignKey('Favorites.id'))
    pass

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
