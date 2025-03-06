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
    jan.geometry("800x600")
    jan.configure(background="#f6f3ec")
    jan.resizable(width=False, height=False)

    forlabel = Label(jan,text = "NOME EMPRESARIAL: ", font =("Times New Roman", 15))
    forlabel.place(x = 115, y = 55)
    fornomeEntry = ttk.Entry(jan, width = 30)
    fornomeEntry.place(x = 330, y = 60)

    fornecedores_ficticio = Label(jan, text="NOME DE FANTASIA: ", font =("Times New Roman", 15))
    fornecedores_ficticio.place(x = 115, y = 150)  # Centraliza o label na tela
    ficticioEntry = ttk.Entry(jan, width = 40) # Criar um campo de entrada para o usuário
    ficticioEntry.place (x = 330, y = 160)

    fornecedores_cnpj = Label(jan, text="CNPJ DA EMPRESA: ", font =("Times New Roman", 15))
    fornecedores_cnpj.place(x = 115, y = 255)  # Centraliza o label na tela
    cnpjEntry = ttk.Entry(jan, width = 40) # Criar um campo de entrada para o usuário
    cnpjEntry.place (x = 330, y = 260)    

    fornecedores_END = Label(jan, text="ENDEREÇO DA EMPRESA: ", font =("Times New Roman", 15))
    fornecedores_END.place(x = 85, y = 350)  # Centraliza o label na tela
    endEntry = ttk.Entry(jan, width = 40) # Criar um campo de entrada para o usuário
    endEntry.place (x = 330, y = 360)  

    AddButton = ttk.Button(jan, text = "REGISTRAR FORNECEDOR", width = 30)
    AddButton.place(x = 300, y = 520)

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