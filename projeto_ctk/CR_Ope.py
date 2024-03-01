from Banco import Banco

class CR_Ope:
    def __init__(self):
        self.banco = Banco()  # Cria uma instância da classe Banco
        self.banco.conectar()  # Conecta ao banco de dados

    # Método para inserir um novo aluno no banco de dados
    def inserir_aluno(self, nome, sexo, email):
        query = "INSERT INTO aluno (nome, sexo, email) VALUES (%s, %s, %s)"  # Query SQL para inserção de aluno
        params = (nome, sexo, email)  # Parâmetros da consulta
        self.banco.executar_insert(query, params)  # Executa a consulta de inserção

    # Método para inserir uma nova matrícula no banco de dados
    def inserir_matricula(self, aluno_id, curso_id):
        query = "INSERT INTO matricula (aluno_id, curso_id) VALUES (%s, %s)"  # Query SQL para inserção de matrícula
        params = (aluno_id, curso_id)  # Parâmetros da consulta
        self.banco.executar_insert(query, params)  # Executa a consulta de inserção

    # Método para selecionar todos os cursos do banco de dados
    def selecionar_cursos(self):
        query = "SELECT * FROM cursos"  # Query SQL para seleção de cursos
        return self.banco.executar_select(query)  # Executa a consulta e retorna o resultado

    # Método para selecionar todos os alunos com seus respectivos cursos do banco de dados
    def selecionar_alunos_com_cursos(self):
        query = """
        SELECT matricula.id, aluno.nome, aluno.email, cursos.nome_curso
        FROM aluno
        LEFT JOIN matricula ON aluno.id = matricula.aluno_id
        LEFT JOIN cursos ON matricula.curso_id = cursos.id
        """  # Query SQL para seleção de alunos com cursos
        return self.banco.executar_select(query)  # Executa a consulta e retorna o resultado

    # Método para obter o último ID inserido na tabela de alunos
    def obter_ultimo_id_aluno(self):
        query = "SELECT LAST_INSERT_ID() AS last_id"  # Query SQL para obter o último ID inserido
        result = self.banco.executar_select(query)  # Executa a consulta e obtém o resultado
        if result:
            return result[0]['last_id']  # Retorna o último ID inserido
        else:
            return None  # Retorna None se não houver resultado
