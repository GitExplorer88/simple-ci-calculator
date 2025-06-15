from calculator import total, difference, multiply, divide
import pytest 

def test_add():
    assert total(3,2)==5
    
def test_subtract():
    assert difference(10,4)==6

def test_multiply():
    assert multiply(8,5)==40
    
def test_divide():
    assert divide(40,5)==8
    
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5,0)