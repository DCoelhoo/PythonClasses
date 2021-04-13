#Exercicio 1

numeros = [1, 5, 3, 6, 22, 45, 63, 30, 344, 22, 12, 25, 10]
numeros2 = [21, 53, 23, 54, 22, 2, 1, 13]

#a
print(len(numeros))

#b
print(max(numeros))
print(min(numeros))

#c
numeros = numeros + numeros2
print(numeros)

#d
numeros.sort()
print(numeros)

#e
for i in range(len(numeros)):
    print(numeros[i], end=" - ")

print(" ")

#f
for i in range(len(numeros)):
    if numeros[i] % 2 == 1:
        print(numeros[i], end=" ")

print(" ")

#g
for i in range(len(numeros)):
    if numeros[i] % 5 == 0:
        print(numeros[i], end=" ")


#Exercicio 2

temperaturas = [ ]

for i in range(0, 7):
    tempInput = int(input("Escreva uma temperatura: "))
    temperaturas.append(tempInput)


sumTemp = sum(temperaturas)
mediaTemp = sumTemp / 7

print("A media das 7 temperaturas é ", mediaTemp)



#Exercicio 3

def mediaCal():
    sumTemp = sum(temperaturas)
    mediaTemp = sumTemp / 7
    print("A media das 7 temperaturas é ", mediaTemp)

temperaturas = [ ]

for i in range(0, 7):
    tempInput = int(input("Escreva uma temperatura: "))
    temperaturas.append(tempInput)


mediaCal()



#Exercicio 4

def volumeCalc(raio):
    volumeEsfera = (4 * 3.14 * raio ** 3) / 3
    print("O volume da esfera é : ", volumeEsfera, " centimetros cubicos.")

raio = int(input("Escreva o raio da esfera em centimetros: "))
volumeCalc(raio)



#Exercicio 5

def desenho(num):
    listaPadrao = []
    for linha in range(num, 0, -1):
        listaPadrao.append("* " * linha)
    print("\n".join(listaPadrao))


num = int(input("Escreva um numero: "))
desenho(num)



#Exercicio 6

min = 0
max = 30

print("Os 10 primeiros numeros primos são: ")

for num in range(min, max + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)