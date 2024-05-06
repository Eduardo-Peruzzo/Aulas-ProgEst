class Conta:
    """
    numero
    saldo
    titular
    """
    # Método construtor
    def __init__(self, numero, titular) -> None:
        self.numero = numero
        self.saldo = 0
        self.titular = titular

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False

        self.saldo -= valor
        return True

    # sobrescrita de metodo
    def __str__(self) -> str:
        return "Conta de {}, numero {}, saldo R${:.2f}".format(self.titular, self.numero, self.saldo)

    def __eq__(self, __value: object) -> bool:
        if __value.__class__ != self.__class__:
            return False

        return self.numero == __value.numero