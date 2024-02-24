import pytest
from slow import slow_run
from basic_maths import division


@pytest.mark.skip(reason="Too slow")
def test_slow_run():
    result = slow_run()
    assert 5 == result


@pytest.mark.xfail(reason="This is under dev")
def test_zero_div():
    division(10, 0)


