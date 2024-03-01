import customtkinter as ctk
from view.App import Application

if __name__ == '__main__':
    root = ctk.CTk()
    app = Application(root)
    root.mainloop()
