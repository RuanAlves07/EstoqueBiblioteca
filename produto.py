from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from comunicacao import comunicacao

class TelaProdutos:

    def __init__(self, root):
        self.root = root
        self.root.title("PRODUTOS - GERAL ")
        self.root.geometry("400x600")
        self.root.configure(background="#f6f3ec")
        self.root.resizable(width=False, height=False)

        #Label do titulo
        Titulolabel = Label(root, text = "GERENCIADOR DE PRODUTOS", font =("Times New Roman", 18))
        Titulolabel.place(x = 30, y = 75)


    #Button para ir no menu de registro dos produto
        AButton = ttk.Button(root, text = "ADICIONAR PRODUTOS", width = 50, command = self.GoToAdicionar)
        AButton.place(x = 45, y = 200)

    #Button para ir no menu de remoção de produto
        RemoveButton = ttk.Button(root, text = "EXCLUIR PRODUTOS", width = 50, command = self.GoToExcluir)
        RemoveButton.place(x = 45, y = 300)

    #Button para ir no menu de atualização de informação de produtos
        UpdateButton = ttk.Button(root, text = "ATUALIZAR PRODUTOS", width = 50, command = self.GoToUpdate)
        UpdateButton.place(x = 45, y = 400)

    #Button para ir no menu de listagem de todos os produtos registrados
        ListButton = ttk.Button(root, text = "LISTAR PRODUTOS", width = 50, command = self.GoToList)
        ListButton.place(x = 45, y = 500)


    
    # Def para ir para a aba de adicionar livros
    def GoToAdicionar(self):

        produto_add = Tk()
        produto_add.title("PRODUTOS - REGISTRAR")
        produto_add.geometry("800x600")
        produto_add.configure(background="#f6f3ec")
        produto_add.resizable(width=False, height=False)


        # Comandos abaixos são referentes ao label, posição e caixa de entrada do nome do livro para informar valor do mesmo.

        Nomelabel = Label(produto_add,text = "Nome do livro: ", font =("Times New Roman", 20))
        Nomelabel.place(x = 115, y = 50)
        NomeEntry = ttk.Entry(produto_add, width = 30)
        NomeEntry.place(x = 330, y = 60)

        # Comandos abaixo são referentes ao label, posição e caixa de entrada da descrição do livro para informar valor do mesmo.

        Desclabel = Label(produto_add,text = "Descrição do livro: ", font =("Times New Roman", 20))
        Desclabel.place(x = 75, y = 150)
        DescEntry = ttk.Entry(produto_add, width = 30)
        DescEntry.place(x = 330, y = 160)

        # Comandos abaixo são referentes ao label, posição e caixa de entrada do genero do livro para informar valor do mesmo.

        Generolabel = Label(produto_add,text = "Gênero do livro: ", font =("Times New Roman", 20))
        Generolabel.place(x = 100, y = 250)
        GeneroEntry = ttk.Entry(produto_add, width = 30)
        GeneroEntry.place(x = 330, y = 260)

        # Comandos abaixo são referentes ao label, posição e caixa de entrada da quantidade de livros para informar valor do mesmo.

        Quantidadelabel = Label(produto_add,text = "Quantidade de livros: ", font =("Times New Roman", 20))
        Quantidadelabel.place(x = 75, y = 350)
        QuantidadeEntry = ttk.Entry(produto_add, width = 30)
        QuantidadeEntry.place(x = 330, y = 360)

        # Comandos abaixo são referentes ao label, posição e caixa de entrada do preço do livro para informar valor do mesmo.

        Precolabel = Label(produto_add,text = "Preço do livro: ", font =("Times New Roman", 20))
        Precolabel.place(x = 120, y = 450)
        PrecoEntry = ttk.Entry(produto_add, width = 30)
        PrecoEntry.place(x = 330, y = 460)


        # Def para informar que caso o usuário esqueça de informar algum campo, o sistema notifica que está faltando algum campo de entrada

        def RegistrarProduto():
 
            nome = NomeEntry.get()
            descricao = DescEntry.get()
            genero = GeneroEntry.get()
            quantidade = QuantidadeEntry.get()
            preco = PrecoEntry.get()
 
            if nome and descricao and genero and quantidade and preco:
                db = comunicacao() 
                db.RegistrarProduto(nome, descricao, genero, quantidade, preco) 
 
                messagebox.showinfo("Success", "produto registrado com sucesso!")
            else:

                messagebox.showerror("Error","Todos os campos são obrigatórios")

        # Botão para registrar o produto no banco de dados

        AddButton = ttk.Button(produto_add, text = "REGISTRAR LIVRO", width = 40, command = RegistrarProduto)
        AddButton.place(x = 300, y = 520)

        # Botão para voltar para a tela das opções sobre a questão de produtos

        VoltarButton = ttk.Button(produto_add, text = "Voltar", width = 8, command = produto_add.destroy)
        VoltarButton.place(x = 10, y = 570)


    # Def para puxar as informações da tabela e jogar tudo para a lista no qual aparece no código 

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
            produto_remove = Toplevel(self.root)
            produto_remove.title("PRODUTOS - EXCLUSÃO")
            produto_remove.geometry("800x400")
            produto_remove.configure(background="#f6f3ec")
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

            # Def feita para realizar a exclusão do produto e já comunicar com o banco para apagar as informações do produto

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

            

            RemoveButton = ttk.Button(produto_remove, text="Excluir Selecionado", command=ExclusaoProd)
            RemoveButton.pack(pady=5)

            VoltarButton = ttk.Button(produto_remove, text="Fechar", width=10, command=produto_remove.destroy)
            VoltarButton.pack(pady=5)

        
            self.PuxarInfo(tree)


    # Def para ir para a aba de atualizar informação de algum livro já registrado

    def GoToUpdate(self):

        produto_Update = Tk()
        produto_Update.title("PRODUTOS - ATUALIZAR")
        produto_Update.geometry("800x500")
        produto_Update.configure(background="#f6f3ec")
        produto_Update.resizable(width=False, height=False)


        # Label e caixa do ID do Produto dentro do Atualizar Informação

        IDlabel = Label(produto_Update,text = "ID do Produto: ", font =("Times New Roman", 20))
        IDlabel.place(x = 40, y = 15)
        self.IDEntry = ttk.Entry(produto_Update, width = 30)
        self.IDEntry.place(x = 230, y = 25)

        # Label e caixa do buscar dentro do Atualizar Informação

        BuscarButton = ttk.Button(produto_Update, text = "BUSCAR", width = 10, command = self.BuscarProduto) 
        BuscarButton.place(x = 430, y = 25)

        # Label e caixa do Nome do produto dentro do Atualizar Informação

        Nomelabel = Label(produto_Update,text = "Nome do produto: ", font =("Times New Roman", 20))
        Nomelabel.place(x = 40, y = 100)
        self.NomeEntry = ttk.Entry(produto_Update, width = 30)
        self.NomeEntry.place(x = 295, y = 110)

        # Label e caixa da descrição do produto dentro do Atualizar Informação

        Desclabel = Label(produto_Update,text = "Descrição do produto: ", font =("Times New Roman", 20))
        Desclabel.place(x = 20, y = 170)
        self.DescEntry = ttk.Entry(produto_Update, width = 30)
        self.DescEntry.place(x = 295, y = 180)

        # Label e caixa do genero do produto dentro do Atualizar Informação

        Generolabel = Label(produto_Update,text = "Gênero do produto: ", font =("Times New Roman", 20))
        Generolabel.place(x = 30, y = 240)
        self.GeneroEntry = ttk.Entry(produto_Update, width = 30)
        self.GeneroEntry.place(x = 295, y = 250)

        # Label e caixa da quantidade do produto dentro do Atualizar Informação

        Quantidadelabel = Label(produto_Update,text = "Quantidade do produto: ", font =("Times New Roman", 20))
        Quantidadelabel.place(x = 20, y = 310)
        self.QuantidadeEntry = ttk.Entry(produto_Update, width = 30)
        self.QuantidadeEntry.place(x = 295, y = 320)

        # Label e caixa do preço do produto dentro do Atualizar Informação

        Precolabel = Label(produto_Update,text = "Preço do produto: ", font =("Times New Roman", 20))
        Precolabel.place(x = 40, y = 370)
        self.PrecoEntry = ttk.Entry(produto_Update, width = 30)
        self.PrecoEntry.place(x = 295, y = 380)

        # Botão para atualizar a informação com a ação de atualizarInfo e quando apertar, já comunicar com o banco e atualizar as informações

        AttButton = ttk.Button(produto_Update, text = "ATUALIZAR PRODUTO", width = 40, command = self.AtualizarInfos) 
        AttButton.place(x = 270, y = 430)

        # Botão para voltar para a tela de menu principal dos produtos

        VoltarButton = ttk.Button(produto_Update, text = "Voltar", width = 8, command = produto_Update.destroy)
        VoltarButton.place(x = 10, y = 470)


    # Def para ir para a aba de listagem de todos os livros já cadastrados atualmente.

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

        # Botão de voltar para voltar para a tela inicial da tela de produto

        VoltarButton = ttk.Button(produto_list, text = "Voltar", width = 8, command = produto_list.destroy)
        VoltarButton.place(x = 10, y = 270)

        self.PuxarInfo(tree)


    # Def feita para a tela de "ATUALIZAR PRODUTO" no qual você pode buscar o mesmo pelo ID e identificar o que precisa alterar 

    def AtualizarInfos(self):
        idproduto = self.IDEntry.get()
        nome = self.NomeEntry.get()
        descricao = self.DescEntry.get()
        genero = self.GeneroEntry.get()
        quantidade = self.QuantidadeEntry.get()
        preco = self.PrecoEntry.get()

        # Notificação para inserir o ID do fornecedor, sem isso ele não vai alterar

        if not idproduto:
            messagebox.showwarning("Atenção", "Por favor, insira o ID do fornecedor.")
            return
        
        try:
            preco = int(preco)
        except ValueError:

            # Se o preço não for um número de fato, ele vai dar erro e vai dar a notificação

            messagebox.showerror("Erro", "Preço devem ser valores numéricos!")
            return

        # Verificação de todas as caixas, se alguma caixa estiver vazia ele vai dar a notificação

        if nome == "" or descricao == "" or genero == "" or quantidade == "" or preco == "":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return
        
        # Puxa as informações para o banco

        db = comunicacao()
        db.AtualizarProduto(idproduto, nome, descricao, genero,  quantidade, preco)
        messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")

    # Def feita para conseguir puxar as informações do produto via ID

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

        # Puxa o nome para as caixas

        self.NomeEntry.delete(0, END)
        self.NomeEntry.insert(0, produto[1])  

        # Puxa a descrição para as caixas

        self.DescEntry.delete(0, END)
        self.DescEntry.insert(0, produto[2])  

        # Puxa o gênero para as caixas

        self.GeneroEntry.delete(0, END)
        self.GeneroEntry.insert(0, produto[3])  

        # Puxa a quantidade para as caixas

        self.QuantidadeEntry.delete(0, END)
        self.QuantidadeEntry.insert(0, produto[4])  

        # Puxa o preço para as caixas

        self.PrecoEntry.delete(0, END)
        self.PrecoEntry.insert(0, produto[5])  



root = Tk()
app = TelaProdutos(root)
root.mainloop()