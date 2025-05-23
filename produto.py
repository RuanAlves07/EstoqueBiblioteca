from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from comunicacao import comunicacao  
from CTkMenuBar import *
from fornecedor import FornecedorApp 

# Configuração global do CustomTkinter
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class TelaProdutos:
    def __init__(self, root):
        self.root = root
        self.root.title("PRODUTOS - GERAL ")
        self.root.geometry("800x600")
        self.root.configure(background="#f6f3ec")
        self.root.resizable(width=False, height=False)
        
        self.idfornecedor_selecionado = None 
        
        root.iconbitmap(default="icons/livro.ico")  # Define o ícone da janela


        # Barra do atalho de navegação para ir de tela em tela
        BarraNavegabilidade = CTkMenuBar(root)
        botao_1 = BarraNavegabilidade.add_cascade("Produtos", command = self.GoToproduto)
        botao_2 = BarraNavegabilidade.add_cascade("Fornecedores", command = self.TelaFornecedores)
        botao_3 = BarraNavegabilidade.add_cascade("Funcionarios", command = self.TelaFuncionarios)
        botao_4 = BarraNavegabilidade.add_cascade("Clientes", command = self.TelaClientes)

        # Label do título
        Titulolabel = ctk.CTkLabel(self.root, text="GERENCIADOR DE PRODUTOS", font=("Poppins", 22, "bold"))
        Titulolabel.place(x=240 , y = 75)

        # Botão para ir no menu de registro dos produtos
        AButton = ctk.CTkButton(root, text="ADICIONAR PRODUTOS", width=300, command=self.GoToAdicionar)
        AButton.place(x=250, y=200)

        # Botão para ir no menu de remoção de produto
        RemoveButton = ctk.CTkButton(root, text="EXCLUIR PRODUTOS", width=300, command=self.GoToExcluir)
        RemoveButton.place(x=250, y=300)

        # Botão para ir no menu de atualização de informação de produtos
        UpdateButton = ctk.CTkButton(root, text="ATUALIZAR PRODUTOS", width=300, command=self.GoToUpdate)
        UpdateButton.place(x=250, y=400)

        # Botão para ir no menu de listagem de todos os produtos registrados
        ListButton = ctk.CTkButton(root, text="LISTAR PRODUTOS", width=300, command=self.GoToList)
        ListButton.place(x=250, y=500)


    # Def para funcionalidade do atalho de navegabilidade e ir para a tela de clientes
    def TelaClientes(self):
        from cliente import GerenciadorClientes
        janela = ctk.CTkToplevel(self.root)
        janela.grab_set()
        janela.focus_force()
        GerenciadorClientes(janela)

    # Def para funcionalidade do atalho de navegabilidade e ir para a tela de fornecedores 
    def TelaFornecedores(self):
        from fornecedor import FornecedorApp
        nova_janela = ctk.CTkToplevel(self.root)
        nova_janela.grab_set()
        nova_janela.focus_force()
        FornecedorApp(nova_janela)

    # Def para funcionalidade do atalho de navegabilidade e ir para a tela de produto
    def GoToproduto(self):
        from produto import TelaProdutos
        nova_janela = ctk.CTkToplevel(self.root)
        nova_janela.grab_set()       
        nova_janela.focus_force()    
        TelaProdutos(nova_janela)

    # Def para funcionalidade do atalho de navegabilidade e ir para a tela de 
    def TelaFuncionarios(self):
        from funcionarios import GerenciadorFuncionarios
        nova_janela = ctk.CTkToplevel(self.root)
        nova_janela.grab_set()       
        nova_janela.focus_force()    
        GerenciadorFuncionarios(nova_janela)


    # Métodos para ir para a tela de adicionar
    def GoToAdicionar(self):
        produto_add = ctk.CTkToplevel(self.root)
        produto_add.title("PRODUTOS - REGISTRAR")
        produto_add.geometry("800x600")
        produto_add.configure(fg_color="#f6f3ec")
        produto_add.resizable(width=False, height=False)

        frame_add = ctk.CTkFrame(produto_add, corner_radius=10)
        frame_add.pack(padx=60, pady=50, fill="both", expand=True)

        titulo = ctk.CTkLabel(frame_add, text="CADASTRO DE PRODUTO", font=("Segoe UI", 18, "bold"))
        titulo.pack(pady=20)

        self.NomeEntry = ctk.CTkEntry(frame_add, placeholder_text="Nome do produto", width=300, height=40)
        self.NomeEntry.pack(pady=10)

        self.DescEntry = ctk.CTkEntry(frame_add, placeholder_text="Descrição do produto", width=300, height=40)
        self.DescEntry.pack(pady=10)

        self.GeneroEntry = ctk.CTkEntry(frame_add, placeholder_text="Categoria do produto", width=300, height=40)
        self.GeneroEntry.pack(pady=10)

        self.QuantidadeEntry = ctk.CTkEntry(frame_add, placeholder_text="Quantidade do produto", width=300, height=40)
        self.QuantidadeEntry.pack(pady=10)

        self.PrecoEntry = ctk.CTkEntry(frame_add, placeholder_text="Preço do produto", width=300, height=40)
        self.PrecoEntry.pack(pady=10)

        self.FornecedorEntry = ctk.CTkEntry(frame_add, placeholder_text="Fornecedor...", width=300, height=40)
        self.FornecedorEntry.pack(pady=10)


        self.botao_linkar_fornecedor = ctk.CTkButton(frame_add, text="🔗", width=40, command=self.Tela_FornProduto)
        self.botao_linkar_fornecedor.place(x = 500, y = 385)   

                
        frame_add.grab_set()       
        frame_add.focus_force()
        # Def para registrar o produto e se comunicar com o banco de dados para registrar o mesmo no banco.         
        def RegistrarProduto():
            nome = self.NomeEntry.get()
            descricao = self.DescEntry.get()
            genero = self.GeneroEntry.get()
            quantidade = self.QuantidadeEntry.get()
            preco = self.PrecoEntry.get()
            idfornecedor = self.idfornecedor_selecionado

            if nome and descricao and genero and quantidade and preco and idfornecedor:
                db = comunicacao()
                db.RegistrarProduto(idfornecedor, nome, descricao, genero, quantidade, preco)
                messagebox.showinfo("Sucesso", "Produto registrado com sucesso!")
            else:
                messagebox.showerror("Error", "Todos os campos são obrigatórios")

        AddButton = ctk.CTkButton(produto_add, text="REGISTRAR PRODUTO", width=200, command=RegistrarProduto)
        AddButton.place(x=300, y=520)

        VoltarButton = ctk.CTkButton(produto_add, text="Voltar", width=80, fg_color="gray", command=produto_add.destroy)
        VoltarButton.place(x=10, y=570)

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

        colunas = ("ID Produto", "Nome", "Descrição", "Genêro", "Quantidade", "Preço")
        tree = ttk.Treeview(produto_remove, columns=colunas, show="headings")
 
        for col in colunas:
            tree.heading(col, text=col)

        tree.column("ID Produto", width=20, anchor="center")
        tree.column("Nome", width=150, anchor="center")
        tree.column("Descrição", width=200)
        tree.column("Genêro", width=20, anchor="center")
        tree.column("Quantidade", width=50, anchor="center")
        tree.column("Preço", width=70,anchor="center")
        tree.pack(pady=10, padx=10, fill=BOTH, expand=True)

        # Def para realizar a exclusão do produto e informar o banco de dados sobre a exclusão do mesmo
        produto_remove.grab_set()       
        produto_remove.focus_force()

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

        def carregar_produtos():
            for item in tree.get_children():
                tree.delete(item)
            db = comunicacao()


        RemoveButton = ctk.CTkButton(produto_remove, text="Excluir Selecionado", command=ExclusaoProd)
        RemoveButton.pack(pady=5)

        VoltarButton = ctk.CTkButton(produto_remove, text="Fechar", width=100, fg_color="gray", command=produto_remove.destroy)
        VoltarButton.pack(pady=5)

        self.PuxarInfo(tree)

    # Def para ir para a aba de atualizar informação de algum livro já registrado

    def GoToUpdate(self):
        produto_Update = ctk.CTkToplevel(self.root)
        produto_Update.title("PRODUTOS - ATUALIZAR")
        produto_Update.geometry("800x600")
        produto_Update.configure(fg_color="#f6f3ec")
        produto_Update.resizable(width=False, height=False)

        frame = ctk.CTkFrame(produto_Update, corner_radius=10)
        frame.pack(padx=60, pady=50, fill="both", expand=True)

        titulo = ctk.CTkLabel(frame, text="ATUALIZAR PRODUTO", font=("Segoe UI", 18, "bold"))
        titulo.pack(pady=20)

        self.IDEntry = ctk.CTkEntry(frame, placeholder_text="ID do Produto", width=300, height=40)
        self.IDEntry.pack(pady=10)        

        BuscarButton = ctk.CTkButton(produto_Update, text="BUSCAR", width=80, command=self.BuscarProduto)
        BuscarButton.place(x=570, y=130)

        self.NomeEntry = ctk.CTkEntry(frame, placeholder_text="Nome do livro", width=300, height=40)
        self.NomeEntry.pack(pady=10)

        self.DescEntry = ctk.CTkEntry(frame, placeholder_text="Descrição do livro", width=300, height=40)
        self.DescEntry.pack(pady=10)

        self.GeneroEntry = ctk.CTkEntry(frame, placeholder_text="Gênero do livro", width=300, height=40)
        self.GeneroEntry.pack(pady=10)

        self.QuantidadeEntry = ctk.CTkEntry(frame, placeholder_text="Quantidade do livro", width=300, height=40)
        self.QuantidadeEntry.pack(pady=10)

        self.PrecoEntry = ctk.CTkEntry(frame, placeholder_text="Preço do livro", width=300, height= 40)
        self.PrecoEntry.pack(pady = 10)

        AttButton = ctk.CTkButton(produto_Update, text="ATUALIZAR PRODUTO", width=200, command=self.AtualizarInfos)
        AttButton.place(x=300, y=500)

        VoltarButton = ctk.CTkButton(produto_Update, text="Voltar", width=80, fg_color="gray", command=produto_Update.destroy)
        VoltarButton.place(x=10, y=560)

        produto_Update.grab_set()       
        produto_Update.focus_force()

    # Def para ir para a aba de listagem de todos os livros já cadastrados atualmente.

    def GoToList(self):
        produto_list = ctk.CTkToplevel(self.root)
        produto_list.title("PRODUTOS - LISTA")
        produto_list.geometry("900x300")
        produto_list.configure(fg_color="#f6f3ec")
        produto_list.resizable(width=False, height=False)

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

        tree.pack(pady=10, padx=10, fill=BOTH, expand=False)

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

        VoltarButton = ctk.CTkButton(produto_list, text="Voltar", width=80, fg_color="gray", command=produto_list.destroy)
        VoltarButton.place(x=10, y=270)

    # Def para realizar a atualização do produto e se comunicar com o banco de dados
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

    # Def para puxar o ID do produto e trazer as informações do produto

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
        self.NomeEntry.insert(0, produto[2])

        self.DescEntry.delete(0, END)
        self.DescEntry.insert(0, produto[3])

        self.GeneroEntry.delete(0, END)
        self.GeneroEntry.insert(0, produto[4])

        self.QuantidadeEntry.delete(0, END)
        self.QuantidadeEntry.insert(0, produto[5])

        self.PrecoEntry.delete(0, END)
        self.PrecoEntry.insert(0, produto[6])

    # Def da tela para linkar o fornecedor com o produto via fk
    def Tela_FornProduto(self):
        
        janela_pesquisa = ctk.CTkToplevel(self.root)
        janela_pesquisa.title("Pesquisar Fornecedor")
        janela_pesquisa.geometry("600x400")
        janela_pesquisa.resizable(False, False)
        janela_pesquisa.grab_set() 

        
        entry_pesquisa = ctk.CTkEntry(janela_pesquisa, placeholder_text="Nome do fornecedor...")
        entry_pesquisa.pack(pady=10, padx=20, fill="x")

        
        frame_resultados = ctk.CTkFrame(janela_pesquisa)
        frame_resultados.pack(pady=10, padx=20, fill="both", expand=True)

        # Função de pesquisa definida antes do uso
        def pesquisar_fornecedores(termo, frame_resultados):
            #
            for widget in frame_resultados.winfo_children():
                widget.destroy()
            db = comunicacao()
            try:
                if termo.strip() == "":
                    db.cursor.execute("SELECT idfornecedor, nome FROM fornecedor")
                else:
                    db.cursor.execute("SELECT idfornecedor, nome FROM fornecedor WHERE nome LIKE %s", (f"%{termo}%",))
                fornecedores = db.cursor.fetchall()
                if not fornecedores:
                    label_vazio = ctk.CTkLabel(frame_resultados, text="Nenhum fornecedor encontrado.")
                    label_vazio.pack(pady=10)
                    return
                # Exibe os fornecedores como botões clicáveis
                for idx, (idfornecedor, nome) in enumerate(fornecedores):
                    def on_select(idforn=idfornecedor, nomeforn=nome):
                        self.FornecedorEntry.delete(0, "end")  # Atualiza o campo de fornecedor
                        self.FornecedorEntry.insert(0, nomeforn)
                        self.idfornecedor_selecionado = idforn  # Salva o ID do fornecedor
                        janela_pesquisa.destroy()

                    btn = ctk.CTkButton(
                        frame_resultados,
                        text=f"{nome} (ID: {idfornecedor})",
                        anchor="w",
                        command=on_select
                    )
                    btn.pack(pady=5, fill="x")
            finally:
                db.conn.close()

        # Função de atualização da lista de fornecedores
        def atualizar(event=None):
            termo = entry_pesquisa.get()
            pesquisar_fornecedores(termo, frame_resultados)

        entry_pesquisa.bind("<KeyRelease>", atualizar)

        # Chama uma vez para carregar todos os fornecedores inicialmente
        pesquisar_fornecedores("", frame_resultados)

    def pesquisar_fornecedores(self, termo, frame_resultados):
        # Limpa resultados anteriores
        for widget in frame_resultados.winfo_children():
            widget.destroy()

        db = comunicacao()
        try:
            if termo.strip() == "":
                db.cursor.execute("SELECT idfornecedor, nome FROM fornecedor")
            else:
                db.cursor.execute("SELECT idfornecedor, nome FROM fornecedor WHERE nome LIKE %s", (f"%{termo}%",))
                
            fornecedores = db.cursor.fetchall()

            if not fornecedores:
                label_vazio = ctk.CTkLabel(frame_resultados, text="Nenhum fornecedor encontrado.")
                label_vazio.pack(pady=10)
                return

            # Exibe os fornecedores como botões clicáveis
            for idx, (idfornecedor, nome) in enumerate(fornecedores):
                def on_select(idforn=idfornecedor, nomeforn=nome):
                    self.NomeEntry.delete(0, "end")
                    self.NomeEntry.insert(0, nomeforn)
                    

                btn = ctk.CTkButton(
                    frame_resultados,
                    text=f"{nome} (ID: {idfornecedor})",
                    anchor="w",
                    command=on_select
                )
                btn.pack(pady=5, fill="x")
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao pesquisar fornecedores: {e}")


# Inicialização da aplicação
if __name__ == "__main__":
    root = ctk.CTk()
    app = TelaProdutos(root)
    root.mainloop()