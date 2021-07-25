"""
Utilities for input-output loading/saving.
"""

from typing import Any
import pickle
import yaml


class PrettySafeLoader(yaml.SafeLoader):
    """Custom loader for reading YAML files"""
    def construct_python_tuple(self, node):
        return tuple(self.construct_sequence(node))


PrettySafeLoader.add_constructor(
    u'tag:yaml.org,2002:python/tuple',
    PrettySafeLoader.construct_python_tuple
)


def load_yml(path: str, loader_type: str = 'default'):
    """Read params from a yml file.

    Args:
        path (str): path to the .yml file
        loader_type (str, optional): type of loader used to load yml files. Defaults to 'default'.

    Returns:
        Any: object (typically dict) loaded from .yml file
    """
    assert loader_type in ['default', 'safe']

    loader = yaml.Loader if (loader_type == "default") else PrettySafeLoader

    with open(path, 'r') as f:
        data = yaml.load(f, Loader=loader)

    return data


def save_yml(data: dict, path: str):
    """Save params in the given yml file path.

    Args:
        data (dict): data object to save
        path (str): path to .yml file to be saved
    """
    with open(path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


def load_pkl(path: str, encoding: str = "ascii") -> Any:
    """Loads a .pkl file.

    Args:
        path (str): path to the .pkl file
        encoding (str, optional): encoding to use for loading. Defaults to "ascii".

    Returns:
        Any: unpickled object
    """
    return pickle.load(open(path, "rb"), encoding=encoding)


def save_pkl(data: Any, path: str) -> None:
    """Saves given object into .pkl file

    Args:
        data (Any): object to be saved
        path (str): path to the location to be saved at
    """
    with open(path, 'wb') as f:
        pickle.dump(data, f)
