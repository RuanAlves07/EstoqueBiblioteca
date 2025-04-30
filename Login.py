import customtkinter as ctk
from tkinter import messagebox
from comunicacao import comunicacao

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class TelaLoginCadastro:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("")
        self.root.state("zoomed")
        self.root.configure(bg="#f6f3ec")
        self.root.resizable(False, False)

        self.JanelaMeio()
        self.root.mainloop()

    def CentralizaçãoDaJanela(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    def JanelaMeio(self):
        JanelaMeio = ctk.CTkToplevel(self.root)
        JanelaMeio.title("Login")
        JanelaMeio.configure(bg="#f6f3ec")
        JanelaMeio.resizable(False, False)

        # Centralizar a nova janela
        self.CentralizaçãoDaJanela(JanelaMeio, 400, 300)

        # Ficar sempre em cima e focado
        JanelaMeio.grab_set()
        JanelaMeio.focus_force()

        # Widgets
        self.BemvindoLabel = ctk.CTkLabel(JanelaMeio, text="Seja Bem-vindo(a)!", font=("Times New Roman", 20), text_color="black")
        self.BemvindoLabel.pack(pady=20)

        self.LoginLabel = ctk.CTkLabel(JanelaMeio, text="Usuário:", font=("Arial", 14))
        self.LoginLabel.pack(pady=5)
        self.LoginEntry = ctk.CTkEntry(JanelaMeio, width=250, placeholder_text="Digite seu usuário")
        self.LoginEntry.pack(pady=5)

        self.SenhaLabel = ctk.CTkLabel(JanelaMeio, text="Senha:", font=("Arial", 14))
        self.SenhaLabel.pack(pady=5)
        self.SenhaEntry = ctk.CTkEntry(JanelaMeio, width=250, show="•", placeholder_text="Digite sua senha")
        self.SenhaEntry.pack(pady=5)

        self.LoginButton = ctk.CTkButton(JanelaMeio, text="LOGIN", width=150, command=self.FazerLogin)
        self.LoginButton.pack(pady=20)

    def FazerLogin(self):
        nome = self.LoginEntry.get()
        senha = self.SenhaEntry.get()

        db = comunicacao() 
        db.cursor.execute("SELECT * FROM login WHERE nome = %s AND senha = %s", (nome, senha))
        VerifyLogin = db.cursor.fetchone()

        if VerifyLogin:
            messagebox.showinfo("INFO LOGIN", "Acesso Confirmado, Bem Vindo!")
            self.root.withdraw()

            adm = VerifyLogin[0]

            if adm == 1:
                from MenuAdm import Menuadm
                root_menu = ctk.CTk()
                Menuadm(root_menu)
                root_menu.mainloop()
            else:
                from MenuUsuario import MenuU
                root_menu = ctk.CTk()
                MenuU(root_menu)
                root_menu.mainloop()

        else:
            messagebox.showerror("INFO LOGIN", "Acesso Negado. Verifique se está cadastrado no sistema!")


if __name__ == "__main__":
    app = TelaLoginCadastro()