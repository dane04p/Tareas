import sys

menu = ("pizza", "hamburguesa", "ensalada", "refresco", "papas", "postre")
categorias = ("Comida", "Bebida", "Postre")

preciosMenu = {
    "pizza": 10000,
    "hamburguesa": 5500,
    "ensalada": 3500,
    "refresco": 1500,
    "papas": 2500,
    "postre": 4000
}

listaCategorias = {
    "pizza": "Comida",
    "hamburguesa": "Comida",
    "ensalada": "Comida",
    "refresco": "Bebida",
    "papas": "Comida",
    "postre": "Postre"
}

listaPedido = []
totalPedidos = {}
totalCategorias = {}

nombre = input("digite su nombre: ")

while True:
    print(preciosMenu)
    pedido = input("que desea ordenar?. Si desea salir, escriba 'salir', o 'terminar pedido' para ordenar: ").lower()

    if pedido == "salir":
        sys.exit()

    if pedido == "terminar pedido":
        totalPagar = 0.0
        descuento = 0.0
        for i in listaPedido:
            totalPagar += preciosMenu[i]
    
            if i in totalPedidos:
                totalPedidos[i] += 1
            else:
                totalPedidos[i] = 1

            categoria = listaCategorias[i]
            if categoria in totalCategorias:
                totalCategorias[categoria] += 1
            else:
                totalCategorias[categoria] = 1
            
        if totalPagar > 25000:
                descuento = totalPagar * 0.90
        elif totalPagar > 15000:
                descuento = totalPagar * 0.95
        elif totalPagar < 15000:
                descuento = totalPagar
    
        print(f"""Pedido de {nombre}
Lista de pedidos: {listaPedido}
Total por producto: {totalPedidos}
Total por categoría: {totalCategorias}
Total a pagar sin descuento: {totalPagar}
TOTAL A PAGAR: {descuento}
""")
        break
        
    if pedido in preciosMenu:
        listaPedido.append(pedido)
        print(f"""Pedido de: {nombre} 
Orden de: {pedido}""")
    else:
        print("Producto no disponible")



