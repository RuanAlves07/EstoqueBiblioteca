from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class TelaLoginCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela de login e cadastro")
        self.root.geometry("1550x900")
        self.root.configure(background="#f6f3ec")
        self.root.resizable(width=False, height=False)

        # Botões de navegação
        self.ProdutosButton = ttk.Button(self.root, text = "Produtos", width = 40, command = self.TelaProdutos)
        self.ProdutosButton.place(x=100, y=35)

        self.FuncionariosButton = ttk.Button(self.root, text = "Funcionarios", width = 40, command = self.TelaFuncionarios)
        self.FuncionariosButton.place(x=450, y=35)

        self.FornecedoresButton = ttk.Button(self.root, text = "Fornecedores", width = 40, command = self.TelaFornecedores)
        self.FornecedoresButton.place(x=800, y=35)

        self.VoltarButton = ttk.Button(self.root, text = "Voltar", width = 40, command = self.Voltar)
        self.VoltarButton.place(x=1150, y=35)

    def TelaProdutos(self):
        from produto import TelaProdutos
        TelaProdutos()

    def TelaFuncionarios(self):
        self.ProdutosButton.place(x=5000)
        self.FuncionariosButton.place(x=5000)
        self.FornecedoresButton.place(x=5000)
        self.VoltarButton.place(x=5000)

    def TelaFornecedores(self):
        self.ProdutosButton.place(x=5000)
        self.FuncionariosButton.place(x=5000)
        self.FornecedoresButton.place(x=5000)
        self.VoltarButton.place(x=5000)

    def Voltar(self):
        # Aqui você pode adicionar o código para voltar à tela de login
        jan.deiconify()  # Caso você tenha a janela de login oculta (como o código original sugeria)


jan = Tk()
tela = TelaLoginCadastro(jan)
jan.mainloop()
