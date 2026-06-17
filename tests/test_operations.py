import pytest
from app.operation import Addition, Subtraction, Multiplication, Division


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (1.5, 2.5, 4.0),
])
def test_addition(a, b, expected):
    assert Addition.execute(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1.5, 0.5, 1.0),
])
def test_subtraction(a, b, expected):
    assert Subtraction.execute(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-2, 5, -10),
])
def test_multiplication(a, b, expected):
    assert Multiplication.execute(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (1, 4, 0.25),
])
def test_division(a, b, expected):
    assert Division.execute(a, b) == expected


def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Division.execute(10, 0)