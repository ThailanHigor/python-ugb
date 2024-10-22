biblioteca_jogos = []

def adicionar_jogo(nome_jogo):
  """Adiciona um jogo à biblioteca."""

  biblioteca_jogos.append(nome_jogo)
  print(f"Jogo '{nome_jogo}' adicionado à biblioteca.\n")

def listar_jogos():
  """Lista todos os jogos na biblioteca."""

  if not biblioteca_jogos:
      print("Sua biblioteca está vazia.\n")
  else:
      print("Jogos na sua biblioteca:")
      for jogo in biblioteca_jogos:
          print(f"- {jogo}")

def verificar_promocoes():
  """Simula a verificação de promoções."""

  print("Verificando promoções...")
  print("Promoção! 50% de desconto em jogos selecionados!\n")
