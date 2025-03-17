from tkinter import *
from tkinter import ttk

class Menuadm:
    def __init__(self, root):
        self.Abrir_Menu(root)

    def Abrir_Menu(self, root):
        self.root = root
        self.root.title("MenuAdm")
        self.root.geometry("1000x600")
        self.root.configure(background = "#f6f3ec")
        self.root.resizable(width= False, height = False)

        self.BV = Label(self.root, text="BEM VINDO ISAAC", font=("Arial", 20, "bold"), bg="#f6f3ec")
        self.BV.place(anchor ="center")

        self.InfoLabel = Label(self.root, text="Por favor, selecione uma das opções abaixo", font=("Arial", 14), bg="#f6f3ec")
        self.InfoLabel.place(x = 300, y = 120)

        self.BV.place(x=500, y=80)

        # Botão Funcionários
        self.FuncionariosButton = ttk.Button(self.root, text="Funcionários", width=20, command=self.TelaFuncionarios)
        self.FuncionariosButton.place(x=105, y=400)
        Label(self.root, text="Tela de funcionários\nAqui você pode cadastrar, listar, excluir\ne pesquisar os funcionários da nossa biblioteca",font=("Arial", 10), bg="#f6f3ec").place(x=30, y=430)

        # Botão Fornecedores
        self.FornecedoresButton = ttk.Button(self.root, text="Fornecedores", width=20, command=self.TelaFornecedores)
        self.FornecedoresButton.place(x=450, y=400)
        Label(self.root, text="Aqui você pode\ncadastrar, listar, excluir\ne pesquisar os nossos\nfornecedores", font=("Arial", 10), bg="#f6f3ec").place(x=440, y=430)

        # Botão Produtos
        self.ProdutosButton = ttk.Button(self.root, text="Produtos", width=20, command=self.TelaProdutos)
        self.ProdutosButton.place(x=770, y=400)
        Label(self.root, text="Na tela de produtos você pode\ncadastrar, listar, excluir\ne pesquisar os produtos", font=("Arial", 10), bg="#f6f3ec").place(x=740, y=430)

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


if __name__ == "__main__":
    root = Tk()
    app = Menuadm(root)  
    root.mainloop()