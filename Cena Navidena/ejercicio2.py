import os
isActiv = True

while(isActiv):
    try:
        print("")
        nombre = input('nombre del Estudiante: ')
        peso = float(input('peso (kg) del Estudiante: '))
        altura = float(input('altura (m) del Estudiante: '))
        print("----------------------------------------------")
        print("")
    except ValueError:
        print('Dato incorrecto')
    else:
        isActiv=False
imc = peso/(altura**2)  
print("")
print("RESULTADO FINAL")   
print("")
if(imc >= 18.5 and imc <= 24.9):
    print(f'El Estudiante {nombre} presenta un IMC NORMAL  {imc}')
elif(imc >= 25 and imc <= 29.9):
    print(f'El Estudiante {nombre} presenta un IMC SOBREPESO {imc}')
elif(imc >= 30 and imc <= 34.9):
    print(f'El Estudiante {nombre} presenta un IMC OBESIDAD I  {imc}')
elif(imc >= 35 and imc <= 39.9):
    print(f'El Estudiante {nombre} presenta un IMC OBESIDAD II {imc}')
else:
    print(f'El Estudiante {nombre} presenta un IMC OBESIDAD III  {imc}')