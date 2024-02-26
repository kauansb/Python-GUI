import mysql.connector

class Banco:
    def __init__(self):
        # Configurações do banco de dados
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.database = 'projeto_python'
        self.connection = None

    # Método para conectar ao banco de dados
    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexão estabelecida com sucesso!")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
    
    def executar_insert(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            last_row_id = cursor.lastrowid  # Obtém o ID da última linha inserida
            cursor.close()
            return last_row_id
        except mysql.connector.Error as e:
            print(f"Erro ao executar consulta: {e}")

    def executar_select(self, query, params=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as e:
            print(f"Erro ao executar consulta: {e}")

    def executar_update_delete(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            cursor.close()
        except mysql.connector.Error as e:
            print(f"Erro ao executar consulta: {e}")