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

        colunas = ("ID", "Nome", "Descrição", "Gênero", "Quantidade", "Preço")
        tree = ttk.Treeview(produto_list, columns=colunas, show="headings")

        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, anchor="w" if col != "ID" else "center")

        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=100)
        tree.column("Descrição", width=150)
        tree.column("Gênero", width=120, anchor="center")
        tree.column("Quantidade", width=120)
        tree.column("Preço", width=80)

        tree.pack(pady=10, padx=10, fill="both", expand=False)

        self.PuxarInfo(tree)

    def carregar_fornecedores(self, tree):
        for item in tree.get_children():
            tree.delete(item)

        db = comunicacao()
        cursor = db.conn.cursor()

        try:
            cursor.execute("SELECT idfornecedor, nome, nomefantasia, CNPJ, endereco FROM fornecedor")
            fornecedores = cursor.fetchall()
            for fornecedor in fornecedores:
                tree.insert("", "end", values=fornecedor)
        finally:
            cursor.close()

    def listar_forn(self):
        janela = ctk.CTkToplevel(self.root)
        janela.title("Listar Fornecedores")
        janela.geometry("700x400")
        janela.configure(bg="#f6f3ec")
        janela.resizable(False, False)

        colunas = ("ID", "Nome", "Nome Fantasia", "CNPJ", "Endereço")
        tree = ttk.Treeview(janela, columns=colunas, show="headings")

        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, anchor="w" if col not in ["ID", "CNPJ"] else "center")

        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=150)
        tree.column("Nome Fantasia", width=150)
        tree.column("CNPJ", width=120, anchor="center")
        tree.column("Endereço", width=200)

        tree.pack(pady=10, padx=10, fill="both", expand=True)

        bt_fechar = ctk.CTkButton(janela, text="Fechar", width=100, command=janela.destroy)
        bt_fechar.pack(pady=10)

        self.carregar_fornecedores(tree)

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

        colunas = ( "ID" , "Nome", "Cnpj", "Endereço") 
        tree = ttk.Treeview(jan_lista, columns=colunas, show="headings", height=20)

        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=150 if col == "Nome" or col == "ID" else 100)

        tree.pack(padx=10, pady=10, fill="both", expand=True)

        self.carregar_clientes(tree)

        jan_lista.grab_set()
        jan_lista.focus_force()
    def carregar_clientes(self, tree):
        for item in tree.get_children():
            tree.delete(item)

        db = comunicacao()
        try:
            cursor = db.conn.cursor()
            cursor.execute("SELECT idcliente, NomeCliente, CNPJ	, endereco FROM cliente")
            for row in cursor.fetchall():
                tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar clientes: {e}")



        
     

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