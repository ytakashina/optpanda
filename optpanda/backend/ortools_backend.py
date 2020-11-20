def backend():
    return "ortools"


def model():
    raise NotImplementedError()


def set_model():
    raise NotImplementedError()


def variable(name, lb=None, ub=None, cat="Continuous", **kwargs):
    raise NotImplementedError()
