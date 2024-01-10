import os
contb = 0
contp = 0
conts = 0
contob = 0
contobe = 0
contobes = 0

for i in range(1,6,1):
    print("")
    print(f"ESTUDIANTE {i}")
    print("")
    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    imc = peso / (altura ** 2)
    print("RESULTADO: ")
    print("")
    if imc < 18.5:
        print("Bajo peso") 
        contb = contb + 1
        print(contb)
    elif 18.5 <= imc < 24.9:
        print("Peso normal")
        contp = contp + 1
        print(contp)
    elif 25 <= imc < 29.9:
        print("Sobrepeso")
        conts = conts+ 1
        print(conts)
    elif 30 <= imc < 34.9:
        print("Obesidad grado I")
        contob = contob+ 1
        print(contob)
    elif 35 <= imc < 39.9:
        print("Obesidad grado II")
        contobe = contobe + 1
        print(contobe)
    else:
        print("Obesidad grado III")
        contobes = contobes+ 1
        print(contobes)
    os.system("pause")
    os.system("cls")   

print("Bajo peso: ",contb)
print("Peso normal: ",contp)
print("Sobrepeso: ",conts)
print("Obesidad grado I: ",contob)
print("Obesidad grado II: ",contobe)
print("Obesidad grado III: ",contobes)
