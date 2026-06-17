import pytest
from app.calculation import Calculation, CalculationFactory


@pytest.mark.parametrize("operation, a, b, expected", [
    ("add", 2, 3, 5),
    ("subtract", 5, 2, 3),
    ("multiply", 4, 3, 12),
    ("divide", 10, 2, 5.0),
])
def test_factory_creates_and_performs(operation, a, b, expected):
    calc = CalculationFactory.create(operation, a, b)
    assert calc.perform() == expected


def test_factory_unknown_operation():
    with pytest.raises(ValueError, match="Unknown operation"):
        CalculationFactory.create("power", 2, 3)


def test_calculation_str():
    assert str(Calculation("add", 2, 3)) == "2 + 3 = 5"