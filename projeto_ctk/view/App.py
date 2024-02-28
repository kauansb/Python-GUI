import customtkinter as ctk
import tkinter as tk
from Crud import Crud

class Application():
    def __init__(self, app):
        self.app = app
        app.title("Python GUI")
        app.geometry("650x400")
        self.create_widgets()
        self.crud = Crud()  # Instancie a classe Crud

        self.carregar_lista_alunos()

    def create_widgets(self):

        # Frame principal
        main_frame = ctk.CTkFrame(self.app)
        main_frame.pack(expand=True, fill='both', padx=10, pady=10)

        # Título
        title_frame = ctk.CTkFrame(main_frame, height=50)
        title_frame.pack(fill='x', padx=10, pady=(0, 10))
        ctk.CTkLabel(title_frame, text="Cadastro de Aluno", font=('verdana', 20)).pack(padx=10, pady=5)

        # Frame para informações do aluno
        info_frame = ctk.CTkFrame(main_frame)
        info_frame.pack(anchor='n', side='left', padx=10, pady=5)

        ctk.CTkLabel(info_frame, text="Nome:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.nome_entry = ctk.CTkEntry(info_frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=2)

        ctk.CTkLabel(info_frame, text="Gênero:").grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.radio_var = tk.IntVar(value=0)
        ctk.CTkRadioButton(info_frame, text="Masculino", variable=self.radio_var, value=1).grid(row=1, column=1, padx=2, pady=2, sticky="w")
        ctk.CTkRadioButton(info_frame, text="Feminino", variable=self.radio_var, value=2).grid(row=2, column=1, padx=2, pady=2, sticky="w")

        ctk.CTkLabel(info_frame, text="Curso de Tecnologia:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.curso_combobox = ctk.CTkComboBox(info_frame, values=["Python", "JavaScript", "Java", "PHP"])
        self.curso_combobox.grid(row=3, column=1, padx=5, pady=2)

        ctk.CTkLabel(info_frame, text="E-mail:").grid(row=4, column=0, padx=5, pady=2, sticky="e")
        self.email_entry = ctk.CTkEntry(info_frame)
        self.email_entry.grid(row=4, column=1, padx=5, pady=2)

        # Botão de adicionar aluno
        crud_frame = ctk.CTkFrame(main_frame)
        crud_frame.pack(anchor='n', side='left', padx=10, pady=10)
        ctk.CTkButton(crud_frame, text="Adicionar", command=self.adicionar_aluno).pack(padx=5, pady=2)

        # Lista de Alunos
        list_frame = ctk.CTkFrame(main_frame)
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.lista_alunos = ctk.CTkTextbox(list_frame, width=540, height=200)
        self.lista_alunos.pack(fill='both', expand=True)

    def adicionar_aluno(self):
        # Obtenha os valores dos campos da GUI
        nome = self.nome_entry.get()
        sexo = "M" if self.radio_var.get() == 1 else "F"
        curso = self.curso_combobox.get()
        email = self.email_entry.get()

        # Chame o método inserir_aluno da classe Crud
        self.crud.inserir_aluno(nome, sexo, email)

        # Obtenha o ID do curso selecionado
        curso_id = self.obter_id_curso(curso)

        # Insira a matrícula do aluno no curso
        if curso_id:
            aluno_id = self.crud.obter_ultimo_id_aluno()  # Obtém o ID do último aluno inserido
            self.crud.inserir_matricula(aluno_id, curso_id)

        # Limpe os campos após a inserção bem-sucedida
        self.nome_entry.delete(0, tk.END)
        self.radio_var.set(0)
        self.curso_combobox.set("")
        self.email_entry.delete(0, tk.END)
        self.carregar_lista_alunos()

    def obter_id_curso(self, nome_curso):
        cursos = self.crud.selecionar_cursos()
        for curso in cursos:
            if curso['nome_curso'] == nome_curso:
                return curso['id']
        return None
    
    def carregar_lista_alunos(self):

        # Limpe o conteúdo da caixa de texto
        self.lista_alunos.delete(1.0, tk.END)

        # Obtenha a lista de alunos da classe Crud
        alunos = self.crud.selecionar_alunos_com_cursos()

        # Adicione os alunos à lista
        for aluno in alunos:
            # Concatene as informações do aluno para adicionar à lista
            info_aluno = f"ID:  {aluno['id']}   Nome:   {aluno['nome']}  Curso:  {aluno['nome_curso']}   Email:  {aluno['email']}\n"
            self.lista_alunos.insert(tk.END, info_aluno)