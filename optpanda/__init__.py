from importlib import reload
from os import environ

import optpanda.backend


def set_backend(name: str):
    environ['OPTPANDA_BACKEND'] = name
    reload(optpanda.backend)
