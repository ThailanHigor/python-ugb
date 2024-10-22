
from skin import Skin

class Jogo:
    """Classe que representa um jogo na Steam."""

    def __init__(self, nome, categoria, preco):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.skins = []

    def __str__(self):
        return f"{self.nome} ({self.categoria}) - R${self.preco}"
    
    def dar_desconto(self, valor_em_reais):
        self.preco =  self.preco - valor_em_reais

    def adicionar_skin(self, skin):
      if isinstance(skin, Skin):
        self.skins.append(skin)
        print(f"Skin '{skin.nome}' adicionada ao jogo.\n")


    def listar_skins(self, skin):
      print("=== Skins Disponíveis no Jogo ===")
      for skin in self.skins:
          print(skin)
      print()