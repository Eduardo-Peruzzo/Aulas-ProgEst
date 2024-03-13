"""
Programação estruturada dia 06/03/2024

Tópicos da aula
    -Estruturas de repetição
        -while -> quando não sabemos quantas vezes vamos executar a repetição
        -for -> quando queremos acessar todos os elementos de uma coleção de dados
"""

def contagem_regressiva(num):
    while num >= 0:
        print(num)
        num -= 1

contagem_regressiva(5)

# não criar loops infinitos como esse
def contagem_regressiva2(num):
    while num >= 0:
        print(num)

# contagem_regressiva2(5)

print("-" * 30)

def contagem_regressiva3(num):
    for cont in range(num, -1, -1):
        print(cont)

contagem_regressiva3(3)

print("-" * 30)

print(list(range(4)))
print(list(range(4, 10)))
print(list(range(4, 20, 2)))
print(list(range(4, -20, 2)))

print("-" * 30)

def ola_infinity(num):
    for _ in range(num):
        print("olá")

ola_infinity(10)

print("-" * 30)

def le_coisas():
    texto = "1"
    while texto != "":
        texto = input("Digite um número ou informe seu nome: ")
        if texto.isnumeric():
            continue # interrompe o loop atual e volta para o while
        print(texto)

# le_coisas()

def le_nome():
    while True:
        nome = input("Informe seu nome: ")
        if nome:
            break # encerra a estrutura de repetição de vez, e segue o código
    print(nome)

le_nome()

def e_primo(num):
    for div in range(2, num):
        if not num % div:
            print("Não é primo")
            break
    else: # só entra no else se não rodar o break, funcionam em conjunto
        print(num, "é primo")

e_primo(7)
e_primo(8)
e_primo(11)
e_primo(12)



"""
Elaborar uma função conta_pares(min, max) para exibir todos os valores entre min e max, com um incremento de 2, separando-os com um hífen. Ex.: 2 – 4 – 6 – 8 – 10 – 12 – 14.
"""

def conta_pares(min, max):
    if min % 2:
        min += 1
    for num in range(min, max + 1, 2):
        if num >= max - 1:
            print(num)
        else:
            print(num, end=" - ")

conta_pares(2, 8)
conta_pares(2, 9)
conta_pares(1, 8)
conta_pares(1, 9)

"""
Faça um programa que calcule o fatorial de um número inteiro positivo fornecido pelo usuário. Ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120.
"""

def fatorial():
    fat = 1
    num = int(input("Digite um número inteiro maior que zero: "))
    for mult in range(1, num + 1):
        fat *= mult
    return fat

print(fatorial())