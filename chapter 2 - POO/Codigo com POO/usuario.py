from biblioteca import BibliotecaSteam
from amigo import ListaDeAmigos

class UsuarioPadrao:
  def __init__(self, nome, status="offline"):
    self.nome = nome
    self.status = status
    self.biblioteca = BibliotecaSteam() # Composição
    self.amigos = ListaDeAmigos() # Composição
      
  def alterar_status(self, novo_status):
    self.status = novo_status
      
  def mostrar_info(self):
    print(f"Usuário: {self.nome}, Status: {self.status}")
    


class Usuario(UsuarioPadrao):
    """Classe base para um usuário da Steam"""
    
    def mostrar_info(self):
        """Exibe informações do usuário"""
        print(f"Usuário: {self.nome}, Status: {self.status}")


class Amigo(Usuario):
    """Classe que representa um amigo na Steam, herdando de Usuario"""
    
    def __init__(self, nome, status="offline"):
        super().__init__(nome, status) 

