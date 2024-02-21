from db_connection import Banco
from models.Contato import Contato

class Crud:
    def __init__(self):
        self.banco = Banco()
        self.banco.conectar()

    def adicionar_contato(self, nome, telefone):
        # Crie uma instância de Contato com os dados fornecidos
        novo_contato = Contato(nome, telefone)
        
        # Use os atributos do contato para inserir no banco de dados
        query = "INSERT INTO Contato (nome, telefone) VALUES (%s, %s)"
        params = (novo_contato.nome, novo_contato.telefone)
        self.banco.executar_consulta(query, params)

    def atualizar_contato(self, id_contato, nome, telefone):
        # Crie uma instância de Contato com os novos dados
        contato_atualizado = Contato(nome, telefone)
        
        # Use os atributos do contato atualizado para atualizar o registro no banco de dados
        query = "UPDATE Contato SET nome = %s, telefone = %s WHERE id = %s"
        params = (contato_atualizado.nome, contato_atualizado.telefone, id_contato)
        self.banco.executar_consulta(query, params)

    def excluir_contato(self, id_contato):
        # Não precisamos criar uma instância de Contato para excluir, apenas usar o ID
        query = "DELETE FROM Contato WHERE id = %s"
        params = (id_contato,)
        self.banco.executar_consulta(query, params)

    def fechar_conexao(self):
        self.banco.desconectar()
