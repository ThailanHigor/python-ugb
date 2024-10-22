# Lista para armazenar jogos em promoção
jogos_promocao = ["Red Dead Redemption", "Sea of Thieves", "Forza"]

def listar_jogos_promocao():
    """Lista os jogos em promoção."""

    print("Jogos em promoção:")
    for jogo in jogos_promocao:
        print(f"- {jogo}")

def comprar_jogo(nome_jogo):
  """Simula a compra de um jogo."""

  if nome_jogo in jogos_promocao:  
    print(f"Você comprou '{nome_jogo}'!\n")
  else:
    print(f"Jogo não encontrado!\n")
