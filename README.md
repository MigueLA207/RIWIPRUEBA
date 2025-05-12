# Sistema de invenatio
This project is an application that allows you to take inventory of a store effectively, using dictionaries, allows you to do basic operations like as adding, consulting, updating and delete products.

## Characteristics
  - Add products to inventory
  - search products in stock
  - Update product prices
  - Delete inventory products
  - Calculate the total inventory value
  - Input validations for each data

## Instrucciones de uso
 1. Install python (only if you don't)
 2. Download the file and decompress in a single folder 
 3. When running the program, you going to enter 5 products that will be stored in the inventory. The user can choose if they want to enter more products
 4. The system will throw 7 options
 5. The user will choose one of the options and enter to that opcion.
 6. According to the option there will be different inputs that the user must enter correctly 
 7. Ask at the end of each option, if you want to repeat the process or go out to the main menu
 8. After touring each option, the only option to leave the program is 7.

## Ejemplos de datos de entrada
- case 1:
     input: 
        Ingrese por favor el nombre del producto: miel 
        Ingrese por favor el precio del producto: 1200
        Ingrese por favor la cantidad de productos que hay: 30
     -output:
        "Producto ingresado con exito"
     
- case 2:
       input: 
        Ingrese por favor el nombre del producto: miel
     -output:
        Busqueda realizada con exito
        Nombre: miel -- Precio: 1200.0 -- Cantidad: 30 

- case 3:
       Input:
         Ingrese por favor el nombre del producto: miel
         Digita el nuevo precio para este producto: 2000
       - Salida:
         Precio editado con exito
       
- case 4:
       Input:
          Ingrese por favor el nombre del producto: miel
       - output:
          Producto eliminado con exito

- caso 5:
       Input:
          None
       - output:
          -Valor total del inventario-
          El valor total del inventario es de: $36000.00

- case 6:
       Input:
          None
       - output:
          Lista de productos
          Nombre: miel -- Precio: $1200.0 -- Cantidad: 20
      
- case 7:
        Input:
          None
        - output:
          Fin del programa. Adioss 👍👍👍       
                
## Explain
Validations are used in the code to have a good user experience, in addition to giving something organized and pleasant to the eye.
The logic in the code is based on functions, the input data is requested in the index and sent as parameters to the functions located in another file called functions.py


     
      
    
    
