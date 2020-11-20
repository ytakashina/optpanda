try:
    from gurobipy import Var
except ModuleNotFoundError:
    pass

_MODEL = None


def backend():
    return "gurobipy"


def model():
    raise NotImplementedError()


def set_model():
    raise NotImplementedError()


def variable(name, lb=None, ub=None, cat="Continuous", **kwargs):
    raise NotImplementedError()
