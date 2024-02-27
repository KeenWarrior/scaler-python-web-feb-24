import pytest

from basic_maths import division


@pytest.mark.parametrize("first, second, result", [(10, 20, .5), (20, 10, 2), (40, 4, 10)])
def test_division_by_zero(first, second, result):
    assert division(first, second) == result
