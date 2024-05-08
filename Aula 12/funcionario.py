class Funcionario:
    def __init__(self, nome, email, matricula) -> None:
        self.nome = nome
        self.email = email
        self.matricula = matricula


    def trocar_email(self, novo_email):
        self.email = novo_email

    def __str__(self) -> str:
        return self.nome
