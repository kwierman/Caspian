from .base import Warehouse
from sqlalchemy import create_engine

class SQLiteWarehouse(Warehouse):

    def __init__(self, location):
        super().__init__(location)
        self.__engine__ = create_engine(self.location, echo=True)