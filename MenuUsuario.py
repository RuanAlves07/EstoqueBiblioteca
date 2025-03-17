from tkinter import *
from tkinter import ttk
from comunicacao import comunicacao

class MenuU:

    def __init__(self, root):
        self.Abrir_Menu(root)

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
        self.FornecedoresButton = ttk.Button(self.root, text="Fornecedores", width=20, command=self.listar_forn)
        self.FornecedoresButton.place(x=260, y=300)
        Label(self.root, text="Aqui você pode\ncadastrar, listar, excluir\ne pesquisar os nossos\nfornecedores", font=("Arial", 10), bg="#f6f3ec").place(x=253, y=340)


        self.ProdutosButton = ttk.Button(self.root, text="Produtos", width=20, command=self.GoToList)
        self.ProdutosButton.place(x=580, y=300)
        Label(self.root, text="Na tela de produtos você pode\ncadastrar, listar, excluir\ne pesquisar os produtos", font=("Arial", 10), bg="#f6f3ec").place(x=550, y=340)

    
    #Puxar informação de produtos
    def PuxarInfo(self, tree):
        for item in tree.get_children():
            tree.delete(item)

        db = comunicacao()  # Define a comunicação com o banco
        cursor = db.conn.cursor()  # Cria o cursor fora do loop
    
        try:
            cursor.execute("SELECT idproduto, nome, descricao, genero, quantidade, preco FROM produto")
            produtos = cursor.fetchall()  
            for produto in produtos:
                tree.insert("", "end", values=produto)
        finally:
            cursor.close()

    #Listar do produto
    def GoToList(self):

        produto_list = Tk()
        produto_list.title("PRODUTOS - LISTA")
        produto_list.geometry("800x300")
        produto_list.configure(background="#f6f3ec")
        produto_list.resizable(width=False, height=False)

        # Colunas para identificar quais vão ser as informações que vão aparecer

        colunas = ("ID", "Nome", "Descrição", "Gênero", "Quantidade", "Preço")
        tree = ttk.Treeview(produto_list, columns=colunas, show="headings")

        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.heading("Descrição", text="Descrição")
        tree.heading("Gênero", text="Gênero")
        tree.heading("Quantidade", text="Quantidade")
        tree.heading("Preço", text="Preço")


        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=100)
        tree.column("Descrição", width=150)
        tree.column("Gênero", width=120, anchor="center")
        tree.column("Quantidade", width=120)
        tree.column("Preço", width = 50)

        tree.pack(pady=10, padx=10, fill=BOTH, expand=False)

        self.PuxarInfo(tree)


    #Buscar do fornecedores
    def carregar_fornecedores(self, tree):
        # Limpa a treeview antes de carregar novos dados
        for item in tree.get_children():
            tree.delete(item)

        # Obtém os dados dos fornecedores do banco de dados
        db = comunicacao()
        cursor = db.conn.cursor()  # Cria um novo cursor

        
        cursor.execute("SELECT idfornecedor, nome, nomefantasia, CNPJ, endereco FROM fornecedor")
        fornecedores = cursor.fetchall()  # Consome todos os resultados

            # Insere os fornecedores na treeview
        for fornecedor in fornecedores:
            tree.insert("", "end", values=fornecedor)


    #Listar fornecedores
    def listar_forn(self):
        janela = Toplevel(self.root)
        janela.title("Listar Fornecedores")
        janela.geometry("700x400")
        janela.configure(background="#f6f3ec")
        janela.resizable(width=False, height=False)

        colunas = ("ID", "Nome", "Nome Fantasia", "CNPJ", "Endereço")
        tree = ttk.Treeview(janela, columns=colunas, show="headings")

        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.heading("Nome Fantasia", text="Nome Fantasia")
        tree.heading("CNPJ", text="CNPJ")
        tree.heading("Endereço", text="Endereço")

        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=150)
        tree.column("Nome Fantasia", width=150)
        tree.column("CNPJ", width=120, anchor="center")
        tree.column("Endereço", width=200)

        tree.pack(pady=10, padx=10, fill=BOTH, expand=True)

        bt_fechar = ttk.Button(janela, text="Fechar", width=10, command=janela.destroy)
        bt_fechar.pack(pady=5)

        # Carrega os fornecedores na treeview
        self.carregar_fornecedores(tree)


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
    app = MenuU(root)  
    root.mainloop()