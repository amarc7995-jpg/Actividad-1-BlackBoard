#Declara una función add_two_numbers. Toma dos parámetros y devuelve una suma
def add_two_numbers(a, b):
    return a + b
resultado = add_two_numbers(1,2)
print(resultado)

#El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una función que calcule el área_del_círculo.
import math
print("Calculo del área del círculo")
num1 = float(input("Ingresa el radio del circulo: "))
area_of_circle= math.pi*num1**2
print("Resultado:", area_of_circle)

# Comprueba si todos los elementos de la lista son tipos numéricos. Si no, dé una valoración razonable
print("Comprobación de datos numéricos")
def add_all_nums(*args):
    total = 0
    for num in args:
        if not isinstance(num, (int, float)):
         return "Error: todos los elementos deben ser números"
        total += num
    return total

#Escribe una función que convierta °C a °F, convert_celsius_to-fahrenheit. 
print("°C a °F")
num2 = float(input("Ingresa la temperatura en °C:"))
convert_celsius_tofahrenheit=(num2*(9/5))+32
print("La temperatura es de:", convert_celsius_tofahrenheit,"°F")

#Escribe una función que calcule el conjunto de soluciones de una ecuación cuadrática, solve_quadratic_eqn.
import math
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))
def solve_quadratic_eqn(a, b, c):
    if a == 0:
        return "No es una ecuación cuadrática"

    d = b**2 - 4*a*c

    if d < 0:
        return "No tiene soluciones reales"
    elif d == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return x1, x2
resultado = solve_quadratic_eqn(a, b, c)
print("Resultado:", resultado)

#Toma una lista como parámetro e imprime cada elemento de la lista
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

lista = []
while True:
  elemento = input("Ingresa un elemento: ")
  lista.append(elemento)
  imprimir_lista(lista)

#Toma una matriz como parámetro y devuelve el reverso de la matriz (use bucles).
def reverso_matriz(matriz):
    resultado = []

    for i in range(len(matriz) - 1, -1, -1):
        resultado.append(matriz[i])

    return resultado


matriz = []

for i in range(2):
    fila = []
    for j in range(3):
        valor = input(f"Ingresa valor [{i}][{j}]: ")
        fila.append(valor)
    matriz.append(fila)

reversa = reverso_matriz(matriz)

print("Matriz invertida:")
for fila in reversa:
    print(fila)
