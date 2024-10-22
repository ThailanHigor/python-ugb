import csv
from jogo import Jogo

class LojaSteam:
    def __init__(self):
        self.jogos_disponiveis = [
            Jogo("CS:GO", "FPS", 0.0),
            Jogo("Dota 2", "MOBA", 0.0)
        ]

        #self.carregar_jogos_csv("arquivos/jogos.csv")

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

    def adicionar_jogo(self, jogo):
        if isinstance(jogo, Jogo):
            self.jogos_disponiveis.append(jogo)
            print(f"Jogo '{jogo.nome}' adicionado à biblioteca.\n")
        else:
            print("Erro: o jogo adicionado deve ser uma instância da classe Jogo.")
                
    def verificar_promocoes(self):
        print("Promoções: Nenhuma promoção no momento.\n")

    
    def carregar_jogos_csv(self, arquivo_csv):
        """Carrega jogos de um arquivo CSV e os adiciona à loja."""
        
        self.jogos_disponiveis = []
        with open(arquivo_csv, mode='r', newline='') as arquivo:
            leitor_csv = csv.reader(arquivo)
            next(leitor_csv)
            for linha in leitor_csv:
                nome_jogo = linha[0]
                categoria = linha[1]
                preco = linha[2]
                self.adicionar_jogo(Jogo(nome_jogo, categoria, preco))
        print(f"Jogos carregados com sucesso do arquivo {arquivo_csv}.")