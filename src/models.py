import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Films (Base):
    """Films"""
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    title = Column(String(120), unique=True, nullable=False)
    episode_id = Column(Integer)
    opening_crawl = Column(String(120))
    director = Column(String(120), nullable=False)
    producer = Column(String(120), nullable=False)
    release_date = Column(DateTime(timezone=False))
    created = Column(DateTime)
    edited = Column(DateTime)

class SpeciesByFilm (Base):
    __tablename__='speciesbyfilm'
    id = Column(Integer, primary_key = True)
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship('Films')
    species_id = Column(Integer, ForeignKey('species.id'))
    specie = relationship('Species')

class StarshipsByFilm (Base):
    __tablename__='starshipsbyfilm'
    id = Column(Integer, primary_key = True)
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship('Films')
    starship_id = Column(Integer, ForeignKey('starship.id'))
    starship = relationship('Starships')

class VehiclesByFilm (Base):
    __tablename__='vehiclesbyfilm'
    id = Column(Integer, primary_key = True)
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship('Films')
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship('Vehicles')

class CharactersByFilm (Base):
    __tablename__='charactersbyfilm'
    id = Column(Integer, primary_key = True)
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship('Films')
    character_id = Column(Integer, ForeignKey('characters.id'))
    vehicle = relationship('Characters')

class PlanetsByFilm (Base):
    __tablename__='planetsbyfilm'
    id = Column(Integer, primary_key = True)
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship('Films')
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planets')



class Characters (Base):
    """Characters"""
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    birth_year = Column(String(50))
    eye_color = Column(String(50))
    gender = Column(String(50))
    hair_color = Column(String(50))
    height = Column(String(50))
    mass = Column(String(50))
    skin_color = Column(String(50))
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    created = Column(DateTime(timezone=False))
    edited = Column(DateTime(timezone=False))
    planets = relationship('Planets')


class SpeciesByCharacter(Base):
    __tablename__='speciesbycharacter'
    id = Column(Integer, primary_key = True)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship('Characters')
    specie_id = Column(Integer, ForeignKey('species.id'))
    specie = relationship('Species')

class StarshipsByCharacter(Base):
    __tablename__='starshipsbycharacter'
    id = Column(Integer, primary_key = True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship('Characters')
    starship_id = Column(Integer, ForeignKey('starships.id'))
    starship = relationship('Starships')

class VehiclesByCharacter(Base):
    __tablename__='vehiclesbycharacter'
    id = Column(Integer, primary_key = True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    character = relationship('Characters')
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship('Vehicles')


class Planets(Base):
    """Planets"""
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    diameter = Column(String(120))
    rotation_period = Column(String(120))
    orbital_period = Column(String(120))
    gravity = Column(String(120))
    population = Column(String(120))
    climate = Column(String(120))
    terrain = Column(String(120))
    surface_water = Column(String(120))
    specie_id = Column(Integer, ForeignKey('species.id'))
    specie = relationship('Species')
    created = Column(DateTime(timezone=False))
    edited = Column(DateTime(timezone=False))


class Starships (Base):
    """Starships"""
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    model = Column(String(120))
    starship_class = Column(String(120))
    manufacturer = Column(String(120))
    cost_in_credits = Column(String(120))
    length = Column(String(120))
    crew = Column(String(120))
    passengers = Column(String(120))
    max_atmosphering_speed = Column(String(120))
    hyperdrive_rating = Column(String(120))
    MGLT = Column(String(120))
    cargo_capacity = Column(String(120))
    consumables = Column(String(120))
    created = Column(DateTime)
    edited = Column(DateTime)


class Vehicles (Base):
    """Vehicles"""
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    model = Column(String(120))
    vehicle_class = Column(String(120))
    manufacturer = Column(String(120))
    length = Column(String(120))
    cost_in_credits = Column(String(120))
    crew = Column(String(120))
    passengers = Column(String(120))
    max_atmosphering_speed = Column(String(120))
    cargo_capacity = Column(String(120))
    consumables = Column(String(120))
    created = Column(DateTime)
    edited = Column(DateTime)


class Species (Base):
    """Species"""
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    classification = Column(String(120))
    designation = Column(String(120))
    average_height = Column(String(120))
    average_lifespan = Column(String(120))
    eye_colors = Column(String(120))
    hair_colors = Column(String(120))
    skin_colors = Column(String(120))
    language = Column(String(120))
    homeworld = Column(Integer, ForeignKey('planet.id'))
    planet = relationship('Planets')
    created = Column(DateTime)
    edited = Column(DateTime)


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
