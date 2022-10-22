from ast import Num, Str
from datetime import date

from operator import itemgetter
from tokenize import Number

fecha_anio_actual=date.strftime(date.today(), "%Y")
dia =date.strftime(date.today(), "%Y-%m-%d")

productos = [
  {
    "codigo": 100,
    "nombre": "short talle x",
    "categoria": "remera",
    "precio": 4500,
    "stock": 0
  },
   {
    "codigo": 101,
    "nombre": "short talle xx",
    "categoria": "short",
    "precio": 4500,
    "stock": 2
  },
   {
    "codigo": 102,
    "nombre": "short talle xxx",
    "categoria": "short",
    "precio": 4500,
    "stock": 2
  },
   {
    "codigo": 103,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000,
    "stock": 2
  }
]

ventas = [
    {
    "codigo_producto": 103,
    "cantidad": 20,
    "fecha": "2022-09-24",
    "precio": 4500
      },
    {
    "codigo_producto": 101,
    "cantidad": 3,
    "fecha": "2022-09-24",
    "precio": 4500
      },
     {
    "codigo_producto": 102,
    "cantidad": 300,
    "fecha": "2022-09-24",
    "precio": 4500
      },
    {
    "codigo_producto": 101,
    "cantidad": 30,
    "fecha": "2022-09-24",
    "precio": 4500
      },
    {
    "codigo_producto": 101,
    "cantidad": 40,
    "fecha": "2023-09-24",
    "precio": 4500
      }
  ]

producto_nuevo={
    "codigo": 10000,
    "nombre": "short talle xxxx",
    "categoria": "remera",
    "precio": 5000,
  }


def lista_de_codigos_productos():
    codigos=[]
    
    if len(productos)>0:
        
        [codigos.append(producto["codigo"]) for producto in productos if  "codigo" in producto]
    else:
        codigos=[]    
        
    return sorted(codigos,reverse=True)

def lista_de_codigos_ventas():
    global ventas
    codigos=[]
    
    if len(ventas)>0:
        
        [codigos.append(venta["codigo_producto"]) for venta in ventas]
    else:
        codigos=[]
    
    return codigos

def codigo_de_producto_solicitado_en_productos(codigo):
 
    global productos
    
    return codigo in lista_de_codigos_productos()

def posicion_de_elemento_en_productos(codigo_de_producto):
    
    global productos
    
    return lista_de_codigos_productos().index(codigo_de_producto)
    
def registrar_producto(producto_nuevo):
    

    lista_codigos_de_productos=lista_de_codigos_productos()
    for producto in productos:
                
            if producto_nuevo["codigo"]==producto["codigo"]:
                    
                raise ValueError("Existe otro producto con igual codigo, estos deben ser unicos")

            
    producto_nuevo["stock"] = 0
    productos.append(producto_nuevo)
        
def recargar_stock(codigo_producto, cantidad):
    
    global productos

    for producto in productos:
        
        if codigo_de_producto_solicitado_en_productos(codigo_producto):
            
            if producto["codigo"] == codigo_producto:
                
                producto["stock"] += cantidad
                
        else:
            
            raise ValueError("No se encuentra el producto")

def hay_stock(codigo_producto):
    
    global productos
    
    lista_de_codigos=lista_de_codigos_productos()
    
    posicion=posicion_de_elemento_en_productos(codigo_producto)
    

    if codigo_producto in lista_de_codigos:

        return productos[posicion]["codigo"]== codigo_producto and productos[posicion]["stock"] > 0

def calcular_precio_final(un_producto, es_extranjero):
    
    if un_producto["precio"] > 70 and es_extranjero:
        
        return un_producto["precio"]
    
    else:
        
        return un_producto["precio"] + un_producto["precio"] * 0.21

def contar_categorias(productos):
    
    categorias_unicas=[]
    
    [categorias_unicas.append(producto["categoria"]) for producto in productos if producto["categoria"] not in categorias_unicas]
    
    return len(categorias_unicas)

def realizar_venta(producto_vendido,cantidad):
    
    ventas.append( {
        
                "codigo_producto": producto_vendido["codigo"],
                "cantidad": cantidad,       
                "fecha": date.strftime(date.today(), "%Y-%m-%d"),
                "precio": producto_vendido["precio"]
                
                })
    
def realizar_compra(codigo_producto, cantidad):
    
    global productos
    
    global ventas
    
    lista_de_codigos = lista_de_codigos_productos()
    
    posicion=posicion_de_elemento_en_productos(codigo_producto)
    
    if hay_stock(codigo_producto) and cantidad <= productos[posicion]["stock"]:
        
            productos[posicion]["stock"]-= cantidad
            
            realizar_venta(productos[posicion],cantidad)
            
    else:
            raise ValueError("No hay stock Disponible, cantidad dispoble de " + str(productos[posicion]["stock"]) )
        
