from dask.distributed import get_client
from dask.bag import Bag
from typing import Dict, Union, List
from uuid import uuid4

schema_type = Dict[str, type]


def wide_records_to_long_records(record: dict)-> List[Dict]:
    """Take in wide records and turns them into long records

    Args:
        record (dict): _description_

    Returns:
        List[Dict]: _description_
    """
    output = []

    for key, value in record.items():
        output.append({'key':key, 'value': value})
    return output


def infer_schema_from_bag(bag: Bag, index_col: str, n_samples: Union[int, None] = None) -> schema_type:
    """Infers the schema of the dictionary-encoded items in the databag (assumes the bag is a collection of dictionaries representing records)

    Args:
        bag (Bag): The dask bag to operate on
        index_col (str): If, there is an index column, make sure to omit this.

    Returns:
        schema_type: A dictionary representing the key and value-type of the items in the records
    """

    if n_samples is not None:
        bag = bag.take(n_samples)

    bag = bag.map(wide_records_to_long_records).flatten()
    schema = bag.distinct('key').map(lambda x: {'key':x['key'], 'type': type(x['value'])}).compute()
    output = {}
    for item in schema:
        output[item['key']] = item['type']
    if index_col in output.keys():
        del output[index_col]

    return output


def bag_to_column(bag: Bag, col_name: str, col_type: str ):
    """ Take in a bag and reduces it to the column name and type and then outputs 

    Args:
        bag (_type_): _description_
        col_name (_type_): _description_
        col_type (_type_): _description_
    """
    ...


def write_bag_to_columnar_dataset( bag, location, index_col=None, schema=None, n_samples=None):
    """ Writes a bag to a columnar dataset

    Args:
        bag (_type_): _description_
        location (_type_): _description_
        index_col (_type_, optional): _description_. Defaults to None.
        schema (_type_, optional): _description_. Defaults to None.
        n_samples (_type_, optional): _description_. Defaults to None.
    """
    if schema is None:
        schema = infer_schema_from_bag(bag, index_col=index_col, n_samples=n_samples)

    client = get_client()
