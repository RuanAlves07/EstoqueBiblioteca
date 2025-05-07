import customtkinter as ctk
from tkinter import messagebox
from comunicacao import comunicacao

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class TelaLoginCadastro:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Sistema de Login")
        self.root.state("zoomed")
        self.root.configure(bg="#f6f3ec")
        self.root.resizable(False, False)

        self.JanelaPequena()
        self.root.mainloop()

    def CentralizarJanela(self, tela, width, height):
        tela_width = tela.winfo_screenwidth()
        tela_height = tela.winfo_screenheight()
        x = (tela_width // 2) - (width // 2)
        y = (tela_height // 2) - (height // 2)
        tela.geometry(f"{width}x{height}+{x}+{y}")

    def JanelaPequena(self):
        JanelaMeio = ctk.CTkToplevel(self.root)
        JanelaMeio.title("Login")
        JanelaMeio.configure(bg="#f6f3ec")
        JanelaMeio.resizable(False, False)

        # Centralizar a nova janela
        self.CentralizarJanela(JanelaMeio, 400, 300)
        imagem_fundo = ctk.CTkImage(
            light_image = ("icosn\pexels-photo-2908984..png.png"),
            size=(400, 300)
        )

        bg_label = ctk.CTkLabel(JanelaMeio, image=imagem_fundo, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

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
        usuario = self.LoginEntry.get()
        senha = self.SenhaEntry.get()

        db = comunicacao() 
        db.cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND senha = %s", (usuario, senha))
        VerifyLogin = db.cursor.fetchone()

        if VerifyLogin:
            messagebox.showinfo("INFO LOGIN", "Acesso Confirmado, Bem Vindo!")
            self.root.withdraw()

            userperm = VerifyLogin[4]

            if userperm == "sim":
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