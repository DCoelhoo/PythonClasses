# Exercicio 1

numeros = [1, 5, 3, 6, 22, 45, 63, 30, 344, 22, 12, 25, 10]

# a
numeros.reverse()
print(numeros)

# b
counter = 0
num = numeros
for i in numeros:
    numAtual = numeros.count(i)
    if (numAtual > counter):
        counter = numAtual
        num = i
print(num)


# Exercicio 2

tuplo = ()
x = list(tuplo)

elementos = int(input("Escreva um numero de elementos do tuplo: "))

for i in range(0, elementos):
    num = int(input("Escreva um numero: "))
    if num % 2 == 0:
        x.append(num)

tuplo = tuple(x)
print(tuplo)



# Exercicio 3

numeros = (10, 15, 3, 6, 99, 45, 63, 30, 344, 22, 4, 25, 10)

#a
print("O comprimento do tuplo é: ", len(numeros))

#b
print("O maior numero do tuplo é: ", max(numeros))
print("O menor numero do tuplo é: ", min(numeros))

#c
numeros2 = (21, 53, 23, 54, 22, 2, 1, 13)
numeros3 = numeros + numeros2

print(numeros3)

print("--------------------Impares---------------------------")

#d
for i in numeros3:
    if i % 2 == 1:
        print(i)

print("--------------------Multiplos de 5---------------------------")

#e
for x in numeros3:
    if x % 5 == 0:
        print(x)


# Exercicio 4
tabela = [[10.2, 12.5, 5.0, 2.1],
          [15.2, 6.3, 10.2, 5.2],
          [10.3, 8.5, 12.9, 25.1]]


def maxTabela():
    linhas = 0
    colunas = 0
    maxN = 0

    for linhas in tabela:
        for colunas in linhas:
            if colunas > maxN:
                maxN = colunas

    print(maxN)


maxTabela()
