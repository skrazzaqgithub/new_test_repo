def substraction(x,y):
    return x-y
def test_substraction():
    assert substraction(5,3) == 2
    assert substraction(10,4) == 6
    assert substraction(0,0) == 0
    assert substraction(-1,-1) == 0
    assert substraction(-5,3) == -8
    assert substraction(5,-3) == 8