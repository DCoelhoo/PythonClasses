#Exercicio 1

nota = input("Escreva a sua nota: ")

if 20 >= int(nota) >= 0:
    print("A nota é valida.")
else:
    print("A nota não é valida.")


#Exercicio 2

for x in range(10, 20):
    x = x * 1.8 + 32
    print(x)



#Exercicio 3

x = input("Escreva um numero positivo: ")

if int(x) <= 0:
    print("Valor introduzido errado.")
else:
    x = int(x) - 1
    for i in range(int(x)):
        print(int(x) - int(i))

#Exercicio 4
import math

raio = input("Escreva o raio do circulo: ")

areaC = int(raio) * 2 * math.pi
print("A area do circulo é: ", round(areaC, 2))