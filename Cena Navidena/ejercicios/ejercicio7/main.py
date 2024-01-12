import registro as reg
import menu
import os
productos = []
isActive = True
opcion = 0

while isActive:
    os.system("cls")  # Utiliza "clear" en lugar de "cls" si estás en un entorno Unix/Linux
    try:
        opcion = reg.menuPrincipal()
        if opcion == 1:
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            valor_compra = float(input("Ingrese el valor de compra del producto: "))
            valor_venta = float(input("Ingrese el valor de venta del producto: "))
            stock_minimo = int(input("Ingrese el stock mínimo permitido: "))
            stock_maximo = int(input("Ingrese el stock máximo permitido: "))
            proveedor = input("Ingrese el nombre del proveedor del producto: ")

            reg.registrar_producto(productos, codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor)
        elif opcion == 2:
            reg.visualizar_productos(productos)
        elif opcion == 3:
            codigo = input("Ingrese el código del producto: ")
            cantidad = int(input("Ingrese la cantidad a agregar/restar al stock: "))
            reg.actualizar_stock(productos, codigo, cantidad)
        elif opcion == 4:
            reg.informe_productos_criticos(productos)
        elif opcion == 5:
            reg.calcular_ganancia_potencial(productos)
        elif opcion == 6:
            isActive = False
        else:
            print("Opción no válida. Intente nuevamente.")
            os.system("pause")

    except ValueError:
        print("\nError en el dato ingresado...\n")
        os.system("pause")