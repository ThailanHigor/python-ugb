import csv
from usuario import UsuarioPadrao

def carregar_usuarios_csv(caminho_arquivo):
    usuarios = []
    
    with open(caminho_arquivo, newline='') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv) 
        for linha in leitor:
            nome = linha['nome']
            status = linha['status']
            usuario = UsuarioPadrao(nome, status)
            usuarios.append(usuario)
    
    return usuarios
