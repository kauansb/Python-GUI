class Aluno:
    def __init__(self, id, nome, sexo, email):
        self.id = id
        self.nome = nome
        self.sexo = sexo
        self.email = email

class Curso:
    def __init__(self, id, nome_curso):
        self.id = id
        self.nome_curso = nome_curso

class Matricula:
    def __init__(self, id, aluno_id, curso_id):
        self.id = id
        self.aluno_id = aluno_id
        self.curso_id = curso_id
