# main_simulacao.py

from loja import LojaSteam
from loja_com_banco import LojaSteamComBanco
from usuario import UsuarioPadrao, Amigo

def simulacao():
    """Função de simulação das funcionalidades da Steam."""
        
    # Criando a loja Steam
    loja = LojaSteam()
    #loja = LojaSteamComBanco()

    # Criando o usuário padrão logado
    usuario = UsuarioPadrao("JogadorPrincipal", "online")
    usuario.mostrar_info()

    # Exibindo os jogos disponíveis na loja
    #loja.adicionar_jogo_ao_banco("Teste", "FTPS", 50)
    loja.listar_jogos_loja()

    # Verificando promoções
    #loja.verificar_promocoes()

    # Simulando compra de jogos
    #novo_jogo = loja.comprar_jogo("Counter-Strike 2")
    #if novo_jogo:
    #  usuario.biblioteca.adicionar_jogo(novo_jogo)

    #novo_jogo = loja.comprar_jogo("Baldur's Gate")
    #if novo_jogo:
    #  usuario.biblioteca.adicionar_jogo(novo_jogo)

    # Listando os jogos na biblioteca após a compra
    #print("\n=== Sua biblioteca após as compras ===")
    #usuario.biblioteca.listar_jogos()

    # Removendo um jogo da biblioteca
    #usuario.biblioteca.remover_jogo("Counter-Strike 2")
    
    # Verificando a biblioteca após a remoção
    #print("\n=== Sua biblioteca após a remoção ===")
    #usuario.biblioteca.listar_jogos()

    # Gerenciando amigos
    #print("\n=== Gerenciamento de Amigos ===")
    #amigo1 = Amigo("Jogador1", "online")
    #amigo2 = Amigo("Jogador2", "offline")

    #usuario.amigos.adicionar_amigo(amigo1)
    #usuario.amigos.adicionar_amigo(amigo2)

    # Listando amigos
    #usuario.amigos.listar_amigos()

    # Removendo um amigo
    #usuario.amigos.remover_amigo("Jogador1")
    
    # Listando amigos após a remoção
    #print("\n=== Lista de amigos após remoção ===")
    #usuario.amigos.listar_amigos()

if __name__ == "__main__":
    simulacao()
