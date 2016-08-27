from ..myfunc import add, sub

def test_add():
    assert add(1,3) == 4

def test_sub():
    assert sub(5,2) == 3
    print "this is v2"
    assert sub(1,2) == -1
