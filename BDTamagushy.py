import Tamagushy
import sqlite3

dados = None
cursor = None

def conectarBD():
    global dados
    dados = sqlite3.connect("dados.db")

    global cursor

    cursor = dados.cursor()



def tabela_existe(tabela):
    global cursor
    cursor.execute("""
    SELECT name FROM sqlite_master WHERE 
    type='table'
    """)
    
    for linha in cursor.fetchall():
        if(linha[0] == tabela):
            return True

    return False

def criarBD():
    cursor.execute("""
    CREATE TABLE dados(
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    fome INTEGER NOT NULL,
    saude INTERGER NOT NULL
);
""")

def ler_todos_clientes():
    global cursor
    sql = 'SELECT * FROM dados'
    r = cursor.execute(sql)
    return r.fetchall()

def adicionarInformacoes(nome,idade,fome,saude):
    cursor.execute("""
        INSERT INTO dados(nome,idade,fome,saude)
        VALUES (?,?,?,?)
    """, (nome,idade,fome,saude))

    dados.commit()
    print()
    print("Dados inseridos no banco de dados.")
    print()
