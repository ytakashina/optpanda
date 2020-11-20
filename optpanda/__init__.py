from importlib import reload
from os import environ

import optpanda.backend
from ._varseries import from_index, create


def set_backend(name: str):
    environ['OPTPANDA_BACKEND'] = name
    reload(optpanda.backend)


__all__ = [
    "set_backend",
    "from_index",
    "create",
]
