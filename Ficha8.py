# Exercicio 1

numeros = [1, 5, 3, 6, 22, 45, 63, 30, 344, 22, 12, 25, 10]

# a
numeros.reverse()
print(numeros)

# b
# Exercicio 1

# Exercicio 1

file = open('texto.txt', 'r')
texto = file.read()
print(texto)

vCounter = {}

for i in "aeiou":
    counter = texto.lower().count(i)
    vCounter[i] = counter

print("A/a: ", vCounter["a"])
print("E/e: ", vCounter["e"])
print("I/i: ", vCounter["i"])
print("O/o: ", vCounter["o"])
print("U/u: ", vCounter["u"])

file.close()

#Exercicio 2

file2 = open('texto2.txt', 'r')
texto2 = file2.readline()
file.close()

print("Frase Antiga: ", texto2)

palavras = set()


for k in texto2.split():
    if k not in palavras:
        resultado = resultado + k + palavras.add(k)

print("Frase Nova: ", resultado)

file2 = open('texto2.txt', 'w')
file2.write(resultado)

file2.close()
