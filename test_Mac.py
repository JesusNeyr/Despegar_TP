from MacoWins import *
import pytest

def test_posicion_de_codigo_ordenado_decre_de_productos():
    reiniciar_productos()
    for i in range(0,3):
        registrar_producto({"codigo": i})
    assert posicion_de_codigo_ordenado_decre_de_productos(2)==0
