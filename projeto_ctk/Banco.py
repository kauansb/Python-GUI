import mysql.connector

class Banco:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.database = 'projeto_python'
        self.connection = None

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
    
    # Método para executar uma operação de inserção no banco de dados
    def executar_insert(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            if params:
                # Se houver parâmetros, executa a consulta com os parâmetros
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()  # Confirma as alterações no banco de dados
            last_row_id = cursor.lastrowid  # Obtém o ID da última linha inserida
            cursor.close()
            return last_row_id  # Retorna o ID da última linha inserida
        except mysql.connector.Error as e:
            # Em caso de erro ao executar a consulta, imprime uma mensagem de erro
            print(f"Erro ao executar consulta: {e}")

    # Método para executar uma operação de seleção no banco de dados
    def executar_select(self, query, params=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()  # Obtém todos os resultados da consulta
            cursor.close()
            return result
        except mysql.connector.Error as e:
            print(f"Erro ao executar consulta: {e}")
