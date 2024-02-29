drop database if exists projeto_python;
create database projeto_python;
use projeto_python;

CREATE TABLE aluno (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    sexo char(1),
    email VARCHAR(55)
);

CREATE TABLE cursos(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_curso VARCHAR(50) NOT NULL
)

CREATE TABLE matricula (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT,
    curso_id INT,
    data_matricula DATETIME DEFAULT CURRENT_TIMESTAMP, 
    FOREIGN KEY (aluno_id) REFERENCES aluno(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO cursos(nome_curso) VALUES('Python'),('JavaScript'),('Java'),('PHP'),('Análise de dados');