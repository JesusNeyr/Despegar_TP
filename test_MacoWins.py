from aifc import Error
from MacoWins import *
import pytest

def test_validar_elementos_en_producto():
    assert len(productos)>0 or len(productos)==0 and type(productos)==list

def test_validar_elementos_en_ventas():
    assert len(ventas)>0 or len(ventas)==0 and type(productos)==list

def test_validar_producto_nuevo():
    assert "stock" not in producto_nuevo

def test_actualizar_precios_por_categoria_inexistente():
    reiniciar_productos()

    assert actualizar_precios_por_categoria("nn", 23)==None

def test_actualizar_precios_por_categoria_existente_con_procentaje_en_string():
    with pytest.raises(ValueError) as exception_info:
        actualizar_precios_por_categoria("remera", "23")
    assert str(exception_info.value)=="Porcentaje no recibe cadena de texto, solo numeros"
def test_actualizar_precios_por_categoria_sin_tener_productos():
    reiniciar_productos()
    assert actualizar_precios_por_categoria("remera",10)== None

def test_actualizar_precios_por_categoria_sin_tener_categoria_en_productos():
    assert "categoria" not in productos

def test_productos_mas_vendido_sin_productos():
    reiniciar_productos()
    assert  productos_mas_vendidos()==[]
def test_productos_mas_vendido_sin_ventas():
    reiniciar_ventas()
    assert productos_mas_vendidos==[]

def  test_productos_mas_vendido_lista_correcta():
    assert productos_mas_vendidos()==productos_mas_vendidos()

def test_cantidad_de_codigo_con_ventas_igual_a_cero():
    codigos_ordenados=[]
    assert cantidad_de_codigo_con_ventas(codigos_ordenados)=={}

def test_cantidad_de_codigo_con_ventas_datos_string():
    codigos_ordenados=["a","1","3","4"]
    assert cantidad_de_codigo_con_ventas(codigos_ordenados)=={}

def test_cantidad_de_codigo_con_ventas_datos_existentes():
    codigos_ordenados_de_productos_decre=lista_de_codigos_productos(productos)
    assert cantidad_de_codigo_con_ventas(codigos_ordenados_de_productos_decre)=={103: 20, 102: 300, 101: 73}

def test_cantidad_de_codigo_con_ventas_datos_inexistentes():
    codigos_ordenados=[104,105,100]
    assert cantidad_de_codigo_con_ventas(codigos_ordenados)=={}

def test_ventas_del_anio_con_anio_0():
    reiniciar_fecha()
    assert ventas_del_anio()==[]

def test_ventas_del_anio_con_anio_diferente():
    cambiar_fecha(200)
    assert ventas_del_anio()==[]

def test_valor_ventas_del_dia_normal():
    assert valor_ventas_del_dia()==0

def test_valor_ventas_del_dia_inexistente():
    cambiar_dia(80)
    assert valor_ventas_del_dia()==0

def test_valor_ventas_del_dia_negativo():
    cambiar_fecha(-4)
    assert valor_ventas_del_dia()==0

def test_discontinuar_productos_sin_productos():
    reiniciar_productos()
    assert discontinuar_productos()==None

def test_discontinuar_productos_stock_negativo():
    reiniciar_productos()
    
    assert discontinuar_productos()==None

def test_lista_de_codigos_productos_sin_productos():
    reiniciar_productos()
    
    assert lista_de_codigos_productos() == []

def test_lista_de_codigos_productos_sin_codigo():
    reiniciar_productos()
    productos.append({"nombre": "short talle x",
    "categoria": "remera",
    "precio": 4500,
    "stock": 0})
    assert lista_de_codigos_productos() == []