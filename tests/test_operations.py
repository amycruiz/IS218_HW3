"Testing operations"

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    """Test the addition operation."""
    calculation = Calculation(Decimal('10'), Decimal('5'), add)
    assert calculation.perform() == Decimal('15'), "Add operation failed"

def test_operation_subtract():
    """Test the subtraction operation."""
    calculation = Calculation(Decimal('10'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('5'), "Subtract operation failed"

def test_operation_multiply():
    """Test the multiplication operation."""
    calculation = Calculation(Decimal('10'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('50'), "Multiply operation failed"

def test_operation_divide():
    """Test the division operation."""
    calculation = Calculation(Decimal('10'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('2'), "Divide operation failed"

def test_divide_by_zero():
    """Test division by zero, which should raise a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
