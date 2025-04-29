from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from comunicacao import comunicacao

class Menuadm:
    def __init__(self, root):
        self.Abrir_Menu(root)

    def BuscarUsuario(self, nome):
        self.cursor.execute("SELECT * FROM login WHERE nome = %s", (nome,))
        
    def Abrir_Menu(self, root):
        self.root = root
        self.root.title("MenuAdm")
        self.root.geometry("1000x600")
        self.root.configure(background = "#f6f3ec")
        self.root.resizable(width= False, height = False)

        self.BV = Label(self.root, text="BEM VINDO", font=("Arial", 20, "bold"), bg="#f6f3ec")
        self.BV.place(anchor ="center")

        self.InfoLabel = Label(self.root, text="Por favor, selecione uma das opções abaixo", font=("Arial", 14), bg="#f6f3ec")
        self.InfoLabel.place(x = 300, y = 120)

        self.BV.place(x=500, y=80)

        cadButton = ttk.Button(self.root, text="Cadastrar Usuario", width=20, command=self.CriarUsuario)
        cadButton.place(x=450, y=450)
        Label(self.root, text="Você pode cadastrar\n o seu usuario aqui", font=("Arial", 10), bg="#f6f3ec").place(x=450, y=490)

        # Botão Funcionários
        self.FuncionariosButton = ttk.Button(self.root, text="Funcionários", width=20, command=self.TelaFuncionarios)
        self.FuncionariosButton.place(x=105, y=250)
        Label(self.root, text="Tela de funcionários\nAqui você pode cadastrar, listar, excluir\ne pesquisar os funcionários da nossa biblioteca",font=("Arial", 10), bg="#f6f3ec").place(x=30, y=280)

        # Botão Fornecedores
        self.FornecedoresButton = ttk.Button(self.root, text="Fornecedores", width=20, command=self.TelaFornecedores)
        self.FornecedoresButton.place(x=450, y=250)
        Label(self.root, text="Aqui você pode\ncadastrar, listar, excluir\ne pesquisar os nossos\nfornecedores", font=("Arial", 10), bg="#f6f3ec").place(x=440, y=280)

        # Botão Produtos
        self.ProdutosButton = ttk.Button(self.root, text="Produtos", width=20, command=self.TelaProdutos)
        self.ProdutosButton.place(x=770, y=250)
        Label(self.root, text="Na tela de produtos você pode\ncadastrar, listar, excluir\ne pesquisar os produtos", font=("Arial", 10), bg="#f6f3ec").place(x=740, y=280)

    def TelaFuncionarios(self):
        from funcionarios import GerenciadorFuncionarios
        nova_janela = Toplevel(self.root)
        GerenciadorFuncionarios(nova_janela)

    def TelaFornecedores(self):
        from fornecedor import FornecedorApp
        nova_janela = Toplevel(self.root)
        FornecedorApp(nova_janela)

    def TelaProdutos(self):
        from produto import TelaProdutos
        nova_janela = Toplevel(self.root)
        TelaProdutos(nova_janela)

    def CriarUsuario(self):
        jan = Toplevel(self.root)
        jan.title("Cadastro de Usuario")
        jan.geometry("500x300")
        jan.configure(background="#f6f3ec")
        jan.resizable(width=False, height=False)

        UsuarioLabel = Label(jan, text="Usuario: ", font=("Times New Roman", 15))
        UsuarioLabel.place(x=70, y=55)
        self.UserNomeEntry = ttk.Entry(jan, width=30)
        self.UserNomeEntry.place(x=220, y=60)

        SenhaLabel = Label(jan, text="Senha: ", font=("Times New Roman", 15))
        SenhaLabel.place(x=70, y=100)
        self.SenhaEntry = ttk.Entry(jan, width=30)
        self.SenhaEntry.place(x=220, y=105)

        NomeCompletoLabel = Label(jan, text="Nome Completo: ", font=("Times New Roman", 15))
        NomeCompletoLabel.place(x=70, y=145)
        self.UserNomeCEntry = ttk.Entry(jan, width=30)
        self.UserNomeCEntry.place(x=220, y=155)


        AddButton = ttk.Button(jan, text="REGISTRAR USUARIO", width=30, command=self.RegistrarUsuarios)
        AddButton.place(x=150, y=240)

    def RegistrarUsuarios(self):
        nome = self.UserNomeEntry.get()
        senha = self.SenhaEntry.get()
        Usuario = self.UserNomeCEntry.get()

        if nome == "" or senha == "" or Usuario == "":
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
        else:
            db = comunicacao()
            db.RegistrarCliente(nome, senha, Usuario)
            messagebox.showinfo("Successo", "Usuario criado com sucesso!")
            self.limpar_campos()

    def limpar_campos(self):
        self.UserNomeEntry.delete(0, END)  
        self.SenhaEntry.delete(0, END)  
        self.UserNomeCEntry.delete(0, END)


if __name__ == "__main__":
    root = Tk()
    app = Menuadm(root)  
    root.mainloop()