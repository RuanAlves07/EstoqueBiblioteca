from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class TelaProdutos:


    i = Tk() 
    i.title("PRODUTOS - GERAL") 
    i.geometry("400x600") 
    i.configure(background = "#f6f3ec") 
    i.resizable(width = False, height = False) 

    def GoToAdicionar():

        produto_add = Tk()
        produto_add.title("PRODUTOS - ADICIONAR")
        produto_add.geometry("800x600")
        produto_add.configure(background="#f6f3ec")
        produto_add.resizable(width=False, height=False)
        Nomelabel = Label(produto_add,text = "Nome do livro: ", font =("Arial", 20))
        Nomelabel.place(x = 75, y = 50)
        Desclabel = Label(produto_add,text = "Descrição do livro: ", font =("Arial", 20))
        Desclabel.place(x = 75, y = 150)
        Generolabel = Label(produto_add,text = "Gênero do livro: ", font =("Arial", 20))
        Generolabel.place(x = 75, y = 250)
        Quantidadelabel = Label(produto_add,text = "Quantidade de livros: ", font =("Arial", 20))
        Quantidadelabel.place(x = 75, y = 350)
        Precolabel = Label(produto_add,text = "Quantidade de livros: ", font =("Arial", 20))
        Precolabel.place(x = 75, y = 450)
    

    def GoToExcluir():
        
        produto_remove = Tk()
        produto_remove.title("PRODUTOS - EXCLUSÃO")
        produto_remove.geometry("800x600")
        produto_remove.configure(background="#f6f3ec")
        produto_remove.resizable(width=False, height=False)

    def GoToUpdate():

        produto_Update = Tk()
        produto_Update.title("PRODUTOS - ATUALIZAR")
        produto_Update.geometry("800x600")
        produto_Update.configure(background="#f6f3ec")
        produto_Update.resizable(width=False, height=False)

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