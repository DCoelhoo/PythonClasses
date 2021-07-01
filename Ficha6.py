# Exercicio 1

numeros = [1, 5, 3, 6, 22, 45, 63, 30, 344, 22, 12, 25, 10]

# a
numeros.reverse()
print(numeros)

# b
# Exercicio 1

string = str(input("Escreva qualquer coisa: "))

vogalA = string.count("a")
vogalE = string.count("e")
vogalI = string.count("i")
vogalO = string.count("o")
vogalU = string.count("u")

vogal1 = string.count("A")
vogal2 = string.count("E")
vogal3 = string.count("I")
vogal4 = string.count("O")
vogal5 = string.count("U")

totalA = vogalA + vogal1
totalE = vogalE + vogal2
totalI = vogalI + vogal3
totalO = vogalO + vogal4
totalU = vogalU + vogal5

print("Ocorrências da Vogal a: ", totalA)
print("Ocorrências da Vogal e: ", totalE)
print("Ocorrências da Vogal i: ", totalI)
print("Ocorrências da Vogal o: ", totalO)
print("Ocorrências da Vogal u: ", totalU)

# Exercicio 2

string = str(input("Escreva uma frase que contenha várias vezes a palavra 'ana': "))
substring = string.replace("ana", "")

print(substring)

# Exercicio 3
string = str(input("Escreva uma frase: "))
novaString = string.replace(" ", "")

print(novaString)


# Exercicio 4
string = str(input("Escreva uma frase: "))
novaString = string.replace(" ", "##")

print(novaString)
