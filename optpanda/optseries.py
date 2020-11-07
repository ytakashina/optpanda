import pandas as pd
from pandas import Series
from pandas.core.dtypes.common import is_list_like

from optpanda.backend import variable, dtype


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
            return variable(name, lb, ub, cat, **kwargs)
        if isinstance(index, pd.Index):
            values = [variable(f"{name}[{i}]", lb, ub, cat, **kwargs) for i in index]
            return OptSeries(pd.Series(values, index, name=name, dtype=dtype()))

        if all(is_list_like(v) for v in index):
            index = pd.MultiIndex.from_product(index)
            return OptSeries.create(name, index=index, lb=lb, ub=ub, cat="cat", **kwargs)
        elif is_list_like(index):
            index = pd.Index(index)
            return OptSeries.create(name, index=index, lb=lb, ub=ub, cat="cat", **kwargs)
        else:
            raise ValueError(f"{type(index)} is not supported for ``index``.")

    def fix(self, data: Series = None):
        """Set mask"""
        raise NotImplementedError()