def discontinuar_productos():
    
    global productos
    
    for producto in productos :
        
        if producto["stock"] == 0:
            
            del productos[productos.index(producto)]

def valor_ventas_del_dia():
    
    global ventas
    
    global dia 
    suma_ventas = 0
    
    for venta in ventas:
        
        if venta["fecha"] == dia:
            
            suma_ventas += venta["precio"]
            
    return suma_ventas

def ventas_del_anio():
    global ventas
    lista_de_ventas_del_anio = []
    
    for venta in ventas:
        
        if venta["fecha"][0:4] == fecha_anio_actual:
            
            lista_de_ventas_del_anio.append(venta)
            
    return lista_de_ventas_del_anio

def cantidad_de_codigo_con_ventas(codigos_ordenados_de_productos_decre):
    
    cantidad_repetida_de_codigo_vendidos={}
    
    for codigo in codigos_ordenados_de_productos_decre:
        
        for venta in ventas:
            
            if codigo == venta["codigo_producto"]:
                
                if codigo in cantidad_repetida_de_codigo_vendidos:
                    
                     cantidad_repetida_de_codigo_vendidos[codigo] += venta["cantidad"]
                     
                else:
                    
                    cantidad_repetida_de_codigo_vendidos[codigo] = venta["cantidad"]
                    
    return cantidad_repetida_de_codigo_vendidos

def productos_mas_vendidos_ordenados(codigos_ordenados_por_ventas):
    
    global productos
    
    nombre_productos = []
    
    for codigo in codigos_ordenados_por_ventas:
        
        for producto in productos:
            
            if codigo[0] == producto["codigo"]:
                
                nombre_productos.append(producto["nombre"])
                
    return nombre_productos

def productos_mas_vendidos(hasta=-1):
    
    global productos
    
    global ventas
    
    if len(ventas) <= hasta:
        
        raise ValueError("cantidad solicitada excedida")
    
    codigos_ordenados_de_productos_decre=lista_de_codigos_productos()
    
    cantidad_repetida_de_codigo_vendidos= cantidad_de_codigo_con_ventas(codigos_ordenados_de_productos_decre)
    
    codigos_ordenados_por_ventas=sorted(cantidad_repetida_de_codigo_vendidos.items(), key=itemgetter(1),reverse=True)
    
    nombre_productos=productos_mas_vendidos_ordenados(codigos_ordenados_por_ventas)
    
    if hasta!=-1:
        return nombre_productos[:hasta]
    else:
        return nombre_productos
    
def actualizar_precios_por_categoria(categoria, porcentaje):

    global productos
    
    if type(porcentaje)==int:
        for producto in productos:
            
            if producto["categoria"] == categoria.lower():
                
                producto["precio"] += producto["precio"]* porcentaje/100
    else:

        raise ValueError("Porcentaje no recibe cadena de texto, solo numeros")


def cargar_producto(un_producto):
    global producto_nuevo
    producto_nuevo=un_producto
def reiniciar_productos():
    global productos
    productos = []
    return productos 

def reiniciar_ventas():
    global ventas
    ventas=[]
    return ventas
def reiniciar_fecha():
    global fecha_anio_actual
    fecha_anio_actual=0
    return fecha_anio_actual
def cambiar_fecha(fecha_nueva):
    global fecha_anio_actual
    fecha_anio_actual=fecha_nueva
    return fecha_anio_actual
def reiniciar_dia():
    global dia
    dia=0
    return dia
def cambiar_dia(un_dia):
    global dia
    dia=un_dia
    return dia
def agregar_producto_a_productos(producto):
    global productos
    productos.append(producto)

#Sprint3

class Estado:
    def __init__(self, productos):    
        self.productos=productos

    def nueva(self,codigo):
        global productos
        for count in range(0, len(self.productos)):
            if self.productos[count]["codigo"]==codigo:
                self.productos[count]["precio"]=self.productos[count]["precio"]
    def promocion(self,codigo,descuento_fijo):
        global productos
        for count in range(0, len(self.productos)):
            if self.productos[count]["codigo"]==codigo:
                self.productos[count]["precio"]-=descuento_fijo
    def liquidacion(self,codigo):
        global productos
        for count in range(0, len(self.productos)):
            if self.productos[count]["codigo"]==codigo:
                self.productos[count]["precio"]-=((self.productos[count]["precio"])*100/50)