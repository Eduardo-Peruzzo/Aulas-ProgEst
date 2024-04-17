"""
Programação Estruturada
2024.1
17/04/2024

Bibliotecas e pacotes em Python
"""
import time
import pprint
import pygame

alunos = [
    {
        "matricula": 1414,
        "nome": "Eduardo"
    },
    {
        "matricula": 124,
        "nome": "Jonas"
    },
    {
        "matricula": 18546,
        "nome": "Carlinhos Brown"
    }
]
print(alunos)
print("=-" * 30)
pprint.pprint(alunos, indent=8)

def fatorial(num: int):
    fat = 1
    for i in range(1, num + 1):
        fat *= i

    return fat

inicio = time.time()
fatorial(10)
print("Tempo decorrido: {} segundos".format(time.time() - inicio))

