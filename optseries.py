import pandas as pd
from pandas import Series
from pandas.core.dtypes.common import is_list_like
from pulp import LpVariable

try:
    import gurobipy
except ModuleNotFoundError:
    print("gurobipy is not found.")
    pass

_backend = 'pulp'
_dtype = LpVariable
_model = None


def set_backend(backend='pulp', model=None):
    mod = __import__(__name__)
    mod._backend = backend
    mod._model = model
    if backend == 'pulp':
        mod._dtype = LpVariable
    else:
        raise ValueError("Only 'pulp' backend is supported.")


# このクラス自体をインスタンス化しないのであれば関数で良い
def create_optvar(name, lb=None, ub=None, cat="Continuous", **kwargs):
    if _backend == 'pulp':
        e = kwargs.get("e", None)
        return LpVariable(name, lowBound=lb, upBound=ub, cat=cat, e=e)
    else:
        raise ValueError("Only 'pulp' backend is supported.")


# このクラス自体をインスタンス化しないのであれば関数で良い。やるなら pandas.Series 拡張したい。
# OptSeries に対して最適化関係のメソッドを実装することを考えると、やはりこの方向性がよさそう。
# - 境界値の設定
# - 区分線形近似
# - etc.
class OptSeries:
    __data: Series

    def __init__(self, data: Series = None):
        self.__data = data

    @classmethod
    def create(cls, name, index=None, fix=None, lb=None, ub=None, cat="Continuous", **kwargs):
        # TODO: lb, ub が index と同じ shape の場合
        # TODO: fix を実装。Gurobi などは変数宣言に時間がかかるため、無駄な変数宣言をしないように。
        # TODO: 特に MultiIndex になる場合に sortorder 等の設定で高速化できないか調査

        if index is None:
            return create_optvar(name, lb, ub, cat, **kwargs)

        if isinstance(index, pd.Index):
            values = [create_optvar(f"{name}[{i}]", lb, ub, cat, **kwargs) for i in index]
            data = pd.Series(values, index, name=name, dtype=_dtype)
        elif all(is_list_like(v) for v in index):
            index = pd.MultiIndex.from_product(index)
            data = OptSeries.create(name, index=index, lb=lb, ub=ub, cat="cat", **kwargs)
        elif is_list_like(index):
            values = [create_optvar(f"{name}[{i}]", lb, ub, cat, **kwargs) for i in index]
            data = pd.Series(values, index=index, name=name, dtype=_dtype)
        else:
            raise ValueError(f"{type(index)} is not supported for ``index``.")

        return OptSeries(data)

    def fix(self, data: Series = None):
        """Set mask"""
        raise NotImplementedError()
