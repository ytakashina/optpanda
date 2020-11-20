import numpy as np
import pandas as pd
from pandas import Index, Series
from pandas.core.dtypes.common import is_list_like

import optpanda.backend as B


def is_consistent(data, index):
    if data is None or np.isscalar(data):
        return True
    if isinstance(data, Series):
        return index.equals(data.index)
    elif np.ndim(data) == 1:
        return np.ravel(data).size == len(index)
    return False


def from_index(name, index: Index, lb=None, ub=None, cat="Continuous", **kwargs):
    if not isinstance(index, Index):
        raise ValueError("index must be a pandas.Index.")

    if is_consistent(lb, index):
        lb = pd.Series(lb, index=index)
    else:
        raise ValueError(f"``lb`` is not consistent with the given ``index``.")

    if is_consistent(ub, index):
        ub = pd.Series(ub, index=index)
    else:
        raise ValueError(f"``ub`` is not consistent with the given ``index``.")

    values = [B.variable(f"{name}[{i}]", lb[i], ub[i], cat, **kwargs) for i in index]
    return pd.Series(values, index, name=name, dtype=object)


def create(name, index, fix=None, lb=None, ub=None, cat="Continuous", **kwargs):
    # TODO: fix を実装。Gurobi などは変数宣言に時間がかかるため、無駄な変数宣言をしないように。
    # TODO: 特に MultiIndex になる場合に sortorder 等の設定で高速化できないか調査
    if fix is not None:
        raise Warning("``fix`` has not been implemented yet. This argument will be ignored.")
    if np.ndim(index) > 2:
        raise ValueError("``index`` dimension cannot be greater than 2.")

    if isinstance(index, Index):
        pass
    elif all(is_list_like(v) for v in index):
        index = pd.MultiIndex.from_product(index)
    elif is_list_like(index):
        index = pd.Index(index)
    else:
        raise ValueError(f"{type(index)} is not supported for ``index``.")
    return from_index(name, index, lb, ub, cat, **kwargs)


def fix_values(series: Series, values: Series):
    raise NotImplementedError()


def approx_piecewise():
    raise NotImplementedError()
