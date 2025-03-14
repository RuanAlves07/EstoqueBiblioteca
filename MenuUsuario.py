from tkinter import *
from tkinter import ttk

class MenuU:
    def Abrir_Menu(self, root):
        self.root = root
        self.root.title("MenuUsuario")
        self.root.geometry("1000x600")
        self.root.configure(background = "#f6f3ec")
        self.root.resizable(width= False, height = False)

        self.BV = Label(self.root, text="BEM VINDO", font=("Arial", 20, "bold"), bg="#f6f3ec")
        self.BV.place(anchor ="center")

        self.BV.place(x=500, y=80)

        # Botão Fornecedores
        self.FornecedoresButton = ttk.Button(self.root, text="Fornecedores", width=20, command=self.TelaFornecedores)
        self.FornecedoresButton.place(x=260, y=300)
        Label(self.root, text="Aqui você pode\ncadastrar, listar, excluir\ne pesquisar os nossos\nfornecedores", font=("Arial", 10), bg="#f6f3ec").place(x=253, y=340)

        self.ProdutosButton = ttk.Button(self.root, text="Produtos", width=20, command=self.TelaProdutos)
        self.ProdutosButton.place(x=580, y=300)
        Label(self.root, text="Na tela de produtos você pode\ncadastrar, listar, excluir\ne pesquisar os produtos", font=("Arial", 10), bg="#f6f3ec").place(x=550, y=340)


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
    app = MenuU()
    app.Abrir_Menu(root)
    root.mainloop()