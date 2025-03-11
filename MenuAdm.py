from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from comunicacao import comunicacao

class TelaLoginCadastro:

    def __init__(self, root):
        self.root = root
        self.root.title("Menu")
        self.root.geometry("1550x900")
        self.root.configure(background="#f6f3ec")
        self.root.resizable(width=False, height=False)

        # Botões de navegação
        self.ProdutosButton = ttk.Button(self.root, text = "Produtos", width = 40, command = self.TelaProdutos)
        self.ProdutosButton.place(x=100, y=435)

        self.FuncionariosButton = ttk.Button(self.root, text = "Funcionarios", width = 40, command = self.TelaFuncionarios)
        self.FuncionariosButton.place(x=450, y=435)

        self.FornecedoresButton = ttk.Button(self.root, text = "Fornecedores", width = 40, command = self.TelaFornecedores)
        self.FornecedoresButton.place(x=800, y=435)

        self.VoltarButton = ttk.Button(self.root, text = "Voltar", width = 40, command = self.Voltar)
        self.VoltarButton.place(x=1150, y=435)

        self.BV = Label(self.root, text = "BEM VINDO", font = ("Times New Roman", 20))
        self.BV.place(x = 675, y = 30)

    def TelaProdutos(self):
        from produto import TelaProdutos
        TelaProdutos(self.root)
        self.ProdutosButton.place(x=5000)

    def TelaFuncionarios(self):
        from funcionarios import GerenciadorFuncionarios
        GerenciadorFuncionarios(self.root)
        self.ProdutosButton.place(x=5000)

    def TelaFornecedores(self):
        from fornecedor import FornecedorApp
        FornecedorApp(self.root)
        self.ProdutosButton.place(x=5000)

    def Voltar(self):
        # Aqui você pode adicionar o código para voltar à tela de login
        jan.deiconify()  # Caso você tenha a janela de login oculta (como o código original sugeria)


jan = Tk()
tela = TelaLoginCadastro(jan)
jan.mainloop()
