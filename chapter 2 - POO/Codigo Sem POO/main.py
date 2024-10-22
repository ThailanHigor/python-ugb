from steam_library import adicionar_jogo, listar_jogos, verificar_promocoes
from store import listar_jogos_promocao, comprar_jogo

def main():
  print("Bem-vindo à biblioteca STEAM!\n")
  listar_jogos()

  adicionar_jogo("Counter-Strike 2")
  adicionar_jogo("Valorant")

  # Lista jogos na biblioteca
  listar_jogos()

  verificar_promocoes()

  listar_jogos_promocao()

  comprar_jogo("Stardew Valley")
  comprar_jogo("Forza")

if __name__ == "__main__":
    main()
