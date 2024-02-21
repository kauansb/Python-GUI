from db_connection import Banco

class Crud:
    def __init__(self):
        self.banco = Banco()
        self.banco.conectar()  # Conectar ao banco de dados ao criar a instância da classe Crud

    def adicionar_contato(self, nome, telefone):
        query = "INSERT INTO Contato (nome, telefone) VALUES (%s, %s)"
        params = (nome, telefone)
        self.banco.executar_consulta(query, params)

    def atualizar_contato(self, id_contato, nome, telefone):
        query = "UPDATE Contato SET nome = %s, telefone = %s WHERE id = %s"
        params = (nome, telefone, id_contato)
        self.banco.executar_consulta(query, params)

    def excluir_contato(self, id_contato):
        query = "DELETE FROM Contato WHERE id = %s"
        params = (id_contato,)
        self.banco.executar_consulta(query, params)

    def fechar_conexao(self):
        self.banco.desconectar()  # Método para fechar a conexão com o banco de dados
