import customtkinter as ctk 
import tkinter as tk  
from CR_Ope import CR_Ope as cr  

class Application():
    def __init__(self, app):
        self.app = app  # Define a janela principal da aplicação
        app.title("Python GUI")  # Define o título da janela principal
        self.create_widgets()  # Chama o método para criar os widgets da interface gráfica
        self.cr = cr()  # Instâcia da classe CR_Ope para realizar operações CRUD no banco de dados
        self.carregar_lista_alunos()  # Carrega a lista de alunos na interface gráfica

    # Método para criar os widgets da interface gráfica
    def create_widgets(self):
        # Cria um frame principal para organizar os widgets
        main_frame = ctk.CTkFrame(self.app)
        main_frame.pack(expand=True, fill='both', padx=10, pady=10)

        # Cria um frame para o título da aplicação
        title_frame = ctk.CTkFrame(main_frame, height=50)
        title_frame.pack(fill='x', padx=10, pady=(0, 10))
        ctk.CTkLabel(title_frame, text="Cadastro de Aluno", font=('verdana', 20)).pack(padx=10, pady=5)

        # Cria um frame para informações do aluno
        info_frame = ctk.CTkFrame(main_frame)
        info_frame.pack(anchor='n', side='left', padx=10, pady=5)

        # Cria labels e entradas para os campos de nome, gênero, curso e e-mail
        labels = ["Nome:", "Gênero:", "Curso de Tecnologia:", "E-mail:"]
        self.entries = {}
        for i, label_text in enumerate(labels):
            ctk.CTkLabel(info_frame, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky="e")
            if label_text == "Gênero:":
                self.radio_var = tk.IntVar(value=0)
                ctk.CTkRadioButton(info_frame, text="Masculino", variable=self.radio_var, value=1).grid(row=i, column=1, padx=0, pady=2, sticky="w")
                ctk.CTkRadioButton(info_frame, text="Feminino", variable=self.radio_var, value=2).grid(row=i, column=2, padx=0, pady=2, sticky="e")
            elif label_text == "Curso de Tecnologia:":
                ctk.CTkLabel(info_frame, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky="e")
                self.curso_combobox = ctk.CTkComboBox(info_frame, values=["Python", "JavaScript", "Java", "PHP", "Análise de dados"])
                self.curso_combobox.grid(row=i, column=1, padx=5, pady=5, columnspan=2, sticky="w")
            else:
                self.entries[label_text] = ctk.CTkEntry(info_frame)
                self.entries[label_text].grid(row=i, column=1, padx=5, pady=5, sticky="w")

        # Cria um frame para botão de adicionar aluno
        crud_frame = ctk.CTkFrame(main_frame)
        crud_frame.pack(anchor='n', side='left', padx=10, pady=10)
        ctk.CTkButton(crud_frame, text="Adicionar", command=self.adicionar_aluno).pack(padx=5, pady=2)

        # Cria um frame para exibir a lista de alunos
        list_frame = ctk.CTkFrame(main_frame)
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)
        self.lista_alunos = ctk.CTkTextbox(list_frame, width=540, height=200)
        self.lista_alunos.pack(fill='both', expand=True)

    # Método para adicionar um novo aluno
    def adicionar_aluno(self):
        # Obtém os valores dos campos de entrada
        nome = self.entries["Nome:"].get()
        sexo = "M" if self.radio_var.get() == 1 else "F"
        curso = self.curso_combobox.get()
        email = self.entries["E-mail:"].get()

        # Insere o aluno no banco de dados
        self.cr.inserir_aluno(nome, sexo, email)
        curso_id = self.obter_id_curso(curso)

        if curso_id:
            aluno_id = self.cr.obter_ultimo_id_aluno()
            self.cr.inserir_matricula(aluno_id, curso_id)

            for entry in self.entries.values():
                entry.delete(0, tk.END)
            self.curso_combobox.set("")

            tk.messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso!")

            # Carrega a lista de alunos após a inserção bem-sucedida
            self.carregar_lista_alunos()
        else:
            tk.messagebox.showinfo("Erro", "Falha ao realizar matrícula")

    # Método para obter o ID do curso a partir do nome do curso
    def obter_id_curso(self, nome_curso):
        cursos = self.cr.selecionar_cursos()
        for curso in cursos:
            if curso['nome_curso'] == nome_curso:
                return curso['id']
        return None
    
    # Método para carregar a lista de alunos na interface gráfica
    def carregar_lista_alunos(self):
        self.lista_alunos.configure(state="normal")  # Habilita edição temporariamente
        self.lista_alunos.delete("0.0", tk.END)  # Limpa o texto na área de texto
        alunos = self.cr.selecionar_alunos_com_cursos()  # Seleciona todos os alunos com cursos do banco de dados
        for aluno in alunos:
            # Formata as informações do aluno e adiciona na área de texto
            info_aluno = f"ID:  {aluno['id']}   Nome:   {aluno['nome']}  Curso:  {aluno['nome_curso']}   Email:  {aluno['email']}\n"
            self.lista_alunos.insert(tk.END, info_aluno)
        self.lista_alunos.configure(state="disabled")  # Desabilita edição novamente
