import customtkinter as ctk #Renomeiar o customtkinter para ctk
from customtkinter import * #importação de todo o tkinter
from tkinter import messagebox #importar do tkinter as mensagens 
from comunicacao import comunicacao #importar o banco de dados
from PIL import Image, ImageFilter #importar da biblioteca "Pillow" imagem e filtro de imagem

ctk.set_appearance_mode("Light") #Cor principal definida como "Claro"
ctk.set_default_color_theme("blue") #Cor secundaria definida como "Azul"

class TelaLoginCadastro: #Tela de fundo
    def __init__(self):
        self.root = ctk.CTk() #self.root esta virando ctk
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
        JanelaMeio = ctk.CTkToplevel(self.root) #JanelaMeio virando ctk
        JanelaMeio.title("Login") #Titulo da JanelaMeio
        JanelaMeio.configure(bg="#f6f3ec") #Cor da JanelaMeio
        JanelaMeio.resizable(False, False) #Codigo para não poder alterar a altura nem largura

        self.CentralizarJanela(JanelaMeio, 400, 300) # Centralizar a nova janela

        JanelaMeio.grab_set() # Ficar sempre em cima da tela
        JanelaMeio.focus_force() # Ficar sempre focado

        # Widgets
        self.BemvindoLabel = ctk.CTkLabel(JanelaMeio, text="Seja Bem-vindo(a)!", font=("Times New Roman", 20), text_color="black") # Label com a frase "Seja Bem-vindo"
        self.BemvindoLabel.pack(pady=20) #Posiciona a label

        self.LoginLabel = ctk.CTkLabel(JanelaMeio, text="Usuário:", font=("Arial", 14)) #Label com nome usuario
        self.LoginLabel.pack(pady=5) #Posiciona a Label
        self.LoginEntry = ctk.CTkEntry(JanelaMeio, width=250, placeholder_text="Digite seu usuário") #Entrada de texto para usuario 
        self.LoginEntry.pack(pady=5) #Posiciona a entrada de texto

        self.SenhaLabel = ctk.CTkLabel(JanelaMeio, text="Senha:", font=("Arial", 14)) #Label com nome senha
        self.SenhaLabel.pack(pady=5) #Posiciona a label
        self.SenhaEntry = ctk.CTkEntry(JanelaMeio, width=250, show="•", placeholder_text="Digite sua senha") #Entrada de texto para senha
        self.SenhaEntry.pack(pady=5) #Posiciona a entrada de texto

        self.LoginButton = ctk.CTkButton(JanelaMeio, text="LOGIN", width=150, command=self.FazerLogin) #Botão para fazer login
        self.LoginButton.pack(pady=20) #Posiciona o botão

    def FazerLogin(self):
        usuario = self.LoginEntry.get() #Recenbendo informação da entrada de texto do usuario
        senha = self.SenhaEntry.get() #Recebendo informação da entrada de texto da senha

        db = comunicacao() #db é o banco
        db.cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND senha = %s", (usuario, senha)) #Buscando do banco a entrada do usuario e a senha
        VerifyLogin = db.cursor.fetchone() #Verificando se os dados batem

        if VerifyLogin:

            messagebox.showinfo("INFO LOGIN", "Acesso Confirmado, Bem Vindo!") #Mensagem de acesso confirmado
            self.root.destroy() #Destroindo a janela principal para não dar erro na navegação de telas
            userperm = VerifyLogin[5] #buscando as colunas dentro do banco

            if userperm == "Sim": #Se o usuario for adm
                from dash import DashboardDistribuidora #Importando a tela de MenuAdm
                root_menu = ctk.CTk() #root_menu recebendo ctk
                DashboardDistribuidora(root_menu) #Classe dentro do MenuAdm recebendo o root_menu
                root_menu.mainloop() #Executando a janela(MenuAdm)
            else: #Se o usuario nao for adm
                from MenuUsuario import MenuU #
                root_menu = ctk.CTk()
                MenuU(root_menu)
                root_menu.mainloop()
        else:
            messagebox.showerror("INFO LOGIN", "Acesso Negado. Verifique se está cadastrado no sistema!")


if __name__ == "__main__":
    app = TelaLoginCadastro()
    