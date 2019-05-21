import Dependencies.matlib as matlib
import csv

def test_suma():
    archivo = open('./Data/nacimientos.csv', 'r')
    print(archivo)
    suma = matlib.porcentaje(matlib.division(1, 3), 1)
    assert suma == 33.33