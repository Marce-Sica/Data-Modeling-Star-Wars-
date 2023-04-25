import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'Characters'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    BirthYear = Column(String(50), nullable=False)
    Gender = Column(String(50), nullable=False)
    EyesColor = Column(String(50), nullable=False)
    Skin = Column(String(50), nullable=False)
    Height = Column(String(50), nullable=False)
    pass

class Planets(Base):
    __tablename__ = 'Planets'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Gravity = Column(String(50), nullable=False)
    Terrain = Column(String(50), nullable=False)
    Climate = Column(String(50), nullable=False)
    OrbitalPeriod = Column(String(50), nullable=False)
    Population = Column(String(50), nullable=False)
    Diameter = Column(String(50), nullable=False)
    pass

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    ID = Column(Integer, primary_key=True)
    Model = Column(String(50), nullable=False)
    Length = Column(String(50), nullable=False)
    MaxSpeed = Column(String(50), nullable=False)
    CargoCapacity = Column(String(50), nullable=False)
    Class = Column(String(50), nullable=False)
    Manufacture = Column(String(100), nullable=False)
    pass

class Favorites(Base):
    __tablename__ = 'Favorites'
    ID = Column(Integer, primary_key=True)
    Characters_id = Column(Integer, ForeignKey('Characters.id'))
    Planets_id = Column(Integer, ForeignKey('Planets.id'))
    Vehicles_id = Column(Integer, ForeignKey('Vehicles.id'))
    pass


class User(Base):
    __tablename__ = 'User'
    UserID = Column(Integer, primary_key=True)
    FirstName = Column(String(50), nullable=False)
    LastName = Column(String(50), nullable=False)
    UserName = Column(String(50), nullable=False)
    Email = Column(String(50), nullable=False)
    Password= Column(Integer, primary_key=True)
    Favorites_id = Column(Integer, ForeignKey('Favorites.id'))
    pass

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
