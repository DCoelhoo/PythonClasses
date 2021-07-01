import math

class empregado:
    def __init__(self, numero, nome, salBruto):
        self.numero = numero
        self.nome = nome
        self.salBruto = salBruto

    def calcIRS(self):
        if self.salBruto >= 2000.00:
            irs = 25.0
        elif self.salBruto >= 1000.00 and self.salBruto < 2000.00:
            irs = 20.0
        elif self.salBruto < 1000.00:
            irs = 17.5
        return "IRS = {}%".format(irs)

    def calcSS(self):
        ss = 11
        return "SS = {}%".format(ss)

    def calcSalLiquido(self):
        salLiquido = (self.salBruto - ((self.salBruto * self.calcIRS()) / 100))
        return "Salario Liquido = {}".format(salLiquido)

class professor(empregado):
    def __init__(self, numero, nome, salBruto, areaEnsino):
        self.areaEnsino = areaEnsino
        empregado.__init__(self, numero, nome, salBruto)




numero = int(input("Escreva o seu numero: "))
nome = str(input("Escreva o seu nome: "))
salBruto = float(input("Escreva o seu salário bruto: "))

empregado1 = empregado(numero, nome, salBruto)

print(empregado1.calcIRS())
print(empregado1.calcSS())
print(empregado1.calcSalLiquido())

numerop = int(input("Escreva o seu numero: "))
nomep = str(input("Escreva o seu nome: "))
salBrutop = float(input("Escreva o seu salário bruto: "))
areaEnsino = str(input("Escreva a sua area de ensino: "))

professor1 = professor(numerop, nomep, salBrutop, areaEnsino)

print(professor1.calcIRS())
print(professor1.calcSS())
print(professor1.calcSalLiquido())

#Exercicio 3
print(" ")
print(" ")
print("Calculadora")

option = 10

while option != 0:
    print("Escreva 1 para somar")
    print("Escreva 2 para subtrair")
    print("Escreva 3 para multiplicar")
    print("Escreva 4 para dividir")
    print("Escreva 5 para calcular a raiz quadrada")
    print("Escreva 6 para calcular o Logaritmo")
    print("Escreva 7 para calcular o seno")
    print("Escreva 0 para sair")
    option = int(input())
    if option == 1:
        print("---SOMA---")
        num1 = int(input("Escreva o primeiro numero:"))
        num2 = int(input("Escreva o primeiro numero:"))
        print(num1 + num2)
    elif option == 2:
        print("---SUBTRACAO---")
        num1 = int(input("Escreva o primeiro numero:"))
        num2 = int(input("Escreva o primeiro numero:"))
        print(num1 - num2)
    elif  option == 3:
        print("---MULTPLICACAO---")
        num1 = int(input("Escreva o primeiro numero:"))
        num2 = int(input("Escreva o primeiro numero:"))
        print(num1 * num2)
    elif  option == 4:
        print("---DIVIDIR---")
        num1 = int(input("Escreva o primeiro numero:"))
        num2 = int(input("Escreva o primeiro numero:"))
        if num2 == 0:
            print("Não é possivel dividir por 0.")
            zero = 0
            print(zero)
        else:
            print(num1 / num2)
    elif  option == 5:
        print("---RAIZ QUADRADA---")
        num1 = int(input("Escreva um numero para calcular a raiz quadrada:"))
        print(math.sqrt(num1))
    elif  option == 6:
        print("---LOGARITMO---")
        num1 = int(input("Escreva um numero para calcular o logaritmo:"))
        num2 = int(input("Escreva a sua base: "))
        print(math.log(num1, num2))
    elif  option == 7:
        print("---SENO---")
        num1 = int(input("Escreva um numero para calcular o seno:"))
        print(math.sin(num1))
