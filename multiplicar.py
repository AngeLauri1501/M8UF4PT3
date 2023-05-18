def multiply(a, b):
    return a * b

def test_multiply():
    result = multiply(2, 3)
    assert result == 6

def test_multiply_negative_numbers():
    result = multiply(-4, 5)
    assert result == -20

def test_multiply_zero():
    result = multiply(7, 0)
    assert result == 0