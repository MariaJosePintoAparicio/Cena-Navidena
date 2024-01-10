class Estudiante:
    def _init_(self, nombre, edad, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def categorizar_imc(self, imc):
        if imc < 18.5:
            return "peso  BAJO"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidad grado I"
        elif 35 <= imc < 39.9:
            return "Obesidad grado II"
        else:
            return "Obesidad grado III"

estudiantes = []
for _ in range(20):
    nombre = input("Nombre  estudiante: ")
    edad = int(input("Edad: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    
    estudiante = Estudiante(nombre, edad, peso, altura)
    estudiantes.append(estudiante)


pesoIdeal = obesidadI = obesidadII = obesidadIII = sobrepeso = 0

for estudiante in estudiantes:
    imc = estudiante.calcular_imc()
    categoria = estudiante.categorizar_imc(imc)

    if categoria == "Peso normal":
        pesoIdeal += 1
    elif categoria == "Obesidad grado I":
        obesidadI += 1
    elif categoria == "Obesidad grado II":
        obesidadII += 1
    elif categoria == "Obesidad grado III":
        obesidadIII += 1
    elif categoria == "Sobrepeso":
        sobrepeso += 1


print("\nReporte de Salud:")
print(f"a. Peso Ideal: {pesoIdeal} estudiantes")
print(f"b. Obesidad Grado I: {obesidadI} estudiantes")
print(f"c. Obesidad Grado II: {obesidadII} estudiantes")
print(f"d. Obesidad Grado III: {obesidadIII} estudiantes")
print(f"e. Sobrepeso: {sobrepeso} estudiantes")