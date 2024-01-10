suma = 0
isActive = True
while(isActive):
    try:
        for i in range(3):
            num = int(input('Ingrese un numero entero: '))
            if (num < 0):
                print('El numero debe de ser positivo')
                suma = 0
                break
            else:
                suma = suma + num
        print(f'La suma de los numeros ingresados es: {suma}')
    except ValueError:
        print("Error en el dato, Debe ingresar un numero entero")
    else:
        isActive = False