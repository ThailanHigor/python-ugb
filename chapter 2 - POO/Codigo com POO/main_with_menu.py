# main_simulacao.py

from biblioteca import BibliotecaSteam
from loja import LojaSteam
from amigo import Amigo
from usuario import UsuarioPadrao
from amigo import ListaDeAmigos

def exibir_menu():
    print("\n=== Menu Principal ===")
    print("1. Ver jogos disponíveis na loja")
    print("2. Comprar um jogo")
    print("3. Ver jogos na biblioteca")
    print("4. Remover um jogo da biblioteca")
    print("5. Verificar promoções")
    print("6. Adicionar um amigo")
    print("7. Ver lista de amigos")
    print("8. Remover um amigo")
    print("9. Sair")

def simulacao():
    """Função de simulação das funcionalidades da Steam."""
    
    # Criando uma biblioteca Steam e uma lista de amigos
    biblioteca = BibliotecaSteam()
    lista_amigos = ListaDeAmigos()
    
    # Criando a loja Steam
    loja = LojaSteam()

    # Criando o usuário padrão logado
    nome_usuario = input("Digite o nome do seu usuário Steam: ")
    usuario = UsuarioPadrao(nome_usuario, "online")
    usuario.mostrar_info()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Exibindo os jogos disponíveis na loja
            print("\n=== Jogos disponíveis na loja Steam ===")
            loja.listar_jogos_loja()

        elif opcao == "2":
            # Simulando a compra de um jogo
            print("\n=== Comprar um jogo ===")
            jogo = input("Digite o nome do jogo que deseja comprar: ")
            usuario.comprar_jogo(jogo, biblioteca)

        elif opcao == "3":
            # Listando os jogos na biblioteca
            print("\n=== Sua biblioteca ===")
            biblioteca.listar_jogos()

        elif opcao == "4":
            # Removendo um jogo da biblioteca
            print("\n=== Remover um jogo da biblioteca ===")
            jogo = input("Digite o nome do jogo que deseja remover: ")
            biblioteca.remover_jogo(jogo)

        elif opcao == "5":
            # Verificando promoções
            biblioteca.verificar_promocoes()

        elif opcao == "6":
            # Adicionando um amigo
            print("\n=== Adicionar um amigo ===")
            nome_amigo = input("Digite o nome do seu amigo: ")
            amigo = Amigo(nome_amigo, "online")
            usuario.adicionar_amigo(amigo, lista_amigos)

        elif opcao == "7":
            # Listando amigos
            print("\n=== Lista de amigos ===")
            lista_amigos.listar_amigos()

        elif opcao == "8":
            # Removendo um amigo
            print("\n=== Remover um amigo ===")
            nome_amigo = input("Digite o nome do amigo que deseja remover: ")
            lista_amigos.remover_amigo(nome_amigo)

        elif opcao == "9":
            # Sair do programa
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    simulacao()
