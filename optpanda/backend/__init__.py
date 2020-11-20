from logging import getLogger
from os import environ

logger = getLogger(__name__)

if 'OPTPANDA_BACKEND' in environ:
    _backend = environ['OPTPANDA_BACKEND']
    assert _backend in {'pulp', 'ortools'}
    _BACKEND = _backend
else:
    _BACKEND = 'pulp'

# TODO: gurobipy support
if _BACKEND == 'pulp':
    logger.info("PuLP backend loaded.")
    from .pulp_backend import *
elif _BACKEND == 'ortools':
    # logger.info("OR-Tools backend loaded.")
    logger.error("OR-Tools backend is not supported currently.")
    from .ortools_backend import *
elif _BACKEND == 'gurobipy':
    # logger.info("Gurobi Python API backend loaded.")
    logger.error("Gurobi Python API backend is not supported currently.")
    from .gurobipy_backend import *
else:
    raise ValueError('Unknown backend: ' + str(_BACKEND))

__all__ = [
    "variable",
    "backend",
    "model",
    "set_model",
]
