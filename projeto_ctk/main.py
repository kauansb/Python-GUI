import customtkinter as ctk  # Importa a biblioteca CustomTkinter com o alias ctk
from view.App import Application  # Importa a classe Application do módulo view/App

if __name__ == '__main__':
    # Cria uma instância da classe CTk() para criar uma janela principal
    root = ctk.CTk()
    
    # Cria uma instância da classe Application passando a janela principal como argumento
    app = Application(root)
    
    # Inicia o loop principal da aplicação, onde a interface gráfica será atualizada e responderá a eventos
    root.mainloop()
