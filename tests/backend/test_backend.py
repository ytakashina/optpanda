import optpanda.backend as B
from optpanda import set_backend


def test_get_backend():
    assert B.backend() == 'pulp'


def test_set_backend():
    set_backend('ortools')
    assert B.backend() == 'ortools'
