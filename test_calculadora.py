import pytest
from calculadora.calculadora import (
    somar, subtrair, multiplicar, dividir, potencia, porcentagem
)

def test_somar():
    assert somar(10, 5) == 15

def test_subtrair():
    assert subtrair(10, 5) == 5

def test_multiplicar():
    assert multiplicar(10, 5) == 50

def test_dividir():
    assert dividir(10, 5) == 2

def test_divisao_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_potencia():
    assert potencia(2, 3) == 8

def test_porcentagem():
    assert porcentagem(200, 10) == 20
