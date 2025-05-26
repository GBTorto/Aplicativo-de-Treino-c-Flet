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
    cursor.execute("SELECT email FROM cadastro_pessoas WHERE email=?", (email,))
    if cursor.fetchone() is not None:
        return False, ("Email já cadastrado!")
    else:
        cursor.execute(
            "INSERT INTO cadastro_pessoas (email, Nome, senha) VALUES (?, ?, ?)",
            (email, nome, senha)
        )

        banco.commit()
        banco.close()
        return True

def verificar_usuario(email, senha):
    usuarios = sqlite3.connect("../banco_de_dados.db")
    cursor = usuarios.cursor()

    verificacao = "SELECT * FROM cadastro_pessoas WHERE email=? and senha=?"
    cursor.execute(verificacao, (email, senha))

    resultado = cursor.fetchone()

    usuarios.close()

    if resultado:
        id_usuario = resultado[0]
        print(id_usuario)
        return id_usuario
    else:
        print("usuario incorreto")
        return None

def banco_dados_exercicios(id_chave_estrageira, categoria, exercicio, gif, instrucoes):
    banco = sqlite3.connect("../banco_de_dados.db")
    cursor = banco.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""CREATE TABLE IF NOT EXISTS cadastro_exercicios(
                    ID_Cadastro_Exercicio INTEGER PRIMARY KEY AUTOINCREMENT, 
                    ID_Usuario INTEGER, 
                    categoria,
                    exercicio,
                    gif,
                    instrucoes, 
                    FOREIGN KEY (ID_Usuario) REFERENCES cadastro_pessoas(ID)
                )""")
    
    cursor.execute(
        "INSERT INTO cadastro_exercicios (ID_Usuario, categoria, exercicio, gif, instrucoes) VALUES (?, ?, ?, ?, ?)",
        (id_chave_estrageira, categoria, exercicio, gif, instrucoes)
    )

    banco.commit()
    banco.close()

def exercicios_usuarios(categoria, id_chave_estrangeira):
    banco = sqlite3.connect("../banco_de_dados.db")
    cursor = banco.cursor()

    cursor.execute("""
                    SELECT * FROM cadastro_exercicios WHERE categoria = ? AND ID_Usuario = ?
                """, (categoria, id_chave_estrangeira))
    resultado = cursor.fetchall()
    
    banco.close

    return resultado

# try:
#     # Tenta conectar ao banco de dados
#     banco = sqlite3.connect("../banco_de_dados.db")
#     cursor = banco.cursor()
    
#     # Executa a consulta
#     # cursor.execute("DELETE FROM cadastro_pessoas WHERE ID > 2")
#     cursor.execute("SELECT * FROM cadastro_exercicios")
#     # cursor.execute("DROP TABLE cadastro_exercicios")
    
#     # Recupera os resultados
#     resultados = cursor.fetchall()

#     # banco.commit()
    
#     # Exibe os resultados
#     for linha in resultados:
#         print(linha)
        
# except sqlite3.Error as erro:
#     print(f"Erro ao acessar o banco de dados: {erro}")
    
# finally:
#     # Fecha a conexão
#     if 'banco' in locals():
#         banco.close()
