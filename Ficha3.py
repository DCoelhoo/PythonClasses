#Exercicio 1

soma = 0

for i in range(0, 22, 2):
    soma = soma + i
    print("Soma = ", soma)

#Exercicio 2

contMedia1 = 0
contMedia2 = 0
contMedia3 = 0

media1 = 0.0
media2 = 0.0
media3 = 0.0

temperatura = []

for i in range(0, 12):
    inputTemp = int(input("Introduza uma temperatura: "))
    temperatura.append(inputTemp)

for k in range(len(temperatura)):
    if 10 < temperatura[k] < 15: #media 1 +10 / -15
        media1 += temperatura[k]
        contMedia1 += 1
    elif 20 < temperatura[k] < 30: #media 2 +20 / -30
        media2 += temperatura[k]
        contMedia2 += 1
    else:
        media3 += temperatura[k] #resto
        contMedia3 += 1


media1 = media1 / contMedia1
media2 = media2 / contMedia2
media3 = media3 / contMedia3

media1Str = str(media1)
media2Str = str(media2)
media3Str = str(media3)


print("A media 1 vai ser: " + media1Str)
print("A media 2 vai ser: " + media2Str)
print("A media 3 vai ser: " + media3Str)


#Exercicio 3

temperaturaC = int(input("Escreva uma temperatura: "))

def conversor():
    temperaturaF = temperaturaC * 1.8 + 32
    temperaturaFStr = str(temperaturaF)
    print("Temperatura em Fahrenheit: " + temperaturaFStr)



conversor()


#Exercicio 4

def intermedio():
    if n1 < n2 < n3:
        print("O numero intermedio é o segundo numero")
    elif n2 < n1 < n3:
        print("O numero intermedio é o primeiro numero")
    elif n1 < n3 < n2:
        print("O numero intermedio é o terceiro numero")



n1 = int(input("Escreva um numero: "))
n2 = int(input("Escreva um numero diferente: "))
n3 = int(input("Escreva outro numero diferente: "))


intermedio()


#Exercicio 5

lista1 = ['Iva', 25, 'Rui', 19, 'Rato', 'abc', 33]
lista2 = [1, 2, 3, 4]

#a
print(lista1)

#b
print(lista1[2:5])

#c
print(lista1[:3])

#d
print(lista1[3:])

#e
lista3 = lista1 + lista2
print(lista3)


#Exercicio 6

def desenho(num):
    listaPadrao = []
    for i in range(1, num + 1):
        listaPadrao.append("* " * i)
    print("\n".join(listaPadrao))


num = int(input("Escreva um numero: "))
desenho(num)


#Exercicio 7

import math

def perimetro():
    form = 2 * math.pi * raio
    formStr = str(form)
    print("O perimetro da circunferência é: " + formStr)


raio = int(input("Escreva o raio de uma circunferência: "))
perimetro()

