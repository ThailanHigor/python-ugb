from banco.database import BancoDeDadosJogos

class LojaSteamComBanco:
    def __init__(self):
        self.db = BancoDeDadosJogos("banco/loja_steam.db")
        self.db.criar_tabela()

    def adicionar_jogo_ao_banco(self, nome, categoria, preco):
        """Adiciona um jogo à loja e ao banco de dados."""

        self.db.adicionar_jogo(nome, categoria, preco)

    def listar_jogos_loja(self):
        """Lista todos os jogos disponíveis na loja, vindo do banco de dados."""

        jogos = self.db.listar_jogos()
        if jogos:
            print("Jogos disponíveis na loja:")
            for jogo in jogos:
                print(f"ID: {jogo[0]}, Nome: {jogo[1]}, Categoria: {jogo[2]}, Preço: {jogo[3]}")
        else:
            print("Nenhum jogo disponível na loja.")

    def buscar_jogo_na_loja(self, nome_jogo):
        """Busca um jogo pelo nome na loja e retorna suas informações, se encontrado."""

        jogos = self.db.listar_jogos()
        for jogo in jogos:
            if jogo[1].lower() == nome_jogo.lower():
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
