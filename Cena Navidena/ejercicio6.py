class Ciudad:
    def _init_(self, nombre):
        self.nombre = nombre
        self.sismos = []

def registrar_ciudad(ciudades, nombre):
    ciudad = Ciudad(nombre)
    ciudades.append(ciudad)
    print(f"Ciudad {nombre} registrada.")

def registrar_sismo(ciudades, ciudad_index, magnitud):
    ciudad = ciudades[ciudad_index]
    ciudad.sismos.append(magnitud)
    print(f"Sismo registrado en la ciudad {ciudad.nombre}.")

def buscar_sismos(ciudades, ciudad_index):
    ciudad = ciudades[ciudad_index]
    print(f"Sismos registrados en la ciudad {ciudad.nombre}: {ciudad.sismos}")

def informe_riesgo(ciudades):
    for ciudad in ciudades:
        promedio_sismos = sum(ciudad.sismos) / len(ciudad.sismos)
        riesgo = ""
        if promedio_sismos < 2.5:
            riesgo = "Amarillo (Sin riesgo)"
        elif 2.6 <= promedio_sismos <= 4.5:
            riesgo = "Naranja (Riesgo medio)"
        else:
            riesgo = "Rojo (Riesgo alto)"
        print(f"Ciudad {ciudad.nombre}: {riesgo} - Promedio de sismos: {promedio_sismos}")

# Código de inicialización
ciudades_sismos = []

# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Registrar Ciudad")
    print("2. Registrar Sismo")
    print("3. Buscar Sismos por Ciudad")
    print("4. Informe de Riesgo")
    print("5. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        nombre_ciudad = input("Ingrese el nombre de la ciudad: ")
        registrar_ciudad(ciudades_sismos, nombre_ciudad)

    elif opcion == 2:
        ciudad_index = int(input("Ingrese el índice de la ciudad: "))
        magnitud_sismo = float(input("Ingrese la magnitud del sismo: "))
        registrar_sismo(ciudades_sismos, ciudad_index, magnitud_sismo)

    elif opcion == 3:
        ciudad_index = int(input("Ingrese el índice de la ciudad: "))
        buscar_sismos(ciudades_sismos, ciudad_index)

    elif opcion == 4:
        informe_riesgo(ciudades_sismos)

    elif opcion == 5:
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")