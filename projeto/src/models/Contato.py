class Contato:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def __str__(self):
        return f"{self.nome}: {self.senha}"
