from importlib import reload
from os import environ

import optpanda.backend
from ._varseries import from_index, variable, variables


def set_backend(name: str):
    environ['OPTPANDA_BACKEND'] = name
    reload(optpanda.backend)


def get_backend():
    return optpanda.backend._BACKEND


__all__ = [
    "get_backend",
    "set_backend",
    "from_index",
    "variable",
    "variables",
]
