import customtkinter as ctk
from view.App import Application

if __name__ == '__main__':
    # Cria uma instância da classe CTk() para criar uma janela principal
    root = ctk.CTk()
    
    # Cria uma instância da classe Application passando a janela principal como argumento
    app = Application(root)
    
    # Inicia o loop principal da aplicação, onde a interface gráfica será atualizada e responderá a eventos
    root.mainloop()
