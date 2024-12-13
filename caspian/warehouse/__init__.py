from .local import SQLiteWarehouse
from .remote import RemoteWareHouse
from .base import Warehouse

def warehouse_factory(location: str) -> Warehouse:
    if location.startswith('sqlite'):
        return SQLiteWarehouse(location)
    elif location.startwith('postgres'):
        return RemoteWareHouse(location)
    raise ValueError('Currently Caspian only supports sqlite and postgres warehouses')