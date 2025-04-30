from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from comunicacao import comunicacao
import customtkinter as ctk

# Configuração global do CustomTkinter
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class TelaProdutos:
    def __init__(self, root):
        self.root = root
        self.root.title("PRODUTOS - GERAL ")
        self.root.geometry("500x600")
        self.root.configure(background="#f6f3ec")
        self.root.resizable(width=False, height=False)

        # Label do título
        Titulolabel = Label(root, text="GERENCIADOR DE PRODUTOS", font=("Times New Roman", 18))
        Titulolabel.place(x=85, y=75)

        # Botão para ir no menu de registro dos produto
        AButton = ctk.CTkButton(root, text="ADICIONAR PRODUTOS", width=300, command=self.GoToAdicionar)
        AButton.place(x=100, y=200)

        # Botão para ir no menu de remoção de produto
        RemoveButton = ctk.CTkButton(root, text="EXCLUIR PRODUTOS", width=300, command=self.GoToExcluir)
        RemoveButton.place(x=100, y=300)

        # Botão para ir no menu de atualização de informação de produtos
        UpdateButton = ctk.CTkButton(root, text="ATUALIZAR PRODUTOS", width=300, command=self.GoToUpdate)
        UpdateButton.place(x=100, y=400)

        # Botão para ir no menu de listagem de todos os produtos registrados
        ListButton = ctk.CTkButton(root, text="LISTAR PRODUTOS", width=300, command=self.GoToList)
        ListButton.place(x=100, y=500)

        # Switch para alternar entre Light/Dark Mode
        self.theme_switch = ctk.CTkSwitch(root, text="Modo Escuro", command=self.alternar_tema)
        self.theme_switch.place(x=10, y=10)

    # Função para alternar modo escuro/claro
    def alternar_tema(self):
        modo = "Dark" if self.theme_switch.get() == 1 else "Light"
        ctk.set_appearance_mode(modo)

    # Def para ir para a aba de adicionar livros
    def GoToAdicionar(self):
        produto_add = ctk.CTkToplevel(self.root)
        produto_add.title("PRODUTOS - REGISTRAR")
        produto_add.geometry("800x600")
        produto_add.configure(fg_color="#f6f3ec")
        produto_add.resizable(width=False, height=False)

        # Comandos abaixos são referentes ao label, posição e caixa de entrada do nome do livro
        Nomelabel = ctk.CTkLabel(produto_add, text="Nome do livro: ", font=("Times New Roman", 20))
        Nomelabel.place(x=115, y=50)
        NomeEntry = ctk.CTkEntry(produto_add, width=300)
        NomeEntry.place(x=250, y=50)

        # Comandos abaixo são referentes ao label, posição e caixa de entrada da descrição do livro
        Desclabel = ctk.CTkLabel(produto_add, text="Descrição do livro: ", font=("Times New Roman", 20))
        Desclabel.place(x=75, y=150)
        DescEntry = ctk.CTkEntry(produto_add, width=300)
        DescEntry.place(x=250, y=150)

        # Comandos abaixo são referentes ao label, posição e caixa de entrada do gênero do livro
        Generolabel = ctk.CTkLabel(produto_add, text="Gênero do livro: ", font=("Times New Roman", 20))
        Generolabel.place(x=100, y=250)
        GeneroEntry = ctk.CTkEntry(produto_add, width=300)
        GeneroEntry.place(x=250, y=250)

        # Comandos abaixo são referentes ao label, posição e caixa de entrada da quantidade de livros
        Quantidadelabel = ctk.CTkLabel(produto_add, text="Quantidade de livros: ", font=("Times New Roman", 20))
        Quantidadelabel.place(x=75, y=350)
        QuantidadeEntry = ctk.CTkEntry(produto_add, width=300)
        QuantidadeEntry.place(x=250, y=350)

        # Comandos abaixo são referentes ao label, posição e caixa de entrada do preço do livro
        Precolabel = ctk.CTkLabel(produto_add, text="Preço do livro: ", font=("Times New Roman", 20))
        Precolabel.place(x=120, y=450)
        PrecoEntry = ctk.CTkEntry(produto_add, width=300)
        PrecoEntry.place(x=250, y=450)

        # Def para informar que caso o usuário esqueça de informar algum campo, o sistema notifica
        def RegistrarProduto():
            nome = NomeEntry.get()
            descricao = DescEntry.get()
            genero = GeneroEntry.get()
            quantidade = QuantidadeEntry.get()
            preco = PrecoEntry.get()

            if nome and descricao and genero and quantidade and preco:
                db = comunicacao()
                db.RegistrarProduto(nome, descricao, genero, quantidade, preco)
                messagebox.showinfo("Success", "Produto registrado com sucesso!")
            else:
                messagebox.showerror("Error", "Todos os campos são obrigatórios")

        # Botão para registrar o produto no banco de dados
        AddButton = ctk.CTkButton(produto_add, text="REGISTRAR LIVRO", width=200, command=RegistrarProduto)
        AddButton.place(x=300, y=520)

        # Botão para voltar
        VoltarButton = ctk.CTkButton(produto_add, text="Voltar", width=80, fg_color="gray", command=produto_add.destroy)
        VoltarButton.place(x=10, y=570)

    # Def para puxar as informações da tabela e jogar tudo para a lista
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

    # Def para ir para a aba de exclusões de livros
    def GoToExcluir(self):
        produto_remove = ctk.CTkToplevel(self.root)
        produto_remove.title("PRODUTOS - EXCLUSÃO")
        produto_remove.geometry("800x400")
        produto_remove.configure(fg_color="#f6f3ec")
        produto_remove.resizable(width=False, height=False)

        colunas = ("ID", "Nome", "Descrição", "Quantidade", "Preço")
        tree = ttk.Treeview(produto_remove, columns=colunas, show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.heading("Descrição", text="Descrição")
        tree.heading("Quantidade", text="Quantidade")
        tree.heading("Preço", text="Preço")
        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=150)
        tree.column("Descrição", width=150)
        tree.column("Quantidade", width=120, anchor="center")
        tree.column("Preço", width=200)
        tree.pack(pady=10, padx=10, fill=BOTH, expand=True)

        def ExclusaoProd():
            item_selecionado = tree.selection()
            if not item_selecionado:
                messagebox.showwarning("Atenção", "Selecione um produto para excluir.")
                return
            produto_id = tree.item(item_selecionado)["values"][0]
            resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este produto?")
            if resposta:
                db = comunicacao()
                db.ExcluirProduto(produto_id)
                self.PuxarInfo(tree)
                messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")

        RemoveButton = ctk.CTkButton(produto_remove, text="Excluir Selecionado", command=ExclusaoProd)
        RemoveButton.pack(pady=5)

        VoltarButton = ctk.CTkButton(produto_remove, text="Fechar", width=100, fg_color="gray", command=produto_remove.destroy)
        VoltarButton.pack(pady=5)

        self.PuxarInfo(tree)

    # Def para ir para a aba de atualizar informação de algum livro já registrado
    def GoToUpdate(self):
        produto_Update = ctk.CTkToplevel(self.root)
        produto_Update.title("PRODUTOS - ATUALIZAR")
        produto_Update.geometry("800x500")
        produto_Update.configure(fg_color="#f6f3ec")
        produto_Update.resizable(width=False, height=False)

        IDlabel = ctk.CTkLabel(produto_Update, text="ID do Produto: ", font=("Times New Roman", 20))
        IDlabel.place(x=40, y=15)
        self.IDEntry = ctk.CTkEntry(produto_Update, width=300)
        self.IDEntry.place(x=230, y=25)

        BuscarButton = ctk.CTkButton(produto_Update, text="BUSCAR", width=80, command=self.BuscarProduto)
        BuscarButton.place(x=550, y=25)

        Nomelabel = ctk.CTkLabel(produto_Update, text="Nome do produto: ", font=("Times New Roman", 20))
        Nomelabel.place(x=40, y=100)
        self.NomeEntry = ctk.CTkEntry(produto_Update, width=300)
        self.NomeEntry.place(x=230, y=110)

        Desclabel = ctk.CTkLabel(produto_Update, text="Descrição do produto: ", font=("Times New Roman", 20))
        Desclabel.place(x=20, y=170)
        self.DescEntry = ctk.CTkEntry(produto_Update, width=300)
        self.DescEntry.place(x=230, y=180)

        Generolabel = ctk.CTkLabel(produto_Update, text="Gênero do produto: ", font=("Times New Roman", 20))
        Generolabel.place(x=30, y=240)
        self.GeneroEntry = ctk.CTkEntry(produto_Update, width=300)
        self.GeneroEntry.place(x=230, y=250)

        Quantidadelabel = ctk.CTkLabel(produto_Update, text="Quantidade do produto: ", font=("Times New Roman", 20))
        Quantidadelabel.place(x=20, y=310)
        self.QuantidadeEntry = ctk.CTkEntry(produto_Update, width=300)
        self.QuantidadeEntry.place(x=230, y=320)

        Precolabel = ctk.CTkLabel(produto_Update, text="Preço do produto: ", font=("Times New Roman", 20))
        Precolabel.place(x=40, y=370)
        self.PrecoEntry = ctk.CTkEntry(produto_Update, width=300)
        self.PrecoEntry.place(x=230, y=380)

        AttButton = ctk.CTkButton(produto_Update, text="ATUALIZAR PRODUTO", width=200, command=self.AtualizarInfos)
        AttButton.place(x=300, y=430)

        VoltarButton = ctk.CTkButton(produto_Update, text="Voltar", width=80, fg_color="gray", command=produto_Update.destroy)
        VoltarButton.place(x=10, y=470)

    # Def para ir para a aba de listagem de todos os livros já cadastrados atualmente.
    def GoToList(self):
        produto_list = ctk.CTkToplevel(self.root)
        produto_list.title("PRODUTOS - LISTA")
        produto_list.geometry("800x300")
        produto_list.configure(fg_color="#f6f3ec")
        produto_list.resizable(width=False, height=False)

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
        tree.column("Preço", width=50)
        tree.pack(pady=10, padx=10, fill=BOTH, expand=False)

        VoltarButton = ctk.CTkButton(produto_list, text="Voltar", width=80, fg_color="gray", command=produto_list.destroy)
        VoltarButton.place(x=10, y=270)

        self.PuxarInfo(tree)

    def AtualizarInfos(self):
        idproduto = self.IDEntry.get()
        nome = self.NomeEntry.get()
        descricao = self.DescEntry.get()
        genero = self.GeneroEntry.get()
        quantidade = self.QuantidadeEntry.get()
        preco = self.PrecoEntry.get()

        if not idproduto:
            messagebox.showwarning("Atenção", "Por favor, insira o ID do produto.")
            return

        try:
            preco = float(preco)
        except ValueError:
            messagebox.showerror("Erro", "Preço deve ser um número válido.")
            return

        if not all([nome, descricao, genero, quantidade]):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        db = comunicacao()
        db.AtualizarProduto(idproduto, nome, descricao, genero, quantidade, preco)
        messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")

    def BuscarProduto(self):
        idproduto = self.IDEntry.get()
        if not idproduto:
            messagebox.showwarning("Atenção", "Por favor, insira o ID do produto.")
            return

        db = comunicacao()
        produto = db.PuxarProdutoPorID(idproduto)
        if not produto:
            messagebox.showerror("Erro", "Produto não encontrado.")
            return

        self.NomeEntry.delete(0, END)
        self.NomeEntry.insert(0, produto[1])

        self.DescEntry.delete(0, END)
        self.DescEntry.insert(0, produto[2])

        self.GeneroEntry.delete(0, END)
        self.GeneroEntry.insert(0, produto[3])

        self.QuantidadeEntry.delete(0, END)
        self.QuantidadeEntry.insert(0, produto[4])

        self.PrecoEntry.delete(0, END)
        self.PrecoEntry.insert(0, produto[5])


# Inicialização da aplicação
if __name__ == "__main__":
    root = ctk.CTk()
    app = TelaProdutos(root)
    root.mainloop()