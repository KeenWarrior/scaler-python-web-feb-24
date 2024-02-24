import pytest
from pytest import approx
from basic_maths import add, multiply, division


def test_addition():
    result = add(2, 3)
    assert 5 == result


def test_multiply():
    result = multiply(2, 3)
    assert 6 == result


def test_division():
    result = division(5, 11)
    assert approx(0.454, rel=1e-2) == result


def test_division_by_zero():
    with pytest.raises(ValueError):
        result = division(5, 0)
