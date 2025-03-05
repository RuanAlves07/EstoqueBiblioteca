from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from config import Config

# Criar a janela
jan = Tk()
jan.title("Login")
jan.geometry("400x200")
jan.configure(background="white")
jan.resizable(width=False, height=False)

# CRIAR FRAME
LeftFrame = Frame(jan, width=150, height=200, bg="lightblue", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=250, height=200, bg="lightblue", relief="raise")
RightFrame.pack(side=RIGHT)

# ADICIONAR CAMPOS DE USUÁRIO E SENHA
UsuarioLabel = Label(RightFrame, text="Usuário:", font=("Arial", 12), bg="lightblue", fg="black")
UsuarioLabel.place(x=10, y=30)

UsuarioEntry = ttk.Entry(RightFrame, width=20)
UsuarioEntry.place(x=100, y=30)

SenhaLabel = Label(RightFrame, text="Senha:", font=("Arial", 12), bg="lightblue", fg="black")
SenhaLabel.place(x=10, y=70)

SenhaEntry = ttk.Entry(RightFrame, width=20, show="•")
SenhaEntry.place(x=100, y=70)

# Função para abrir a tela de estoque apos login
def abrir_tela_fornecedores():
    # Criar  janela para o estoque apos login
    fornecedores_janela = Toplevel()
    fornecedores_janela.title("Fornecedores")
    fornecedores_janela.geometry("800x600")
    fornecedores_janela.configure(background="grey")
    fornecedores_janela.resizable(width=False, height=False)

    
    fornecedores_label = Label(fornecedores_janela, text="Estoque", font=("Arial", 50), bg="white", fg="black")
    fornecedores_label.place(relx=0.5, rely=0.5, anchor=CENTER)  # Centraliza o label na tela
        # func. para as opções do menu
    def adicionar_fornecedor():
        messagebox.showinfo("Adicionar Fornecedor", "vai servir pra add os fornecedores")



    def sair():
        fornecedores_janela.destroy()  # fecha a janela de estoque
        jan.deiconify()  # faz logoff (vi no reddit)

    # criar a barra de menu
    barra_menu = Menu(fornecedores_janela)

    # Menu
    menu_funcoes = Menu(barra_menu, tearoff=0)
    menu_funcoes.add_command(label="Adicionar Fornecedor", command=adicionar_fornecedor)
    menu_funcoes.add_separator()
    menu_funcoes.add_command(Label = "Lista de fornecedores")
    menu_funcoes.add_command(label="Sair", command=sair)

    # Adicionar o menu "Funções" à barra de menu
    barra_menu.add_cascade(label="Funções", menu=menu_funcoes)

    # Configurar a barra de menu na janela de estoque
    fornecedores_janela.config(menu=barra_menu)


# FUNÇÃO DE LOGIN
def Login():
    usuario = UsuarioEntry.get()
    senha = SenhaEntry.get()

    db = Config()
    db.cursor.execute("SELECT * FROM usuario WHERE usuario = %s AND senha = %s", (usuario, senha))
    VerifyLogin = db.cursor.fetchone()

    if VerifyLogin:
        messagebox.showinfo(title="Sucesso", message="Acesso Confirmado. Bem Vindo!")
        jan.withdraw()



    else:
        messagebox.showerror(title="Erro", message="Acesso Negado. Verifique seu usuário e senha.")

# CRIANDO BOTÕES
LoginButton = ttk.Button(RightFrame, text="LOGIN", width=15, command=Login)
LoginButton.place(x=80, y=120)

# FUNÇÃO PARA REGISTRAR NOVO USUÁRIO
def Registrar():
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)

    NomeLabel = Label(RightFrame, text="Nome:", font=("Arial", 12), bg="lightblue", fg="black")
    NomeLabel.place(x=10, y=10)

    NomeEntry = ttk.Entry(RightFrame, width=20)
    NomeEntry.place(x=100, y=10)

    EmailLabel = Label(RightFrame, text="Email:", font=("Arial", 12), bg="lightblue", fg="black")
    EmailLabel.place(x=10, y=50)

    EmailEntry = ttk.Entry(RightFrame, width=20)
    EmailEntry.place(x=100, y=50)

    def RegistrarNoBanco():
        nome = NomeEntry.get()
        email = EmailEntry.get()
        usuario = UsuarioEntry.get()
        senha = SenhaEntry.get()

        if nome == "" or email == "" or usuario == "" or senha == "":
            messagebox.showerror(title="Erro", message="Preencha todos os campos!")
        else:
            db = Config()
            db.RegistrarNoBanco(nome, email, usuario, senha)
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")

            NomeEntry.delete(0, END)
            EmailEntry.delete(0, END)
            UsuarioEntry.delete(0, END)
            SenhaEntry.delete(0, END)

    Register = ttk.Button(RightFrame, text="REGISTRAR", width=15, command=RegistrarNoBanco)
    Register.place(x=80, y=120)

    def VoltarLogin():
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Voltar.place(x=5000)

        LoginButton.place(x=80, y=120)
        RegisterButton.place(x=80, y=150)

    Voltar = ttk.Button(RightFrame, text="VOLTAR", width=15, command=VoltarLogin)
    Voltar.place(x=80, y=150)

RegisterButton = ttk.Button(RightFrame, text="REGISTRAR", width=15, command=Registrar)
RegisterButton.place(x=80, y=150)

# Inicia o loop principal da aplicação
jan.mainloop()