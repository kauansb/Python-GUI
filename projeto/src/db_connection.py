import mysql.connector

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'projeto_python'
}

# Conexão com o banco de dados
def conectar():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

# Função para executar consultas
def executar_consulta(query, params=None, close_cursor=True):
    connection = conectar()
    if connection:
        try:
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            connection.commit()
            return cursor
        except mysql.connector.Error as e:
            print(f"Erro ao executar consulta: {e}")