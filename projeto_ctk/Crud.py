from Banco import Banco

class Crud:
    def __init__(self):
        self.banco = Banco()
        self.banco.conectar()

    def inserir_aluno(self, nome, sexo, email):
        query = "INSERT INTO aluno (nome, sexo, email) VALUES (%s, %s, %s)"
        params = (nome, sexo, email)
        self.banco.executar_insert(query, params)

    def inserir_curso(self, nome_curso):
        query = "INSERT INTO cursos (nome_curso) VALUES (%s)"
        params = (nome_curso,)
        self.banco.executar_insert(query, params)

    def inserir_matricula(self, aluno_id, curso_id):
        query = "INSERT INTO matricula (aluno_id, curso_id) VALUES (%s, %s)"
        params = (aluno_id, curso_id)
        self.banco.executar_insert(query, params)

    def selecionar_alunos(self):
        query = "SELECT * FROM aluno"
        return self.banco.executar_select(query)

    def selecionar_cursos(self):
        query = "SELECT * FROM cursos"
        return self.banco.executar_select(query)

    def selecionar_matriculas(self):
        query = "SELECT * FROM matricula"
        return self.banco.executar_select(query)

    def excluir_aluno(self, aluno_id):
        query = "DELETE FROM aluno WHERE id = %s"
        params = (aluno_id,)
        self.banco.executar_update_delete(query, params)

    def excluir_curso(self, curso_id):
        query = "DELETE FROM cursos WHERE id = %s"
        params = (curso_id,)
        self.banco.executar_update_delete(query, params)

    def excluir_matricula(self, matricula_id):
        query = "DELETE FROM matricula WHERE id = %s"
        params = (matricula_id,)
        self.banco.executar_update_delete(query, params)
    
    def editar_aluno(self, aluno_id, novo_nome, novo_sexo, novo_email, novo_curso):
        try:
            # Execute a consulta SQL para editar o aluno com os novos valores
            query = "UPDATE aluno SET nome = %s, sexo = %s, email = %s WHERE id = %s"
            params = (novo_nome, novo_sexo, novo_email, aluno_id)
            self.executar_consulta(query, params)
            print("Aluno editado com sucesso!")
        except Exception as e:
            print(f"Erro ao editar aluno: {e}")

    # Implemente o método para obter o último ID de aluno inserido
    def obter_ultimo_id_aluno(self):
        query = "SELECT LAST_INSERT_ID() AS last_id"
        result = self.banco.executar_select(query)
        if result:
            return result[0]['last_id']
        else:
            return None