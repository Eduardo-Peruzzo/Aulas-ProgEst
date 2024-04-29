"""
Realizar as operações
"""
# Referência relativa
from numeros.operacoes import arit, exponencial

def selecionar_operacao(n1, n2, operacao):
    match operacao:
        case "+":
            print(arit.soma(n1, n2))
        case "-":
            print(arit.subtracao(n1, n2))
        case "*":
            print(arit.multiplicacao(n1, n2))
        case "/":
            print(arit.divisao(n1, n2))
        case "**":
            print(exponencial.potencia(n1, n2))
        case "raiz":
            print(exponencial.raiz(n1, n2))

print(__name__)