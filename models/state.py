#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if models.storage_type != 'db':
        @property
        def cities(self):
            """Getter method for cities"""
            from models import storage
            cities_list = []
            all_cities = storage.all('City').values()
            for city in all_cities:
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
    else:
        cities = relationship("City", backref="state", cascade="all, delete")
