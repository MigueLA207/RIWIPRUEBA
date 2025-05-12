from funciones_productos import *

inventario = {
    #Estructura de cada producto en el diccionario
    #'Uva' : {'Precio': 4000 , 'Cantidad' : 12}
}

print("╔═════════════════════════════════════════════════════════════╗") 
print("║                     INVENTARIO DE PRODUCTOS                 ║") 
print("╚═════════════════════════════════════════════════════════════╝\n")

#Mostramos opciones disponibles
while True:
    print("Opciones disponibles: ")
    print("\n(1).Añadir productos \n(2).Consultar productos \n(3).Actualizar precio \n(4).Eliminar producto \n(5).Valor total del inventario \n(6).Mostrar inventario\n(7).Salir del programa\n") 

    #Verificion de entrada valida
    while True:
        opcion_menu = input("Ingresa una opcion del menu por favor: ")
        if opcion_menu.isdigit() and 1 <= int(opcion_menu) <= 7:
            break
        else: 
            print("Opcion invalida. Intenta de nuevo")
            
    #Segun la eleccion se ejecutara cierto bloque de codigo
    match opcion_menu:
        case "1":
            while True: 
                salir = True
                print("\n---------------Agregar Producto---------------\n")
                #Verificacion de nombre 
                while True:
                    nombre_producto = input("Ingrese por favor el nombre del producto: ")
                    if nombre_producto.replace(" ", "").isalpha():
                        break
                    else:
                        print(WARNING +"Opcion Invalida. Intente de nuevo" + RESET)

                #Verificacion de precio 
                while True:    
                    precio_producto = input("Ingrese por favor el precio del producto: ")
                    if precio_producto.isdigit() and float(precio_producto) > 0:
                        precio_producto = float(precio_producto)
                        break
                    else:
                        print(WARNING +"Opcion Invalida. Intente de nuevo" + RESET)

                #Verificacion de cantidad 
                while True:
                    cantidad_producto = input("Ingrese por favor la cantidad de productos que hay: ")
                    if cantidad_producto.isdigit() and int(cantidad_producto) > 0:
                        cantidad_producto = int(cantidad_producto)
                        break
                    else:
                        print(WARNING +"Opcion Invalida. Intente de nuevo" + RESET)

                #Llama la funcion para agregar los prodcutos     
                agregar_producto(nombre_producto,precio_producto,cantidad_producto,inventario)
            
                #valicion par mas intentos del proceso anterior
                
                if validacion() == "2":
                    break
            #Muestra el inventario al agregar un producto 
            mostrar_inventario(inventario)
            
        case "2":
            print("\n-----------------Buscar Producto----------------\n")
            while True: 

                #Verificacion de nombre 
                while True:
                    nombre_buscar = input("Ingrese por favor el nombre del producto: ")
                    if nombre_buscar.replace(" ", "").isalpha():
                        break
                    else:
                        print(WARNING +"Opcion Invalida. Intente de nuevo" + RESET)
                    
                #Llama la funcion para verificar si el producto esta en el inventario
                buscar_producto(nombre_buscar,inventario)

                #valicion par mas intentos del proceso anterior
                if validacion() == "2":
                    break

        case "3":
            print("\n-----------------Actualizar Precio----------------\n")
            while True:
                #Verificacion de nombre 
                while True:
                    nombre_editar = input("Ingrese por favor el nombre del producto: ")
                    if nombre_editar.replace(" ", "").isalpha():
                        break
                    else:
                        print(WARNING +"Opcion Invalida. Intente de nuevo" + RESET)    

                #Llama la funcion para actualizar el precio 
                editar_precio(nombre_editar,inventario)    

                #valicion par mas intentos del proceso anterior
                if validacion() == "2":
                    break
        case "4":
            print("\n-----------------Eliminar Producto----------------\n")
            while True:

                #Verificacion de nombre 
                while True:
                    producto_eliminar = input("Ingrese por favor el nombre del producto: ")
                    if producto_eliminar.replace(" ", "").isalpha():
                        break
                    else:
                        print(WARNING +"Opcion Invalida. Intente de nuevo" + RESET)

                eliminar_producto(producto_eliminar,inventario)

                #valicion par mas intentos del proceso anterior
                if validacion() == "2":
                    break
        case "5":
            print(SUCCESS + "\n--------------Valor total del inventario-------------\n")
            #Llama la funcion para calcular el valor del inventario
            valor_total_inventario(inventario)
            print("---------------------------------------------------\n" + RESET)

        case "6":
            #Llama la funcion que muestra el inventario
            mostrar_inventario(inventario)
        case "7":
            print("Fin de programa")
            break
            
      
        
        
        
        
            
                

        
    