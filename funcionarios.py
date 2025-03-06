from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Criar a janela
jan = Tk()
jan.title("Funcionarios")
jan.geometry("400x600")
jan.configure(background="#f6f3ec")
jan.resizable(width=False, height=False)




def cadastro_func():
    jan = Tk()
    jan.title("Cadastro de Funcionarios")
    jan.geometry("800x600")
    jan.configure(background="#f6f3ec")
    jan.resizable(width=False, height=False)

    NomeLabel = Label(jan, text="Nome:", font=("Times New Roman", 20))
    NomeLabel.place(x = 115, y = 50)
    UsuarioEntry = ttk.Entry(jan, width = 40) # Criar um campo de entrada para o usuário
    UsuarioEntry.place (x = 250, y = 60)

    TelefoneLabel =  Label(jan, text="Telefone:", font=("Times New Roman", 20))
    TelefoneLabel.place(x = 115, y = 120)
    TelefoneEntry = ttk.Entry(jan, width=40) # Criar um campo de entrada para o telefone
    TelefoneEntry.place (x = 250, y = 130)

    
    EnderecoLabel =  Label(jan, text="Endereço:", font=("Times New Roman", 20))
    EnderecoLabel.place(x = 115, y = 190)
    EnderecoEntry = ttk.Entry(jan, width=40) # Criar um campo de entrada para o telefone
    EnderecoEntry.place (x = 250, y = 200)

    voltButton = ttk.Button(jan, text = "Fechar", width = 10,command=jan.withdraw) # Cria um botão 
    voltButton.place(x = 10, y = 570)
def excluir_func():
    jan = Tk()
    jan.title("Exclusão de Funcionarios")
    jan.geometry("400x600")
    jan.configure(background="#f6f3ec")
    jan.resizable(width=False, height=False)


def listar_func():
    jan = Tk()
    jan.title("lista de Funcionarios")
    jan.geometry("400x600")
    jan.configure(background="#f6f3ec")
    jan.resizable(width=False, height=False)

def atuu_func():
    jan = Tk()
    jan.title("Atualizar Funcionarios")
    jan.geometry("400x600")
    jan.configure(background="#f6f3ec")
    jan.resizable(width=False, height=False)
    

def sair():
    jan.withdraw()



Titulolabel = Label(text = "GERENCIADOR DE FORNECEDOR", font =("Times New Roman", 18))
Titulolabel.place(x = 10, y = 75)

cadButton = ttk.Button( text = "Cadastrar Funcionario", width = 50, command= cadastro_func) # Cria um botão 
cadButton.place(x = 45, y = 200) # Posiciona o botão 

excnButton = ttk.Button( text = "Excluir Funcionario", width = 50,command=excluir_func) # Cria um botão 
excnButton.place(x = 45, y = 300) # Posiciona o botão 

listButton = ttk.Button( text = "Listar Funcionario", width = 50,command=listar_func) # Cria um botão 
listButton.place(x = 45, y = 400) # Posiciona o botão 

atuButton = ttk.Button( text = "Atualizar Funcionario", width = 50,command=atuu_func) # Cria um botão 
atuButton.place(x = 45, y = 500) # Posiciona o botão 

voltButton = ttk.Button( text = "Fechar", width = 10,command=sair) # Cria um botão 
voltButton.place(x = 10, y = 570) # Posiciona o botão 


jan.mainloop()

