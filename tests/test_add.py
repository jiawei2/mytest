from ..myfunc import add, sub

def test_add():
    assert add(1,3) == 4

def test_sub():
    assert sub(5,2) == 3
    assert sub(6,5) == 1
