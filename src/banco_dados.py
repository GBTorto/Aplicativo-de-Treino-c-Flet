import sqlite3

def banco_dados_usuarios(email, nome, senha):
    # Conecta ao banco de dados dentro da função
    banco = sqlite3.connect("../banco_de_dados.db")
    cursor = banco.cursor()

    # Cria a tabela se não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cadastro_pessoas (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        Nome TEXT,
        senha TEXT
    )
    """)

    # Inserção segura usando parâmetros (evita SQL injection)
    cursor.execute(
        "INSERT INTO cadastro_pessoas (email, Nome, senha) VALUES (?, ?, ?)",
        (email, nome, senha)
    )

    banco.commit()
    banco.close()
