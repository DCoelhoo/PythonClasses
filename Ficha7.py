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
# Exercicio 1
animais = {
    "Ziggy": "canario",
    "Pluto": "cao",
    "Kitty": "gato",
    "Nemo": "peixe",
    "Mickey": "rato"
}

# Exercicio 2
item = ""
x = 0
while x == 0:
    item = str(input("Escreva um novo nome para um animal de estimação: "))
    if item == "fim": break
    especie = str(input("Escreva a especie do mesmo: "))

    animais[item] = especie

print(animais)

# Exercicio 3
def search():
    x = 0
    while x == 0:
        chave = str(input("Escreva a chave do dado que procura: "))
        if chave in animais:
            valor = animais[chave]
            print("Chave: ", chave, "- Valor: ", valor)
            break
        else:
            print("Esta chave não existe, tente novamente.")
            continue

search()
