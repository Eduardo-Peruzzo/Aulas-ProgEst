"""
Receber dados da calculadora
"""

from numeros import decisor

def iniciar():
    n1 = float(input("Informe o primeiro número: "))
    operacao = input("Informe a operação (+, -, *, /, **, raiz): ")
    n2 = float(input("Informe o segundo número: "))

    decisor.selecionar_operacao(n1, n2, operacao)

print(__name__)