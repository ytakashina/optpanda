try:
    from gurobipy import Var
except ModuleNotFoundError:
    pass

_MODEL = None


def variable(name, lb=None, ub=None, cat="Continuous", **kwargs):
    raise NotImplementedError()


def model():
    raise NotImplementedError()


def dtype():
    return Var
