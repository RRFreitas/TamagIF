import sqlite3

dados = None
cursor = None

#Conectando, iniciando Banco de Dados
def conectarBD():
    global dados
    dados = sqlite3.connect("dados.db")

    global cursor

    cursor = dados.cursor()


#Verificando se existe alguma tabela    
def tabela_existe(tabela):
    global cursor
    cursor.execute("""
    SELECT name FROM sqlite_master WHERE 
    type='table'
    """)

    for linha in cursor.fetchall():
        if (linha[0] == tabela):
            return True

    return False

#Criando Tabela
def criarBD():
    cursor.execute("""
    CREATE TABLE dados(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    fome INTEGER NOT NULL,
    saude INTEGER NOT NULL,
    r INTEGER NOT NULL,
    g INTEGER NOT NULL,
    b INTEGER NOT NULL,
    recordJG1 INTEGER NOT NULL,
    recordJG2 INTEGER NOT NULL,
    comidas INTEGER NOR NULL
);
""")

#LEndo tabela
def ler_todos_clientes():
    global cursor
    sql = 'SELECT * FROM dados'
    r = cursor.execute(sql)

    return r.fetchall()

#Adicionando informacoes
def adicionarInformacoes(nome, idade, fome, saude,r,g,b,recordJG1,recordJG2,comidas):
    cursor.execute("""
        INSERT INTO dados(id,nome,idade,fome,saude,r,g,b,recordJG1,recordJG2,comidas)
        VALUES (NULL,?,?,?,?,?,?,?,?,?,?)
    """, (nome, idade, fome, saude,r,g,b,recordJG1,recordJG2,comidas))

    dados.commit()
    print()
    print("Dados inseridos no banco de dados.")
    print()

#atualizando os dados
def atualizarDados (nome,idade,fome,saude,r,g,b,recordJG1,recordJG2,comidas):
    cursor.execute("""
    UPDATE dados 
    SET nome = ?,idade = ? , fome = ? , saude = ? , r = ? , g = ? , b = ? , recordJG1 = ? , recordJG2 = ? , comidas = ?
""",(nome,idade,fome,saude,r,g,b,recordJG1,recordJG2,comidas))

    dados.commit()

#DEletar bnco de dados
def deletarDados ():
    cursor.execute("""
    DROP TABLE dados
;
""")
