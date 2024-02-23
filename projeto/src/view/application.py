import tkinter as tk
from tkinter import messagebox
from Crud import Crud

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Contatos")
        self.create_widgets()
        self.crud = Crud()

    def create_widgets(self):
        data_frame = tk.Frame(self.master)
        data_frame.grid(row=0, column=1, padx=45, pady=28)

        tk.Label(data_frame, text="ID:").grid(row=0, column=0, padx=5, pady=2, sticky="e")
        self.entry_id = tk.Entry(data_frame)
        self.entry_id.grid(row=0, column=1, padx=5, pady=2)
        
        tk.Label(data_frame, text="Nome:").grid(row=1, column=0, padx=5, pady=2, sticky="e")
        self.entry_nome = tk.Entry(data_frame)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=2)
        
        tk.Label(data_frame, text="Telefone:").grid(row=2, column=0, padx=5, pady=2, sticky="e")
        self.entry_telefone = tk.Entry(data_frame)
        self.entry_telefone.grid(row=2, column=1, padx=5, pady=2)

        button_frame = tk.Frame(self.master)
        button_frame.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(button_frame, text="Adicionar", command=self.adicionar_contato).pack(side="left", padx=5)
        tk.Button(button_frame, text="Atualizar", command=self.atualizar_contato).pack(side="left", padx=5)
        tk.Button(button_frame, text="Excluir", command=self.excluir_contato).pack(side="left", padx=5)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def show_error(self, message):
        messagebox.showerror("Erro", message)

    def clear_entries(self):
        self.entry_id.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)

    def adicionar_contato(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        if nome and telefone:
            self.crud.adicionar_contato(nome, telefone)  # Chamando o método da instância CRUDOperations
            self.show_message("Sucesso", "Contato adicionado com sucesso!")
            self.clear_entries()
        else:
            self.show_error("Por favor, preencha todos os campos.")

    def atualizar_contato(self):
        id_contato = self.entry_id.get()
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        if id_contato and nome and telefone:
            self.crud.atualizar_contato(id_contato, nome, telefone)  # Chamando o método da instância CRUDOperations
            self.show_message("Sucesso", "Contato atualizado com sucesso!")
        else:
            self.show_error("Por favor, preencha todos os campos.")

    def excluir_contato(self):
        id_contato = self.entry_id.get()
        if id_contato:
            self.crud.excluir_contato(id_contato)  # Chamando o método da instância CRUDOperations
            self.show_message("Sucesso", "Contato excluído com sucesso!")
        else:
            self.show_error("Por favor, preencha o ID do contato.")