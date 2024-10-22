
import sqlite3

class BancoDeDadosJogos:
    def __init__(self, caminho_do_banco="loja_steam.db"):
        self.conexao = sqlite3.connect(caminho_do_banco)
        self.cursor = self.conexao.cursor()
    
    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS jogos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL NOT NULL  -- Removemos a coluna 'ano_lancamento'
            )
        ''')
        self.conexao.commit()
    
    def adicionar_jogo(self, nome, categoria, preco):
        self.cursor.execute('''
            INSERT INTO jogos (nome, categoria, preco)
            VALUES (?, ?, ?)
        ''', (nome, categoria, preco))
        self.conexao.commit()
    
    def listar_jogos(self):
        self.cursor.execute('SELECT * FROM jogos')
        return self.cursor.fetchall()
    
    def buscar_jogo(self, nome):
        self.cursor.execute('SELECT * FROM jogos WHERE nome = ?', (nome,))
        return self.cursor.fetchone()
    
    def fechar_conexao(self):
        self.conexao.close()

# Exemplo de uso da classe
if __name__ == "__main__":
    db = BancoDeDadosJogos()
    db.criar_tabela()
    
    # Adicionando alguns jogos
    db.adicionar_jogo("Counter-Strike 2", "FPS", 59.0)
    db.adicionar_jogo("The Legend of Zelda: Tears of the Kingdom", "Aventura", 60)

    # Listando jogos
    print("Jogos no banco:")
    for jogo in db.listar_jogos():
        print(jogo)

    # Atualizando um jogo
    #db.atualizar_jogo(1, "Counter-Strike 2", "Tiro em Primeira Pessoa", 80)

    # Removendo um jogo
    #db.remover_jogo(2)

    # Listando jogos após a atualização e remoção
   # print("\nJogos após atualização e remoção:")
    #for jogo in db.listar_jogos():
    #    print(jogo)

    # Fechando a conexão
    db.fechar_conexao()
