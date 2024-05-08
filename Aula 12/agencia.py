from conta import Conta
from gerente import Gerente

class Agencia:
    """
    endereço
    numero
    gerente
    """

    def __init__(self, numero, endereco, gerente: Gerente) -> None:
        self.numero = numero
        self.endereco = endereco
        self.gerente = gerente
        self.contador_de_contas = 0

    def __str__(self) -> str:
        return "Agência número {} - {}, gerente {}.".format(self.numero, self.endereco, self.gerente)

    def __eq__(self, __value: object) -> bool:
        if __value.__class__ != self.__class__:
            return False

        return self.numero == __value.numero

    def abrir_nova_conta(self, titular):
        self.contador_de_contas += 1
        if self.gerente.autorizar_abertura_conta(self.contador_de_contas):
            return Conta(self.contador_de_contas, titular)

        return None
