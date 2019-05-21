import Dependencies.matlib as matlib

def test_suma():
    suma = matlib.suma(2, 3)
    assert suma == 4

def test_div():
    division = matlib.division(2, 0)
    assert division == 1