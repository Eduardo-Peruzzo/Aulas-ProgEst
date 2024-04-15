# Esta é uma linha de comentário, o código não vai executar nada a direita da #, o atalho ctrl+; enquanto algo está selecionado transforma em comentário

"""
Um comentário de várias linhas pode ser feito usando as três " no início e no final.
"""

print("Olá, mundo!", end="... ")
print("Olá,","mundo!")
print("Ana tem 18 anos")
print("Ana tem", 18, "anos")
print("Ana tem", 18, "anos", sep="--")

"""
Tipos de dados em Python

- 4 tipos de dados primitivos
    -Números inteiros (int)
    -Números decimais (float)
    -Booleanos (bool)
    -Texto (string)

"""

print(-20, 4, 5, 18, 15215, sep="; ")
print(4.5, 2.5, 6.5, sep="; ")
print(4,5, sep="; ")
print("""representação de um
texto de múltiplas linhas""")
print('Olá, "mundo"!')
print("Olá, \"mundo\"!")
print("Olá, \n mundo!")
print("Olá, \t mundo!")

# input("Informe o seu nome: ")

# print(type(input("Informe o seu nome: ")))

# print(input("Informe o seu nome: "))

nome = input("Informe seu nome: ")
print("Olá, ", nome)

print(type("2"))
print(type(int("2")))
print(type(2))

# Todo dado diferente de 0, 0.0, "", etc. são considerados como True
print(bool(""))
print(bool("Olá, mundo"))
print(bool(0))
print(bool(34.512))

x = 10

if x:
    print("Diferente de zero")