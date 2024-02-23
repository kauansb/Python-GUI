from view.application import Application
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk() #Cria uma instância principal da janela Tkinter.
    app = Application(root) #Cria uma instância da classe Application, passando a instância principal da janela Tkinter como argumento.
    root.mainloop() #Inicia o loop principal de eventos do Tkinter, permitindo que a janela permaneça aberta e interativa até que seja fechada pelo usuário.
