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
        # Bloco 1: Informações Principais
        frame = ctk.CTkFrame(self.app, width=200, height=200)
        frame.grid(row=0, column=0, padx=10, pady=5)

        ctk.CTkLabel(frame, text="Nome:").grid(row=0, column=0, padx=0, pady=2, sticky="e")
        self.nome_entry = ctk.CTkEntry(frame)
        self.nome_entry.grid(row=0, column=1, padx=5, pady=2)

        self.radio_var = tk.IntVar(value=0)
        ctk.CTkRadioButton(frame, text="Masculino", variable=self.radio_var, value=1).grid(row=1, column=0, padx=2, pady=1, sticky="e")
        ctk.CTkRadioButton(frame, text="Feminino", variable=self.radio_var, value=2).grid(row=1, column=1, padx=2, pady=1, sticky="e")

        ctk.CTkLabel(frame, text="Curso de Tecnologia:").grid(row=2, column=0, padx=5, pady=2, sticky="e")
        self.curso_combobox = ctk.CTkComboBox(frame, values=["Python", "JavaScript", "Java", "PHP"])
        self.curso_combobox.grid(row=2, column=1, padx=5, pady=2)

        ctk.CTkLabel(frame, text="E-mail:").grid(row=3, column=0, padx=5, pady=2, sticky="e")
        self.email_entry = ctk.CTkEntry(frame)
        self.email_entry.grid(row=3, column=1, padx=5, pady=2)

        # Botões CRUD
        crud_frame = ctk.CTkFrame(self.app)
        crud_frame.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkButton(crud_frame, text="Adicionar", command=self.adicionar_aluno).grid(row=0, column=0, padx=5, pady=2)
        ctk.CTkButton(crud_frame, text="Editar", command=self.editar_aluno).grid(row=1, column=0, padx=5, pady=2)
        ctk.CTkButton(crud_frame, text="Excluir").grid(row=2, column=0, padx=5, pady=2)

        # Bloco 3: Lista de Alunos
        self.lista_alunos = ctk.CTkTextbox(self.app, width=540, height=200) 
        self.lista_alunos.grid(row=3, column=0, columnspan=2, padx=50, pady=5)

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

    def obter_id_curso(self, nome_curso):
        cursos = self.crud.selecionar_cursos()
        for curso in cursos:
            if curso['nome_curso'] == nome_curso:
                return curso['id']
        return None
    
    def carregar_lista_alunos(self):
        if self.lista_alunos is None:  # Verifique se lista_alunos está inicializado
            return

        # Limpe o conteúdo da caixa de texto
        self.lista_alunos.delete(1.0, tk.END)

        # Obtenha a lista de alunos da classe Crud
        alunos = self.crud.selecionar_alunos()

        # Adicione os alunos à lista
        for aluno in alunos:
            self.lista_alunos.insert(tk.END, aluno['nome'] + '\n')  # Adicione '\n' para nova linha


    
    def editar_aluno(self):
        # Obtenha o ID do aluno selecionado na lista
        aluno_id = self.obter_id_aluno_selecionado()

        # Se nenhum aluno estiver selecionado, retorne
        if aluno_id is None:
            return

        # Obtenha os detalhes do aluno selecionado
        aluno_selecionado = self.crud.obter_aluno_por_id(aluno_id)
        if aluno_selecionado:
            # Preencha os campos da GUI com os detalhes do aluno selecionado
            self.nome_entry.delete(0, tk.END)
            self.nome_entry.insert(tk.END, aluno_selecionado['nome'])
            
            if aluno_selecionado['sexo'] == 'M':
                self.radio_var.set(1)
            else:
                self.radio_var.set(2)
            
            # Defina o curso selecionado na caixa de combinação
            self.curso_combobox.set(aluno_selecionado['curso'])
            
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, aluno_selecionado['email'])

            # Agora o usuário pode editar os detalhes e salvar as alterações


    def excluir_aluno(self):
        # Obtenha o ID do aluno selecionado na lista
        aluno_id = self.obter_id_aluno_selecionado()

        # Se nenhum aluno estiver selecionado, retorne
        if aluno_id is None:
            return

        # Chame o método correspondente na classe Crud para excluir o aluno
        self.crud.excluir_aluno(aluno_id)

        # Atualize a lista de alunos na interface gráfica
        self.carregar_lista_alunos()

    def obter_id_aluno_selecionado(self):
        # Obtenha o índice do aluno selecionado na lista
        indice_selecionado = self.lista_alunos.curselection()

        # Se nenhum aluno estiver selecionado, retorne None
        if not indice_selecionado:
            return None

        # Obtenha o ID do aluno selecionado na lista
        aluno_selecionado = self.lista_alunos.get(indice_selecionado[0])
        alunos = self.crud.selecionar_alunos()
        for aluno in alunos:
            if aluno['nome'] == aluno_selecionado:
                return aluno['id']
        return None