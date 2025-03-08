from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from comunicacao import comunicacao

class TelaProdutos:


    i = Tk() 
    i.title("PRODUTOS - GERAL") 
    i.geometry("400x600") 
    i.configure(background = "#f6f3ec") 
    i.resizable(width = False, height = False) 


    
    # Def para ir para a aba de adicionar livros
    def GoToAdicionar():

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
                 RegistrarProduto(nome, descricao, genero, quantidade, preco)
 
                 messagebox.showerror("Success", "Usuario criado com sucesso!")
             else:
                 db = comunicacao() 
                 db.RegistrarProduto(nome, descricao, genero, quantidade, preco) 
                 messagebox.showerror("Error","Todos os campos são obrigatórios")

        # Botão para registrar o produto no banco de dados

        AddButton = ttk.Button(produto_add, text = "REGISTRAR LIVRO", width = 40, command = RegistrarProduto)
        AddButton.place(x = 300, y = 520)

        # Botão para voltar para a tela das opções sobre a questão de produtos

        VoltarButton = ttk.Button(produto_add, text = "Voltar", width = 8)
        VoltarButton.place(x = 10, y = 570)


    
    # Def para ir para a aba de exclusões de livros

    def GoToExcluir():
        
        produto_remove = Tk()
        produto_remove.title("PRODUTOS - EXCLUSÃO")
        produto_remove.geometry("800x400")
        produto_remove.configure(background="#f6f3ec")
        produto_remove.resizable(width=False, height=False)

        colunas = ("ID", "Nome", "Descrição", "Gênero", "Quantidade", "Preço")
        tree = ttk.Treeview(produto_remove, columns=colunas, show="headings")

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

        RemoveButton = ttk.Button(produto_remove, text = "REMOVER LIVRO", width = 40) #command = RemoverNoBanco
        RemoveButton.place(x = 270, y = 320)
    
        VoltarButton = ttk.Button(produto_remove, text = "Voltar", width = 8)
        VoltarButton.place(x = 10, y = 370)

    # Def para ir para a aba de atualizar informação de algum livro já registrado

    def GoToUpdate():

        produto_Update = Tk()
        produto_Update.title("PRODUTOS - ATUALIZAR")
        produto_Update.geometry("800x600")
        produto_Update.configure(background="#f6f3ec")
        produto_Update.resizable(width=False, height=False)


        IDlabel = Label(produto_Update,text = "ID do Produto: ", font =("Times New Roman", 20))
        IDlabel.place(x = 100, y = 60)
        IDEntry = ttk.Entry(produto_Update, width = 30)
        IDEntry.place(x = 330, y = 70)

        Nomelabel = Label(produto_Update,text = "Nome do produto: ", font =("Times New Roman", 20))
        Nomelabel.place(x = 90, y = 130)
        NomeEntry = ttk.Entry(produto_Update, width = 30)
        NomeEntry.place(x = 330, y = 140)

        Desclabel = Label(produto_Update,text = "Descrição do produto: ", font =("Times New Roman", 20))
        Desclabel.place(x = 60, y = 200)
        DescEntry = ttk.Entry(produto_Update, width = 30)
        DescEntry.place(x = 330, y = 210)

        Generolabel = Label(produto_Update,text = "Descrição do produto: ", font =("Times New Roman", 20))
        Generolabel.place(x = 60, y = 280)
        GeneroEntry = ttk.Entry(produto_Update, width = 30)
        GeneroEntry.place(x = 330, y = 290)

        Quantidadelabel = Label(produto_Update,text = "Quantidade do produto: ", font =("Times New Roman", 20))
        Quantidadelabel.place(x = 50, y = 350)
        QuantidadeEntry = ttk.Entry(produto_Update, width = 30)
        QuantidadeEntry.place(x = 330, y = 360)

        Precolabel = Label(produto_Update,text = "Preço do produto: ", font =("Times New Roman", 20))
        Precolabel.place(x = 80, y = 420)
        PrecoEntry = ttk.Entry(produto_Update, width = 30)
        PrecoEntry.place(x = 330, y = 430)

        AttButton = ttk.Button(produto_Update, text = "ATUALIZAR PRODUTO", width = 40) #command = AtualizarNoBanco
        AttButton.place(x = 270, y = 520)

        VoltarButton = ttk.Button(produto_Update, text = "Voltar", width = 8)
        VoltarButton.place(x = 10, y = 570)

    # Def para ir para a aba de listagem de todos os livros já cadastrados atualmente.

    def GoToList(self):

        produto_list = Tk()
        produto_list.title("PRODUTOS - LISTA")
        produto_list.geometry("800x300")
        produto_list.configure(background="#f6f3ec")
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
        tree.column("Preço", width = 50)

        tree.pack(pady=10, padx=10, fill=BOTH, expand=False)

        VoltarButton = ttk.Button(produto_list, text = "Voltar", width = 8)
        VoltarButton.place(x = 10, y = 270)


            
    #Label do titulo
    Titulolabel = Label(text = "GERENCIADOR DE PRODUTOS", font =("Times New Roman", 18))
    Titulolabel.place(x = 30, y = 75)


    #Button para ir no menu de registro dos produto
    AButton = ttk.Button(text = "ADICIONAR PRODUTOS", width = 50, command = GoToAdicionar)
    AButton.place(x = 45, y = 200)

    #Button para ir no menu de remoção de produto
    RemoveButton = ttk.Button(text = "EXCLUIR PRODUTOS", width = 50, command = GoToExcluir)
    RemoveButton.place(x = 45, y = 300)

    #Button para ir no menu de atualização de informação de produtos
    UpdateButton = ttk.Button(text = "ATUALIZAR PRODUTOS", width = 50, command = GoToUpdate)
    UpdateButton.place(x = 45, y = 400)

    #Button para ir no menu de listagem de todos os produtos registrados
    ListButton = ttk.Button(text = "LISTAR PRODUTOS", width = 50, command = GoToList)
    ListButton.place(x = 45, y = 500)

    #Button de voltar para tela de menu principal do sistema
    VoltarButton = ttk.Button(text = "Voltar", width = 8)
    VoltarButton.place(x = 10, y = 570)


    i.mainloop()