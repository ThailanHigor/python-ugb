class ListaDeAmigos:
  """Gerencia a lista de amigos do usuário."""

  def __init__(self):
      self.amigos = []

  def adicionar_amigo(self, amigo):
      """Adiciona um amigo à lista."""

      if amigo not in self.amigos:
          self.amigos.append(amigo)
          print(f"Amigo '{amigo.nome}' adicionado.\n")
      else:
          print(f"Amigo '{amigo.nome}' já está na lista.\n")

  def remover_amigo(self, nome_amigo):
      """Remove um amigo da lista."""

      for amigo in self.amigos:
          if amigo.nome == nome_amigo:
              self.amigos.remove(amigo)
              print(f"Amigo '{nome_amigo}' removido.\n")
              return
      print(f"Amigo '{nome_amigo}' não está na lista.\n")

  def listar_amigos(self):
      """Lista todos os amigos."""

      if not self.amigos:
          print("Sua lista de amigos está vazia.\n")
      else:
          print("Seus amigos:")
          for amigo in self.amigos:
              print(f"- {amigo}")
          print()
