from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class TelaProdutos:


    i = Tk() 
    i.title("PRODUTOS - GERAL") 
    i.geometry("400x600") 
    i.configure(background = "#f6f3ec") 
    i.resizable(width = False, height = False) 

    # Def para ir para a aba de adicionar livros

    def GoToAdicionar():

        produto_add = Tk()
        produto_add.title("PRODUTOS - ADICIONAR")
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

        # Botão para registrar o produto no banco de dados

        AddButton = ttk.Button(produto_add, text = "REGISTRAR LIVRO", width = 30)
        AddButton.place(x = 300, y = 520)

        # Botão para voltar para a tela das opções sobre a questão de produtos

        VoltarButton = ttk.Button(produto_add, text = "Voltar", width = 8)
        VoltarButton.place(x = 10, y = 570)


    
    # Def para ir para a aba de exclusões de livros

    def GoToExcluir():
        
        produto_remove = Tk()
        produto_remove.title("PRODUTOS - EXCLUSÃO")
        produto_remove.geometry("800x600")
        produto_remove.configure(background="#f6f3ec")
        produto_remove.resizable(width=False, height=False)

    # Def para ir para a aba de atualizar informação de algum livro já registrado

    def GoToUpdate():

        produto_Update = Tk()
        produto_Update.title("PRODUTOS - ATUALIZAR")
        produto_Update.geometry("800x600")
        produto_Update.configure(background="#f6f3ec")
        produto_Update.resizable(width=False, height=False)

    # Def para ir para a aba de listagem de todos os livros já cadastrados atualmente.

    def GoToList():

        produto_list = Tk()
        produto_list.title("PRODUTOS - UPDATE")
        produto_list.geometry("800x600")
        produto_list.configure(background="#f6f3ec")
        produto_list.resizable(width=False, height=False)



    AButton = ttk.Button(text = "ADICIONAR PRODUTOS", width = 50, command = GoToAdicionar)
    AButton.place(x = 45, y = 200)

    RemoveButton = ttk.Button(text = "EXCLUIR PRODUTOS", width = 50, command = GoToExcluir)
    RemoveButton.place(x = 45, y = 300)

    UpdateButton = ttk.Button(text = "ATUALIZAR PRODUTOS", width = 50, command = GoToUpdate)
    UpdateButton.place(x = 45, y = 400)

    ListButton = ttk.Button(text = "LISTAR PRODUTOS", width = 50, command = GoToList)
    ListButton.place(x = 45, y = 500)

    VoltarButton = ttk.Button(text = "Voltar", width = 8)
    VoltarButton.place(x = 10, y = 570)


    i.mainloop()