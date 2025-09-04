from src.math_operation import add,subtract


def test_add():
    assert add(1,1)==2
    assert add(2,2)==4
    assert add(3,3)==6


def test_subtract():
    assert subtract(1,1)==0
    assert subtract(2,1)==1
    assert subtract(3,4)==-1    