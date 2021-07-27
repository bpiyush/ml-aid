"""
Utilities for simple pythonic operations.
"""
from typing import List, Any
from functools import reduce
import operator


def get_from_dict(dataDict: dict, mapList: List):
    """
    Returns value from a dict based on list of keys.
    E.g., for dict D, keys=[a, b, c], it will return D[a][b][c]
    Credits: https://stackoverflow.com/questions/14692690/access-nested-dictionary-items-via-a-list-of-keys

    Args:
        dataDict (dict): input dictionary
        mapList (List): list of keys to be accessed

    Returns:
        Any: value from the dict based on given keys
    """
    return reduce(operator.getitem, mapList, dataDict)


def set_in_dict(dataDict: dict, mapList: List, value: Any):
    """
    Replaces given value in a dict based on list of keys.
    E.g., for dict D, keys=[a, b, c], it will set D[a][b][c] = value
    Note that this is in-place replacement

    Credits: https://stackoverflow.com/questions/14692690/access-nested-dictionary-items-via-a-list-of-keys

    Args:
        dataDict (dict): input dictionary
        mapList (List): list of keys to be accessed
        value (Any): value to be replaced
    """
    get_from_dict(dataDict, mapList[:-1])[mapList[-1]] = value
