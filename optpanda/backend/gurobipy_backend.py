try:
    from gurobipy import Var
except ModuleNotFoundError:
    pass

_MODEL = None
