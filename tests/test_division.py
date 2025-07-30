def division(a, b):
    """Returns the result of dividing a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def test_division():
    """Tests the division function."""
    assert division(10, 2) == 5
    assert division(9, 3) == 3
    assert division(7, 1) == 7
    assert division(-10, 2) == -5
    assert division(0, 1) == 0
    try:
        division(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    else:
        assert False, "Expected ValueError not raised"