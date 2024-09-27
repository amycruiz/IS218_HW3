from calculator.operations import add, multiply, subtract, divide

def test_addition():
    '''Test addition '''
    assert add(2,2) == 4

def test_subtraction():
    '''Test subtraction '''
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test multiplication '''
    assert multiply(2,2) == 4

def test_division():
    '''Test division'''
    assert divide(2,2) == 1