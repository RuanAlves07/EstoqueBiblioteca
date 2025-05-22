import customtkinter as ctk
from tkinter import ttk, messagebox
from comunicacao import comunicacao

ctk.set_appearance_mode("Light")  
ctk.set_default_color_theme("blue")  

class MenuU:
    def __init__(self, root):
        self.Abrir_Menu(root)

    def Abrir_Menu(self, root):
        self.root = root
        self.root.title("Menu Usuário")
        self.root.geometry("1000x400")
        self.root.configure(bg="#f6f3ec")
        self.root.resizable(True, True)

        # Título centralizado
        self.BV = ctk.CTkLabel(self.root, text="BEM-VINDO", font=("Arial", 24, "bold"))
        self.BV.pack(pady=50)

        # Frame principal para os botões
        frame_botoes = ctk.CTkFrame(self.root, fg_color="transparent")
        frame_botoes.pack(pady=80)


        self.botao_logout = ctk.CTkButton(
            self.root,
            text="LOGOUT",
            width=100,
            command=self.logout,
            fg_color="red",
            hover_color="#a52a2a"
        )
        self.botao_logout.place(x=875, y=350)

        # Botão Fornecedores
        self.FornecedoresButton = ctk.CTkButton(
            frame_botoes, text="Fornecedores", width=180, command=self.listar_forn
        )
        self.FornecedoresButton.grid(row=0, column=0, padx=80)

        desc_forn = (
            "Aqui você pode listar e pesquisar\n"
            "os nossos fornecedores"
        )
        ctk.CTkLabel(frame_botoes, text=desc_forn, font=("Arial", 10), wraplength=180).grid(
            row=1, column=0, padx=80, pady=(5, 20)
        )

        # Botão Produtos
        self.ProdutosButton = ctk.CTkButton(
            frame_botoes, text="Produtos", width=180, command=self.GoToList
        )
        self.ProdutosButton.grid(row=0, column=1, padx=80)

        desc_prod = (
            "Na tela de produtos você pode\n"
            "listar e pesquisar os produtos"
        )
        ctk.CTkLabel(frame_botoes, text=desc_prod, font=("Arial", 10), wraplength=180).grid(
            row=1, column=1, padx=80, pady=(5, 20)
        )


        self.ClientesButton = ctk.CTkButton(
            frame_botoes, text="Clientes", width=180, command=self.listar_cliente
        )
        self.ClientesButton.grid(row=0, column=2, padx=80)

        desc_Clie = (
            "Nesta tela você lista e pesquisa os clientes"
        )
        ctk.CTkLabel(frame_botoes, text=desc_Clie, font=("Arial", 10), wraplength=180).grid(
            row=1, column=2, padx=80, pady=(5, 20)
        )



    def PuxarInfo(self, tree):
        for item in tree.get_children():
            tree.delete(item)

        db = comunicacao()
        cursor = db.conn.cursor()

        try:
            cursor.execute("SELECT idproduto, nome, descricao, genero, quantidade, preco FROM produto")
            produtos = cursor.fetchall()
            for produto in produtos:
                tree.insert("", "end", values=produto)
        finally:
            cursor.close()

    def GoToList(self):
        produto_list = ctk.CTkToplevel(self.root)
        produto_list.title("PRODUTOS - LISTA")
        produto_list.geometry("800x300")
        produto_list.configure(bg="#f6f3ec")
        produto_list.resizable(False, False)

        # Atualizando as colunas para incluir o fornecedor
        colunas = ("ID", "Nome", "Descrição", "Gênero", "Quantidade", "Preço", "Fornecedor")
        tree = ttk.Treeview(produto_list, columns=colunas, show="headings")

        # Definições dos cabeçalhos
        for col in colunas:
            tree.heading(col, text=col)
        
        # Configurações de largura das colunas
        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=120)
        tree.column("Descrição", width=150)
        tree.column("Gênero", width=80, anchor="center")
        tree.column("Quantidade", width=80, anchor="center")
        tree.column("Preço", width=80, anchor="e")
        tree.column("Fornecedor", width=150)

        tree.pack(pady=10, padx=10, fill="both", expand=False)

        produto_list.grab_set()       
        produto_list.focus_force()

        def carregar_produtos():
            for item in tree.get_children():
                tree.delete(item)
            db = comunicacao()
            cursor = db.conn.cursor()
            try:
                # Consulta com INNER JOIN para trazer o nome do fornecedor
                query = """SELECT p.idproduto, p.nome, p.descricao, p.genero, p.quantidade, p.preco, f.nome FROM produto p INNER JOIN fornecedor f ON p.idfornecedor = f.idfornecedor"""
                cursor.execute(query)
                produtos = cursor.fetchall()
                for produto in produtos:
                    tree.insert("", "end", values=produto)
            finally:
                cursor.close()

        carregar_produtos()

    def carregar_fornecedores_com_endereco(self, tree):
        for item in tree.get_children():
            tree.delete(item)

        db = comunicacao()#consulta join entre as tabelas fornecedor e endereco
        query = """SELECT f.idfornecedor, f.nome, f.nomefantasia, f.CNPJ, e.rua, e.bairro, e.cidade, e.estado FROM fornecedor f LEFT JOIN endereco e ON f.idendereco = e.idendereco"""
        try:
            db.cursor.execute(query)
            fornecedores = db.cursor.fetchall()

            for fornecedor in fornecedores:
                tree.insert("", "end", values=fornecedor)
        finally:
            db.conn.close()

    def listar_forn(self):
        janela = ctk.CTkToplevel(self.root)
        janela.title("Listar Fornecedores")
        janela.geometry("700x400")
        janela.configure(bg="#f6f3ec")
        janela.resizable(False, False)

        colunas = ("ID", "Nome", "Nome Fantasia", "CNPJ", "Rua", "Bairro", "Cidade", "Estado")
    
        # Use ttk.Treeview em vez de ctk.Treeview
        tree = ttk.Treeview(janela, columns=colunas, show="headings", selectmode="browse")
    
        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.heading("Nome Fantasia", text="Nome Fantasia")
        tree.heading("CNPJ", text="CNPJ")
        tree.heading("Rua", text="Rua")
        tree.heading("Bairro", text="Bairro")
        tree.heading("Cidade", text="Cidade")
        tree.heading("Estado", text="Estado")

    
        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=100)
        tree.column("Nome Fantasia", width=100)
        tree.column("CNPJ", width=50, anchor="center") #colunas da tabela do listar 
        tree.column("Rua", width=50)
        tree.column("Bairro", width=50)
        tree.column("Cidade", width=50)
        tree.column("Estado", width=50)
    
        tree.pack(fill="both", expand=True, padx=10, pady=10)


        self.carregar_fornecedores_com_endereco(tree)
        janela.grab_set()
        janela.focus_force()

    def carregar_produtos_baixo_estoque(self):
        # Limpar a tabela
        for item in self.tree_produtos.get_children():
            self.tree_produtos.delete(item)
        
        # Consultar produtos com baixo estoque (menos de 10 unidades)
        db = comunicacao()
        db.cursor.execute("""
            SELECT idproduto, nome, genero, quantidade, preco
            FROM produto
            WHERE quantidade < 10
            ORDER BY quantidade ASC
            LIMIT 10
        """)
        
        produtos = db.cursor.fetchall()

    def logout(self):
        """Fecha o dashboard e retorna à tela de login."""
        self.root.destroy()  # Destrói completamente a janela antiga
        from Login import TelaLoginCadastro
        login_window = ctk.CTk()
        TelaLoginCadastro()
        login_window.mainloop()

    def listar_cliente(self):
        jan_lista = ctk.CTkToplevel(self.root)
        jan_lista.title("Listar Clientes")
        jan_lista.geometry("800x400")
        jan_lista.resizable(True, True)

        colunas = ("ID", "Nome", "CNPJ","Rua", "Bairro", "Cidade", "Estado")
        tree = ttk.Treeview(jan_lista, columns=colunas, show="headings", height=20)

        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=150 if col == "Nome" else 50)

        tree.pack(padx=10, pady=10, fill="both", expand=True)

        self.carregar_clientes(tree)
        jan_lista.grab_set()
        jan_lista.focus_force()

    def carregar_clientes(self, tree):
        for item in tree.get_children():
            tree.delete(item)

        db = comunicacao()
        query = """SELECT c.idcliente, c.NomeCliente, c.CNPJ, e.rua, e.bairro, e.cidade, e.estado FROM cliente c LEFT JOIN endereco e ON c.idendereco = e.idendereco"""
        try:
            db.cursor.execute(query)
            clientes = db.cursor.fetchall()

            for cliente in clientes:
                tree.insert("", "end", values=cliente)
        finally:
            db.conn.close()



        
     

    def TelaFornecedores(self):
        from fornecedor import FornecedorApp
        nova_janela = ctk.CTkToplevel(self.root)
        FornecedorApp(nova_janela)

    def TelaProdutos(self):
        from produto import TelaProdutos
        nova_janela = ctk.CTkToplevel(self.root)
        TelaProdutos(nova_janela)

    def TelaClientes(self):
        from cliente import GerenciadorClientes
        nova_janela = ctk.CTkToplevel(self.root)
        GerenciadorClientes(nova_janela)


if __name__ == "__main__":
    root = ctk.CTk()
    app = MenuU(root)
    root.mainloop()