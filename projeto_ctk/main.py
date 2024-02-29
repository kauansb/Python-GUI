import customtkinter as ctk
from view.App import Application
from view.AppCrud import Application2

if __name__ == '__main__':
    root = ctk.CTk()
    #app = Application(root)
    app2 = Application2(root)
    root.mainloop()
