from Banco import Banco
class Crud:
    def __init__(self):
        self.banco = Banco()
        self.banco.conectar()

    def inserir_aluno(self, nome, sexo, email):
        query = "INSERT INTO aluno (nome, sexo, email) VALUES (%s, %s, %s)"
        params = (nome, sexo, email)
        self.banco.executar_insert(query, params)

    def inserir_matricula(self, aluno_id, curso_id):
        query = "INSERT INTO matricula (aluno_id, curso_id) VALUES (%s, %s)"
        params = (aluno_id, curso_id)
        self.banco.executar_insert(query, params)

    def selecionar_cursos(self):
        query = "SELECT * FROM cursos"
        return self.banco.executar_select(query)
    
    def selecionar_alunos_com_cursos(self):
        query = """
        SELECT matricula.id, aluno.nome, aluno.email, cursos.nome_curso
        FROM aluno
        LEFT JOIN matricula ON aluno.id = matricula.aluno_id
        LEFT JOIN cursos ON matricula.curso_id = cursos.id
        """
        return self.banco.executar_select(query)

    def obter_ultimo_id_aluno(self):
        query = "SELECT LAST_INSERT_ID() AS last_id"
        result = self.banco.executar_select(query)
        if result:
            return result[0]['last_id']
        else:
            return None
