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
    jan.geometry("400x600")
    jan.configure(background="#f6f3ec")
    jan.resizable(width=False, height=False)
    UsuarioEntry = ttk.Entry(jan, width = 30) # Criar um campo de entrada para o usuário
    UsuarioEntry.place (x = 120, y = 115)
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

