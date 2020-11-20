from importlib import reload
from os import environ

import optpanda.backend
from optpanda.backend import variable
from ._varseries import from_index, variables


def set_backend(name: str):
    environ['OPTPANDA_BACKEND'] = name
    reload(optpanda.backend)


__all__ = [
    "set_backend",
    "from_index",
    "variable",
    "variables",
]
