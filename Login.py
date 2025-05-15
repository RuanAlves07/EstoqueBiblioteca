import customtkinter as ctk #Renomeiar o customtkinter para ctk
from customtkinter import * #importação de todo o tkinter
from tkinter import messagebox #importar do tkinter as mensagens 
from comunicacao import comunicacao #importar o banco de dados
from PIL import Image, ImageFilter #importar da biblioteca "Pillow" imagem e filtro de imagem

ctk.set_appearance_mode("Light") #Cor principal definida como "Claro"
ctk.set_default_color_theme("blue") #Cor secundaria definida como "Azul"

class TelaLoginCadastro: #Tela de fundo
    def __init__(self):
        self.root = ctk.CTk() #Chamando o customtkinter
        self.root.title("Sistema de Login") #Titulo da Tela de fundo
        self.root.state("zoomed") #Codigo para ela ficar em tela cheia
        self.root.configure(bg="Blue") #Cor da tela
        self.root.resizable(False, False) #Codigo para não poder alterar a altura nem largura
        self.JanelaPequena() #Chamando a tela principal de login pequena
        self.root.mainloop() #Executando as telas

    def CentralizarJanela(self, tela, width, height): 
        tela_width = tela.winfo_screenwidth() #Obtem o tamanho da largura do monitor
        tela_height = tela.winfo_screenheight() #Obtem o tamanho da altura do monitor
        x = (tela_width // 2) - (width // 2) #Calcula a posição x para centralizar a janela
        y = (tela_height // 2) - (height // 2) #Calcula a posição y para centralizar a janela
        tela.geometry(f"{width}x{height}+{x}+{y}") #Define o tamanho e a posição da janela na tela

    def JanelaPequena(self):
        JanelaMeio = ctk.CTkToplevel(self.root)
        JanelaMeio.title("Login")
        JanelaMeio.configure(bg="#f6f3ec")
        JanelaMeio.resizable(False, False)

        # Centralizar a nova janela
        self.CentralizarJanela(JanelaMeio, 400, 300)

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
            self.root.destroy()
            userperm = VerifyLogin[5]

            if userperm == "Sim":
                from dash import DashboardDistribuidora
                root_menu = ctk.CTk()
                DashboardDistribuidora(root_menu)
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
    