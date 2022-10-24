from MacoWins import *
import pytest
def reiniciar_listas():
    global productos
    global ventas
    productos.clear()
    ventas.clear()
def reiniciar_anio():
    global fecha_anio_actual
    fecha_anio_actual=""
    
def reiniciar_dia():
    global dia
    dia=""

def cambiar_dia(dia_nuevo):
    global dia
    dia=dia_nuevo

def producto_new():
    return {"codigo":2,"nombre":"short talle ss","precio":120,"categoria":"short"}
     
def test_validar_elementos_en_producto():
    assert len(productos)>0 or len(productos)==0 and type(productos)==list

def test_validar_elementos_en_ventas():
    assert len(ventas)>0 or len(ventas)==0 and type(productos)==list

def test_actualizar_precios_por_categoria_existente():
    reiniciar_listas()
    
    registrar_producto(producto_new())
    
    porcentaje=50

    actualizar_precios_por_categoria("short",porcentaje)
    assert productos[0]["precio"]==180
def test_actualizar_precios_por_categoria_inexistente():

    reiniciar_listas()

    registrar_producto(producto_new())

    actualizar_precios_por_categoria("remera",50)

    assert productos[0]["precio"]==120
def test_actualizar_precios_por_categoria_existente_con_procentaje_en_string():
    
    reiniciar_listas()
    
    registrar_producto(producto_new())
   
    with pytest.raises(ValueError) as exception_info:
   
        actualizar_precios_por_categoria("remera", "23")
    
    assert str(exception_info.value)=="Porcentaje no recibe cadena de texto, solo numeros"
def test_actualizar_precios_por_categoria_sin_tener_productos():
    
    reiniciar_listas()
    
    assert actualizar_precios_por_categoria("remera",10)== None

def test_actualizar_precios_por_categoria_sin_tener_categoria_en_productos():
    reiniciar_listas()
    registrar_producto({"codigo":1,"precio":120})
    assert "categoria" not in productos

def test_productos_mas_vendido_sin_productos_y_sin_ventas():
   
    reiniciar_listas()
    
    assert  productos_mas_vendidos()==[]

def test_cantidad_de_codigo_con_ventas_igual_a_cero():
    reiniciar_listas()
    assert cantidad_de_codigo_con_ventas([])=={}

def test_cantidad_de_codigo_con_ventas_datos_string():
    reiniciar_listas()
    codigos_ordenados=["a","1","3","4"]
    assert cantidad_de_codigo_con_ventas(codigos_ordenados)=={}

