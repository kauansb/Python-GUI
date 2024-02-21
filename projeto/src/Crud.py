from db_connection import executar_consulta

# Operações CREATE, UPDATE E DELETE
class Crud:
    @staticmethod
    def adicionar_contato(nome, telefone):
        query = "INSERT INTO Contato (nome, telefone) VALUES (%s, %s)" 
        params = (nome, telefone)
        executar_consulta(query, params)

    @staticmethod
    def atualizar_contato(id_contato, nome, telefone):
        query = "UPDATE Contato SET nome = %s, telefone = %s WHERE id = %s"
        params = (nome, telefone, id_contato)
        executar_consulta(query, params)

    @staticmethod
    def excluir_contato(id_contato):
        query = "DELETE FROM Contato WHERE id = %s"
        params = (id_contato,)
        executar_consulta(query, params)
