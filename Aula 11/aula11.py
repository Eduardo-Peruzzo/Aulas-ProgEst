"""
SRP - Single Responsibility Principle
"""
# Referência absoluta
from calc import calculadora

def main():
    calculadora.iniciar()

print(__name__)

if __name__ == "__main__":
    main()

