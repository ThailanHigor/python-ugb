from jogo import Jogo


class BibliotecaSteam:
    def __init__(self):
        self._jogos = []
        

    def adicionar_jogo(self, jogo):
        if isinstance(jogo, Jogo):
            self._jogos.append(jogo)
            print(f"Jogo '{jogo.nome}' adicionado à biblioteca.\n")
        else:
            print("Erro: o jogo adicionado deve ser uma instância da classe Jogo.")


    def listar_jogos(self):
        if not self._jogos:
            print("Sua biblioteca está vazia.\n")
        else:
            print("=== Seus Jogos ===")
            for jogo in self._jogos:
                print(jogo)
            print()


    def remover_jogo(self, nome_jogo):
        for jogo in self._jogos:
            if jogo.nome == nome_jogo:
                self._jogos.remove(jogo)
                print(f"Jogo '{nome_jogo}' removido da biblioteca.\n")
                return
        print(f"Jogo '{nome_jogo}' não encontrado na biblioteca.\n")