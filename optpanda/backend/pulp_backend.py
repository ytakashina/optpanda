from logging import getLogger

from pulp import LpVariable

logger = getLogger(__name__)


def init_model():
    logger.info("PuLP does not need a model before variable creation. Model initialization ignored.")
    return None


def get_model():
    logger.info("PuLP does not need a model before variable creation. Returns None.")
    return None


def set_model(model=None):
    logger.info("PuLP does not need a model before variable creation. Model assignment ignored.")


def variable(name, lb=None, ub=None, cat="Continuous", **kwargs):
    e = kwargs.get("e", None)
    return LpVariable(name, lowBound=lb, upBound=ub, cat=cat, e=e)
