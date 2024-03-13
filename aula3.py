"""
Programação estruturada dia 04/03/2024

Tópicos da aula
    -Funções
        -Evitar duplicidade de código (repetição)
        -Organização

Princípio SOLID
- SRP: Single Responsibility Principle
"""

# def = definir/declarar uma função
def cabecalho(título):
    traco()
    print(título)
    traco()


def traco():
    print("-" * 30)


cabecalho("Introdução") # executa tudo que está dentro do def
cabecalho("Relatório de pagamento")


"""
Faça uma função media(), que recebe os parâmetros posicionais ap1, ap2 e ac, e retorne a média de avaliações, utilizando a fórmula M = (AP1 + AP2) * 0.4 + AC * 0.2.
"""

def media(ap1, ap2, ac):
    return round((ap1 + ap2) * 0.4 + ac * 0.2, 2)


"""
Monte um conversor de temperatura, que recebe uma temperatura em graus Fahrenheit e devolva a temperatura em graus Celsius. A fórmula para conversão é C / 5 = (F - 32) / 9.
"""

def conv_temp(temp_fahr):
    return round(((temp_fahr - 32)/9)*5, 2)

def main():
    print(media(10, 9, 8))
    print(media(8 , 7 , 3))
    print("A temperatura em Celsius é:", conv_temp(100))

main()