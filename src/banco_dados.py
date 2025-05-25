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

    cursor.execute("SELECT * FROM cadastro_pessoas")


    banco.commit()
    banco.close()

def verificar_usuario(email, senha):
    usuarios = sqlite3.connect("../banco_de_dados.db")
    cursor = usuarios.cursor()

    verificacao = f"SELECT * FROM cadastro_pessoas WHERE email=? and senha=?"
    cursor.execute(verificacao, (email, senha))

    resultado = cursor.fetchone()

    usuarios.close()

    return resultado is not None