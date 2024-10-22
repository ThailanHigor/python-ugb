
class Skin:
    """Classe que representa uma skin de um jogo na Steam."""

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

    def inspecionar(self):
        print("Você está vendo a skin: {self.nome}")



class ArmaDourada(Skin):
    def inspecionar(self):
        print("Você está vendo a skin: {self.nome}. Possui um efeito especial em Dourado.")


class ArmaDeBronze(Skin):
    def inspecionar(self):
        print("Você está vendo a skin: {self.nome}. Possui um efeito especial em Bronze.")
 




