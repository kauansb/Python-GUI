from Banco import Banco

class CR_Ope:
    def __init__(self):
        self.banco = Banco()  # Cria uma instância da classe Banco
        self.banco.conectar()  # Conecta ao banco de dados

    def inserir_aluno(self, nome, sexo, email):
        query = "INSERT INTO aluno (nome, sexo, email) VALUES (%s, %s, %s)"  # Query SQL para inserção de aluno
        params = (nome, sexo, email)  # Parâmetros da consulta
        self.banco.executar_insert(query, params)  # Executa a consulta de inserção

    def inserir_matricula(self, aluno_id, curso_id):
        query = "INSERT INTO matricula (aluno_id, curso_id) VALUES (%s, %s)"
        params = (aluno_id, curso_id)  
        self.banco.executar_insert(query, params)  

    def selecionar_cursos(self):
        query = "SELECT * FROM cursos"
        return self.banco.executar_select(query)  

    def selecionar_alunos_com_cursos(self):
        query = """ 
        SELECT matricula.id, aluno.nome, aluno.sexo, aluno.email, cursos.nome_curso, COUNT(matricula.id) as total_mat
        FROM aluno
        LEFT JOIN matricula ON aluno.id = matricula.aluno_id
        LEFT JOIN cursos ON matricula.curso_id = cursos.id
        """  # Query SQL para seleção de alunos matriculados
        return self.banco.executar_select(query) 

    def obter_ultimo_id_aluno(self):
        query = "SELECT LAST_INSERT_ID() AS last_id"  # Query SQL para obter o último ID inserido
        result = self.banco.executar_select(query) 
        if result:
            return result[0]['last_id']  # Retorna o último ID inserido
        else:
            return None  # Retorna None se não houver resultado
