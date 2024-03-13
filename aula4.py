"""
Implemente um programa que receba dois números e retorne o maior deles.
"""

def recebe_num(num1, num2):
    if num1 > num2:
        return num1
    return num2

print(recebe_num(57, 32))

"""
Faça um programa que verifique se uma letra é vogal ou consoante.
"""

def letras(letra):
    match letra:
        case "a" | "e" | "i" | "o" | "u":
            print("é par")
        case _:
            print("é impar")

letras("g")

"""
Faça um programa que receba três notas, calcule sua média aritmética simples e apresente na tela uma das seguintes informações:

A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
A mensagem “Reprovado”, se a média for menor do que sete;
A mensagem “Aprovado com Distinção”, se a média for igual a dez;
A mensagem “Nota inválida!” toda vez que for inserido um valor inválido.
"""

def media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media < 0 or media > 10:
        print("Nota inválida!")
    elif media == 10:
        print("Aprovado com Distinção!")
    elif media >= 7:
        print("Aprovado!")
    elif media < 7:
        print("Reprovado!")


media(10, 10 ,10)




"""
Programação estruturada dia 06/03/2024

Tópicos da aula
    -Estruturas de decisão
        -if/elif/else
        -match/case
"""

# def saudacao(turno):
#     if turno == "m":
#         print("bom dia")
#     else:
#         if turno == "t":
#             print("boa tarde")
#         else:
#             turno == "n"
#             print("boa noite")

# É a mesma coisa que o de baixo, porém mais longo

def saudacao(turno):
    if turno == "m":
        print("bom dia")
    elif turno == "t":
        print("boa tarde")
    elif turno == "n":
        print("boa noite")
    else:
        print("Informação inválida")



saudacao("m")
saudacao("t")
saudacao("n")
saudacao("")

def saudacao(turno):
    if turno == "m":
        return "bom dia"
    if turno == "t":
        return "boa tarde"
    if turno == "n":
        return "boa noite"
    return "Informação inválida"

def e_par(num):
    return "é par" if num % 2 == 0 else "é impar"

print(e_par(4))

def le_nome():
    nome = input("Informe seu nome: ")
    if nome == "":
        print("Nome inválido")

    return nome

print(le_nome())

def avaliacao(conceito):
    match conceito:
        case "bom":
            print("Aprovado")
        case "otimo":
            print("Aprovado")
        case _: # default case
            print("Reprovado")

def avaliacao2(conceito):
    match conceito:
        case "bom" | "otimo":
            print("Aprovado")
        case _:
            print("Reprovado")


avaliacao("ruim")
avaliacao2("bom")