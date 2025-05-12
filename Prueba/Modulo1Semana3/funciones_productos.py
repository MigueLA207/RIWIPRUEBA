#Definimos colores para mejor visibilidad
DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m" 

#Todas las funciones reciben el inventario como parametro

#Funcion para agregar producto. Recibe como parametro el nombre, precio y cantidad del producto
def agregar_producto(nombre,precio,cantidad,inventario):
    #Guarda el precio y la cantidad en otro diccionario para asignarlo despues al nombre
    detalles_producto = {'Precio':float(precio) , 'Cantidad' : cantidad}
    inventario[nombre] = detalles_producto
    print(SUCCESS + "Producto ingresado con exito" + RESET)

#Funcion para mostrar el inventario
def mostrar_inventario(inventario):
    print(SUCCESS + "\n--------------Lista de productos---------------" + RESET)
    for nombre, detalle in inventario.items():
        print(f"Nombre: {nombre} -- Precio: {detalle['Precio']} -- Cantidad: {detalle['Cantidad']}")
    print(SUCCESS + "------------------------------------------------\n" + RESET)

#Funcion para buscar producto en el inventario. Recibe como parametro el nombre del producto
def buscar_producto(nombre_buscar,inventario):
    if nombre_buscar in inventario:
        print(SUCCESS + f"\nBusqueda realizada con exito" + RESET)
        print("---------------------------------------------------")
        print(f"Nombre: {nombre_buscar} -- Precio: {inventario[nombre_buscar]['Precio']} -- Cantidad: {inventario[nombre_buscar]['Cantidad']} ")
        print("---------------------------------------------------")
    else:
        print(WARNING + "El producto no se encuentra en el inventario" + RESET)
    
#Funcion para editar el precio de un producto. Recibe como parametro el nombre del producto
def editar_precio(nombre_editar,inventario):
    if nombre_editar in inventario:
        #Mostramos el producto que va a editar
        print("\n---------------------------------------------------")
        print(f"Nombre: {nombre_editar} -- Precio: {inventario[nombre_editar]['Precio']} ")
        print("---------------------------------------------------")
        while True:
            precio_editar = input("Digita el nuevo precio para este producto: ")
            #verifica la entrada
            if precio_editar.isdigit() and float(precio_editar) > 0:
                precio_editar = float(precio_editar)
                break
            else:
                print(WARNING + "Opcion Invalida. Intente de nuevo" + RESET)
        #actualiza el precio del producto
        inventario[nombre_editar]['Precio'] = precio_editar
        print(SUCCESS + "Precio editado con exito" + RESET)
    else:
        print(WARNING + "El producto no se encuentra en el inventario" + RESET)

#Funcion para eliminar un producto. Recibe como parametro el nombre del producto
def eliminar_producto(producto_eliminar,inventario):
    if producto_eliminar in inventario:
        del inventario[producto_eliminar]
        print(SUCCESS + "Producto eliminado con exito" + RESET)
    else: 
        print(WARNING + "Este producto no se encuentra en el inventario" + RESET)

#Funcion para calcular el valor total del inventario. Recibe como parametro el nombre del producto

def valor_total_inventario(inventario):
    valor_inventario = sum(map(lambda producto: producto[1]['Precio'] * producto[1]['Cantidad'] , inventario.items()))
    print(f"El valor total del inventario es de: {valor_inventario}")

#Validacion para repeticion de cada opcion del menu
def validacion():
    while True:
        salir = input("\n¿Quieres hacerlo otra vez? 1 (si) o 2 (no): ")
        if salir.isdigit() == False:
            print(WARNING + "Opcion invalida. Intenta de nuevo" + RESET)
        elif int(salir) != 1 and int(salir) != 2:
            print(WARNING + "Opcion invalida. Intenta de nuevo" + RESET)
        else:
            break
        
    return salir
        