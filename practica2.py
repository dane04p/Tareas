#lista de productos
productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Auriculares"]

#tupla de categorias
categorias = ("Computadoras", "Accesorios", "Audio")

#diccionario de precios
precios = {
    "Laptop": 500000,
    "Mouse": 20000,
    "Teclado": 35000,
    "Monitor": 150000,
    "Auriculares": 14000
}

#calculo de precio total y precio promedio
precioTotal = sum(precios.values())
precioPromedio = precioTotal / len(precios)

#clasificacion de cada producto
for producto, precio in precios.items():
    if precio > 250000:
        salida = "Producto Premium"
    elif 50000 <= precio <= 250000:
        salida = "Producto Estándar"
    else:
        salida = "Producto Económico"
    
#imprimir la clasificacion de cada producto
print(f"{producto}: {salida}, Precio: {precio}")

#conjunto set con las marcas de los productos
marcasProductos = {"HP", "T-Wolf", "T-Wolf", "Dell", "Samsung"}

print(f""" Los productos disponibles en el inventario son: {productos}\n
           Las categorías en el inventario son: {categorias}\n
           Los precios de cada producto disponible son: {precios}\n
           Precio total: {precioTotal}\n
           Precio promedio: {precioPromedio}\n
           Las marcas de los productos son: {marcasProductos}\n
           El número de marcas únicas en el inventario es de: {len(marcasProductos)}
""")
