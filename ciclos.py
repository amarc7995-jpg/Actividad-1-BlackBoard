import math
for i in range(11):
    print(i)

for i in reversed(range(11)):
    print(i)
 
llamadas = ["#", "##", "###","####","#####","######","#######"]

for i in llamadas:
    print(i)

for i in range(8):
    for j in range(8):
        print("#", end= " ")
    print() 

for i in range(11):
    resultado = i * i
    print(f"{i} x {i} =, {resultado}") 


programas = ["Python", "Numpy", "Pandas","Django","Flask"]
for programa in programas :
    print(programa)


for i in range(0, 101, 2):
    print(f"El número {i} es par.")

for i in range(1, 101, 2):
    print(f"El número {i} es impar.")