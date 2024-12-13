from sqlalchemy import create_engine, Engine

from .models import Base

import logging

class Warehouse(object):

    def __init__(self, location):
        if location is None:
            location = "sqlite+pysqlite:///:memory:"
        self.location = location
        self.__engine__ = None

    def initialize(self):
        """_summary_
        """
        Base.metadata.create_all(self.engine)

    @property
    def engine(self) -> Engine:
        if self.__engine__ is None:
            self.__engine__ = create_engine(self.location, echo=True)
        return self.__engine__

