try:
    from gurobipy import Var
except ModuleNotFoundError:
    pass

_MODEL = None


def init_model():
    raise NotImplementedError()


def get_model():
    raise NotImplementedError()


def set_model(model=None):
    raise NotImplementedError()


def variable(name, lb=None, ub=None, cat="Continuous", **kwargs):
    raise NotImplementedError()
