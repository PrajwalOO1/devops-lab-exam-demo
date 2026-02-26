import pytest
from app import factorial


def test_factorial_0():
    assert factorial(0) == 1


def test_factorial_5():
    assert factorial(5) == 120


def test_negative():
    with pytest.raises(ValueError):
        factorial(-1)
