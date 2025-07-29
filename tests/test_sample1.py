def multiplication(x,y):
    return x*y
def test_multiplication():
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 5) == -5
    assert multiplication(0, 10) == 0
    assert multiplication(7, 8) == 56
    assert multiplication(-3, -4) == 12
    assert multiplication(1.5, 2) == 3.0
    assert multiplication(0.1, 10) == 1.0