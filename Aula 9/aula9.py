"""
Programação Estruturada
2024.1
15/04/2024

Tratamento de erros e exceções
    try / except / else / finally
"""

def divisao(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Erro no cálculo! Divisão por 0")
    except TypeError:
        print("Erro no cálculo! Tipos incompatíveis")
    except Exception as erro:
        print("Erro de tipo {}: {}".format(type(erro).__name__, erro))

divisao(2, 1)
divisao(2, 2)
divisao(2, 0)   # ZeroDivisionError
divisao("a", 2) # TypeError

def terceira_letra():
    nome = input()
    try:
        print(f"A terceira letra é {nome[2]}")
    except IndexError:
        print("O nome precisa ter pelo menos três letras")
    else: # só entra se não surgiu uma excessão
        print("Leitura feita com sucesso")
    finally: #entra sempre, independente de ter dado erro ou não
        print("Fim do try")


# terceira_letra()

def divisao2(a, b):
    if b == 0:
        raise ValueError

# divisao2(2, 0)

def func1():
    raise NotImplementedError

def func2():
    raise NotImplementedError

def func3():
    raise NotImplementedError

class TamanhoExcedidoError(Exception):
    pass

lista = [1, 2, 3, 4, 5]

if len(lista) > 4:
    raise TamanhoExcedidoError

