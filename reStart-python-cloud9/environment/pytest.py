import pytest

def myfunction(a):
    return a+10
def test_method():
    assert myfunction(10)==18