def test_cantidad_de_codigo_con_ventas_datos_existentes():
    reiniciar_listas()
    registrar_producto({
    "codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500})
    recargar_stock(102,400)
    realizar_venta({"codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500,"stock":400},300)
    codigos=lista_de_codigos_productos()
    assert cantidad_de_codigo_con_ventas(codigos)=={102:300}
    
    
def test_cantidad_de_codigo_con_ventas_datos_inexistentes():
    reiniciar_listas()
    registrar_producto({
    "codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500})
    recargar_stock(102,400)
    realizar_venta({"codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500,"stock":400},300)
    codigos_ordenados=[104,105,100]
    assert cantidad_de_codigo_con_ventas(codigos_ordenados)=={}
def test_ventas_del_anio_con_anio_0():
    reiniciar_anio()
    reiniciar_listas()
    registrar_producto({
    "codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500})
    recargar_stock(102,400)
    realizar_venta({"codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500,"stock":400},300)   
    ventas[0]["fecha"]=""
    assert ventas_del_anio()==[]

def test_ventas_del_anio_actual():
    fecha_anio_actual=date.strftime(date.today(), "%Y")
    reiniciar_anio()
    reiniciar_listas()
    registrar_producto({
    "codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500})
    recargar_stock(102,400)
    realizar_venta({"codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500,"stock":400},300)
    anio=date.strftime(date.today(), "%Y-%m-%d")
    assert ventas_del_anio()==[{"cantidad":300,"codigo_producto": 102,"fecha":anio,"precio":4500}]
def test_valor_ventas_del_dia_normal():
    reiniciar_listas()
    registrar_producto({
    "codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500})
    recargar_stock(102,400)
    realizar_venta({"codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500,"stock":400},300)
    assert valor_ventas_del_dia()==4500

def test_valor_ventas_del_dia_inexistente():
   
    reiniciar_listas()
    registrar_producto({
    "codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500})
    recargar_stock(102,400)
    realizar_venta({"codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500,"stock":400},300)
    ventas[0]["fecha"]="2022-10-90"
    assert valor_ventas_del_dia()==0

def test_discontinuar_productos_sin_productos():
    reiniciar_listas()
    registrar_producto({
    "codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500})
    registrar_producto({
    "codigo": 103,
    "nombre": "short talle x",
    "categoria": "short",
    "precio": 45030})
    recargar_stock(102,400)
    discontinuar_productos()

    assert productos==[{
    "codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500,"stock":400}]

# -------------------------------------------------------------

def test_lista_de_codigos_productos_sin_productos():
    reiniciar_listas()
    assert lista_de_codigos_productos() == []

def test_lista_de_codigos_productos_sin_codigo():
    reiniciar_listas()
    registrar_producto({
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500})
    assert lista_de_codigos_productos() == []

def test_lista_de_codigos_ventas_sin_venta():
    reiniciar_listas()
    registrar_producto({
    "codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500})
    recargar_stock(102,400)
    assert lista_de_codigos_ventas() == []

# def test_lista_de_codigos_ventas_sin_codigo():
#     reiniciar_listas()
#     registrar_producto({
#     "codigo": 102,
#     "nombre": "short talle xxx",
#     "categoria": "short",
#     "precio": 4500})
#     recargar_stock(102,400)
#     realizar_venta({"nombre": "short talle xxx",
#     "categoria": "short",
#     "precio": 4500,"stock":400},300)
#     with pytest.raises(ValueError):
#         assert lista_de_codigos_ventas()
    
    

def test_codigo_de_producto_solicitado_en_productos_sin_productos():
    reiniciar_listas()
    assert codigo_de_producto_solicitado_en_productos(100) == False

def test_codigo_de_producto_solicitado_en_productos_sin_parametro():
    reiniciar_listas()
    with pytest.raises(TypeError) as exception_info:
        codigo_de_producto_solicitado_en_productos()
    assert str(exception_info.value)=="codigo_de_producto_solicitado_en_productos() missing 1 required positional argument: 'codigo'"
def test_posicion_de_codigo_ordenado_decre_de_productos_existente():
    reiniciar_listas()
    nuevo={"codigo":1,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000,"stock":123}
    
    registrar_producto(nuevo)
    
    posicion=posicion_de_codigo_ordenado_decre_de_productos(1)
    assert posicion==0

def test_registrar_producto_vacio():

    reiniciar_listas()

    with pytest.raises(TypeError) as exception_info:
    
        registrar_producto()

    assert str(exception_info.value)=="registrar_producto() missing 1 required positional argument: 'producto_nuevo'"

def test_registrar_producto_sin_codigo():
    reiniciar_listas()
    nuevo={
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000,"stock":123}
    with pytest.raises(ValueError) as exception_info:
        registrar_producto(nuevo)

    assert str(exception_info.value)== 'no se encotro codigo, no incializar stock '
def test_registrar_producto_ya_registrado():
    reiniciar_listas()
    nuevo={"codigo":1,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000,"stock":123}
    nuevo_2={"codigo":1,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000,"stock":123}
    registrar_producto(nuevo)
    with pytest.raises(ValueError) as exception_info:
        registrar_producto(nuevo_2)
    assert str(exception_info.value)=="producto registrado"

def test_recargar_stock_en_producto_no_disponible():
    reiniciar_listas()
    producto={"codigo":1,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000,"stock":123}
    registrar_producto(producto)
    with pytest.raises(ValueError) as exception_info:
        recargar_stock(2,10)
        assert str(exception_info.value)=="No se encuentra el producto"

def test_recargar_stock_producto_disponible():
    reiniciar_listas()
    producto={"codigo":100,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000}
    registrar_producto(producto)
    recargar_stock(100,2) 
    assert producto["stock"] == 2

def test_hay_stock_producto_con_stock_devulve_True():
    reiniciar_listas()
    producto={"codigo":100,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000,"stock":0}
    registrar_producto(producto)
    recargar_stock(100,3)
    assert hay_stock(100) == True

def test_hay_stock_en_cero_devuelve_False():
    reiniciar_listas()
    producto={"codigo":100,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000,"stock":0}
    registrar_producto(producto)
    assert hay_stock(100) == False

def test_calcular_precio_final_si_precio_es_mayor_70_y_extranjero():
    reiniciar_listas()
    producto={"codigo":100,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000,"stock":10}
    registrar_producto(producto)
    assert calcular_precio_final(producto, True) == 5000

def test_calcular_precio_final_si_precio_es_mayor_70_y_not_extranjero():
    reiniciar_listas()
    producto={"codigo":100,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000,"stock":10}
    registrar_producto(producto)
    assert calcular_precio_final(producto, False) == 6050

def test_contar_categorias_de_2_categoria_en_la_lista():
    reiniciar_listas()
    producto={"codigo":100,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000}
    producto_nuevo={"codigo":101,
    "nombre": "short talle xxxx",
    "categoria": "short",
    "precio": 5000}
    registrar_producto(producto)
    registrar_producto(producto_nuevo)
    assert contar_categorias(productos) == 2

def test_contar_categorias_de_0_categoria_en_la_lista():
    reiniciar_listas()
    producto={"codigo":100,
    "nombre": "short talle xxxx",
    "precio": 5000}
    producto_nuevo={"codigo":101,
    "nombre": "short talle xxxx",
    "precio": 5000}
    registrar_producto(producto)
    registrar_producto(producto_nuevo)
    assert contar_categorias(productos)==0
    # with pytest.raises(ValueError) as exception_info:
    #     assert str(exception_info.value)== 'categoria'

def test_realizar_venta_de_un_producto():
    reiniciar_listas()
    producto={"codigo":100,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000}  
    registrar_producto(producto)
    recargar_stock(100,10)
    realizar_venta(producto,1)
    assert  producto["codigo"] == ventas[0]["codigo_producto"]
def test_realizar_venta_de_un_producto_con_codigo_inexistente():
    reiniciar_listas()
    producto={"codigo":-1,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000,
    "stock": 1}  
    registrar_producto(producto)
    with pytest.raises(ValueError) as exception_info:
            realizar_venta(producto,1)
    assert str(exception_info.value)=="Codigo no encontrado"


def test_realizar_compra_de_un_producto():
    reiniciar_listas()
    producto={"codigo":100,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000}
    registrar_producto(producto)
    recargar_stock(100,10)
    realizar_compra(100,1)
    assert producto["stock"] == 9

def test_realizar_compra_de_un_producto_sin_stock():
    reiniciar_listas()
    producto={"codigo":100,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000}
    registrar_producto(producto)
    posicion=posicion_de_codigo_ordenado_decre_de_productos(100)
    with pytest.raises(ValueError) as exception_info:
        realizar_compra(100,12)
   
    assert str(exception_info.value)=="No hay stock Disponible, cantidad dispoble de " + str(productos[posicion]["stock"])
    








