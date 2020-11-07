from logging import getLogger

from pulp import LpVariable

logger = getLogger(__name__)


def variable(name, lb=None, ub=None, cat="Continuous", **kwargs):
    e = kwargs.get("e", None)
    return LpVariable(name, lowBound=lb, upBound=ub, cat=cat, e=e)


def model():
    logger.info("PuLP does not need a model before variable creation. Ignored.")
    return None


def set_model():
    logger.info("PuLP does not need a model before variable creation. Ignored.")


def dtype():
    return LpVariable


def backend():
    return 'pulp'