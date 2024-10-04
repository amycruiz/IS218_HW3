"Testing Calculation class"

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_operations(a, b, operation, expected):
    "Testing calculation operations"
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f'''Failed {operation.__name__} operation
    with {a} and {b}'''

def test_calculation_repr():
    "Testing __repr__ method"
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr, '''The __repr__ method output
    does not match the expected string.'''

def test_divide_by_zero():
    "Testing divison by zero"
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
