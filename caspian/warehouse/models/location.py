import dataclasses
from .base import Model, Field, Integer, String
from dataclasses import dataclass


class Location(Model):
    __tablename__ = 'datalake_location'

    id = Field(Integer, primary_key=True)
    uri = Field(String)


    

