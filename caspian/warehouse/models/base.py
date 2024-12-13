from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Date, Integer, String
from dataclasses import dataclass

Base = declarative_base()


@dataclass
class Model(Base):
    ...


Field = Column
