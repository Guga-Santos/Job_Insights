import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, mode="r") as data:
        data_result = csv.DictReader(data)
        return[*data_result]
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
