from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# Criar a janela
jan = Tk()
jan.title("Fornecedor")
jan.geometry("400x600")
jan.configure(background="#f6f3ec")
jan.resizable(width=False, height=False)


def cadastro_forn():
    jan = Tk()
    jan.title("Cadastro de Fornecedores")
    jan.geometry("400x600")
    jan.configure(background="#f6f3ec")
    jan.resizable(width=False, height=False)



    fornecedores_label = Label(jan, text="NOME EMPRESARIAL: ", font=("Arial",13))
    fornecedores_label.place(x = 120, y = 85)  # Centraliza o label na tela
    fornecedoEntry = ttk.Entry(jan, width = 40) # Criar um campo de entrada para o usuário
    fornecedoEntry.place (x = 80, y = 115)

    fornecedores_ficticio = Label(jan, text="NOME DE FANTASIA: ", font=("Arial",13))
    fornecedores_ficticio.place(x = 120, y = 160)  # Centraliza o label na tela
    ficticioEntry = ttk.Entry(jan, width = 40) # Criar um campo de entrada para o usuário
    ficticioEntry.place (x = 80, y = 190)


    voltButton = ttk.Button(jan, text = "Fechar", width = 10,command=jan.withdraw) # Cria um botão 
    voltButton.place(x = 10, y = 570)
def excluir_forn():
    jan = Tk()
    jan.title("Exclusão de Fornecedores")
    jan.geometry("400x600")
    jan.configure(background="#f6f3ec")
    jan.resizable(width=False, height=False)

    UsuarioEntry = ttk.Entry(jan, width = 40) # Criar um campo de entrada para o usuário
    UsuarioEntry.place (x = 80, y = 115)

    voltButton = ttk.Button(jan, text = "Fechar", width = 10,command=jan.withdraw) # Cria um botão 
    voltButton.place(x = 10, y = 570)



def listar_forn():
    jan = Tk()
    jan.title("lista de Fornecedores")
    jan.geometry("400x600")
    jan.configure(background="#f6f3ec")
    jan.resizable(width=False, height=False)

    voltButton = ttk.Button(jan, text = "Fechar", width = 10,command=jan.withdraw) # Cria um botão 
    voltButton.place(x = 10, y = 570)
def atuu_funci():
    jan = Tk()
    jan.title("Atualizar Fornecedores")
    jan.geometry("400x600")
    jan.configure(background="#f6f3ec")
    jan.resizable(width=False, height=False)

    voltButton = ttk.Button(jan, text = "Fechar", width = 10,command=jan.withdraw) # Cria um botão 
    voltButton.place(x = 10, y = 570)

def sair():
    jan.withdraw()



cadButton = ttk.Button( text = "Cadastrar Fornecedor", width = 50, command= cadastro_forn) # Cria um botão 
cadButton.place(x = 45, y = 200) # Posiciona o botão 

excnButton = ttk.Button( text = "Excluir Fornecedor", width = 50,command=excluir_forn) # Cria um botão 
excnButton.place(x = 45, y = 300) # Posiciona o botão 

listButton = ttk.Button( text = "Listar Fornecedor", width = 50,command=listar_forn) # Cria um botão 
listButton.place(x = 45, y = 400) # Posiciona o botão 

atuButton = ttk.Button( text = "Atualizar Fornecedor", width = 50,command=atuu_funci) # Cria um botão 
atuButton.place(x = 45, y = 500) # Posiciona o botão 

voltButton = ttk.Button( text = "Fechar", width = 10,command=sair) # Cria um botão 
voltButton.place(x = 10, y = 570) # Posiciona o botão 


jan.mainloop()