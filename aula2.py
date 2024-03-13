"""
Programação estruturada dia 28/02/2024

Tópicos da aula
    -Aritméticos
    -Atribuição
    -Comparação (ou relacionais)
    -Lógicos (ou booleanos)
"""

# Operadores aritméticos
# Quando ambos os operandos são números:

x = 10
y = 5

print(x + y) # soma
print(x - y) # subtração
print(x * y) # multiplicação
print(x / y) # divisão
print(x // y) # divisão inteira
print(x % y) # módulo (resto da divisão)
print(x ** y) # potência

print(round(x + y, 1)) # Define o número de casas decimais mostradas

# Quando um dos operandos for uma string:

print("A" * 10) # Repete a str o número de vezes especificado
print("A" + "B") # Junta as duas str

# Operadores de atribuição

x = 2
x += 1 # x = x + 1
x -= 4 # x = x - 4
x *= 6
x /= 2
x //=4
x **= 2
x %= 5
print(x)

# Operadores de comparação

a = 20
b = 15

print(a > b) # maior que
print(a < b) # menor que
print(a >= b) # maior ou igual a
print(a <= b) # menor ou igual a
print(a == b) # igual a
print(a != b) # diferente de

print("-" * 50)
# Operadores lógicos

c = True
d = False

print(c and d) # True se os dois valores forem verdadeiros apenas
print(c or d) # True se pelo menos um dos valores forem verdadeiros
print(not d) # Inverte o valor

# Type casting
idade = int(input("Informe sua idade: ")) # input recebe dados tipo str, e o int o transforma em um dado tipo int
print("Sua idade é " + str(idade)) # Transforma o dado int idade em um dado str e o exibe na mensagem

print("-" * 50)

"""
and se o primeiro for false, retornará o primeiro, se for true retornará o segundo, mesmo que o segundo seja false

or vai retornar o primeiro valor se for ele for true, e vai retornar sempre o segundo valor se o primeiro for false
"""


"""
Calculando a média da AP1, AP2 e AC
Calculada com a fórmula: (AP1 + AP2) * 0.4 + AC * 0.2
"""

ap1 = float(input("Insira a nota da sua AP1: "))
ap2 = float(input("Insira a nota da sua AP2: "))
ac = float(input("Insira a nota da sua AC: "))

print("A sua média é: ", round((ap1 + ap2) * 0.4 + ac * 0.2, 2))