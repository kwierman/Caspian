from dask.bag import Bag, from_sequence

import random

def sparse_bag(n_samples, n_cols):
    """ Generates a sparse bag of data

    Args:
        n_samples (int): _description_
        n_cols (int): _description_

    Returns:
        Bag: _description_
    """
    output = []
    schema = []
    for col in range(n_cols):
        schema.append( (f'col_{col}', 0.0) )
    for idx in range(n_samples):
        record = {'idx':idx}
    
        # select the number of samples in this record
        n_samples = random.randrange( n_cols) + 1
        choices = random.choices(schema, k=n_samples)
        for choice in choices:
            record[choice[0]] = random.uniform(0, 100.)
        output.append(record)
    return from_sequence(output)