import numpy as np
import pandas as pd
from pandas import Series
from pandas.core.dtypes.common import is_list_like

import optpanda.backend as B


def from_index(name, index: pd.Index, lb=None, ub=None, cat="Continuous", **kwargs):
    if not isinstance(index, pd.Index):
        raise ValueError("index must be a pandas.Index.")

    if not isinstance(lb, np.number):
        if not isinstance(lb, pd.Series):
            raise ValueError("lb must be a Series if not a scalar.")
        if not index.equals(lb.index):
            raise ValueError("lb must have the same index with index if it is a Series.")

    if not isinstance(ub, np.number):
        if not isinstance(ub, pd.Series):
            raise ValueError("ub must be a Series if not a scalar.")
        if not index.equals(ub.index):
            raise ValueError("ub must have the same index with index if it is a Series.")

    values = [B.variable(f"{name}[{i}]", lb, ub, cat, **kwargs) for i in index]
    return pd.Series(values, index, name=name, dtype=B.dtype())


def create(name, index, fix=None, lb=None, ub=None, cat="Continuous", **kwargs):
    # TODO: fix を実装。Gurobi などは変数宣言に時間がかかるため、無駄な変数宣言をしないように。
    # TODO: 特に MultiIndex になる場合に sortorder 等の設定で高速化できないか調査
    if fix is not None:
        raise Warning("``fix`` has not been implemented yet. This argument will be ignored.")
    if np.ndim(index) > 2:
        raise ValueError("``index`` dimension cannot be greater than 2.")

    if isinstance(index, pd.Index):
        pass
    elif all(is_list_like(v) for v in index):
        index = pd.MultiIndex.from_product(index)
    elif is_list_like(index):
        index = pd.Index(index)
    else:
        raise ValueError(f"{type(index)} is not supported for ``index``.")
    return from_index(name, index, lb, ub, cat, **kwargs)


def fix(varseries: Series, values: Series):
    raise NotImplementedError()


def set_border(varseries: Series, index):
    raise NotImplementedError()


def approx_piecewise():
    raise NotImplementedError()
