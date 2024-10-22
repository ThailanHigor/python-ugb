# loja.py

from jogo import Jogo

class LojaSteam:
    def __init__(self):
        self.jogos_disponiveis = [
            Jogo("CS:GO", "FPS", 0.0),
            Jogo("Dota 2", "MOBA", 0.0),
            Jogo("Cyberpunk 2077", "RPG", 199.90),
            Jogo("Valorant", "FPS", 0.0),
            Jogo("The Witcher 3", "RPG", 99.90)
        ]

    def listar_jogos_loja(self):
        print("=== Jogos Disponíveis na Loja ===")
        for jogo in self.jogos_disponiveis:
            print(jogo)
        print()

    def buscar_jogo_na_loja(self, nome_jogo):
        for jogo in self.jogos_disponiveis:
            if jogo.nome == nome_jogo:
                return jogo
        return None

    def comprar_jogo(self, nome_jogo):
        jogo_encontrado = self.buscar_jogo_na_loja(nome_jogo)
        if jogo_encontrado:
            return jogo_encontrado
        else:
            print(f"Jogo '{nome_jogo}' não encontrado na loja.\n")

    def verificar_promocoes(self):
        print("Promoções: Nenhuma promoção no momento.\n")
