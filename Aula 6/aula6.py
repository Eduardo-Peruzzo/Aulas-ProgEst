"""
Programação estruturada dia 20/03/2024

Tópicos da aula
    -Listas
        -Mutáveis
        -Ordenados
    -Tuplas
        -imutáveis
        -Ordenados
"""

letras = ["A", "B", "C", "D", "E"]

print(letras[3])

print(letras)
letras[4] = "P"
print(letras)

print(letras[-1])
print(letras[-2])

numeros = range(1, 10)
print(numeros[-1])

# Slicing ou fatiamento
print(letras[1:4])
print(letras[1:])
print(letras[:4])
print(letras[:])
print(letras[::2]) # do início ao fim de 2 em 2
print(letras[::-1])

texto = "olá, mundo"
print(texto[::-1])

coordenadas = [[1, 0], [3, 4], [10, 11]]
print(coordenadas)
print(coordenadas[2])
print(coordenadas[1][1])

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(matriz)

# operador in / not in
print("F" in letras)
print("A" in letras)

if "B" in letras:
    print("A letra está na lista")

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()

for indice, letra in enumerate(letras):
    print(indice, letra, sep=' - ')

alunos = ["Jão", "Bernardo", "Dudu"]
notas = [1.2, 7.0, 10.0]

for aluno, nota in zip(alunos, notas):
    print("A nota do aluno", aluno, "foi", nota)

alunos_ordenados = sorted(alunos)
print(alunos_ordenados)
print(alunos)
print("-"*30)
alunos.sort()
print(alunos)

numeros = [1, 2, 3, 4, 5]
texto = ", ".join([str(num) for num in numeros])
print(texto)


# Tupla

tupla = (1, 2, 3)
print(tupla)
print(tupla[2])

