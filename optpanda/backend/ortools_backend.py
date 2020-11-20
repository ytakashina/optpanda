from logging import getLogger
from typing import Optional

from ortools.linear_solver.pywraplp import Solver

logger = getLogger(__name__)

_MODEL: Optional[Solver] = None


def init_model():
    global _MODEL
    _MODEL = Solver("No name", Solver.CBC_MIXED_INTEGER_PROGRAMMING)


def get_model():
    return _MODEL


def set_model(model=None):
    global _MODEL
    _MODEL = model


def variable(name, lb=None, ub=None, cat="Continuous", **kwargs):
    # TODO: 予期しない cat を除外するロジックは他の backend と共通化。
    lb = lb if lb is not None else 0
    ub = ub if ub is not None else _MODEL.infinity()
    if cat == "Continuous":
        return _MODEL.NumVar(float(lb), float(ub), name)
    if cat == "Binary":
        return _MODEL.BoolVar(name)
    if cat == "Integer":
        return _MODEL.IntVar(lb, ub, name)
    raise ValueError(f"{cat} is not supported for ``cat``.")
