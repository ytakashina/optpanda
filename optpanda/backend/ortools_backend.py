def variable(name, lb=None, ub=None, cat="Continuous", **kwargs):
    raise NotImplementedError()


def model():
    raise NotImplementedError()


def set_model():
    raise NotImplementedError()


def dtype():
    raise NotImplementedError()


def backend():
    return 'ortools'
