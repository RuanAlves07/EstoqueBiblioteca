from tkinter import * 
from tkinter import messagebox 
from tkinter import ttk 
#from Login import jan

#Criação da tela
jan = Tk() 
jan.title("Tela de login e cadastro") 
jan.geometry("1550x900") 
jan.configure(background = "#f6f3ec") 
jan.resizable(width = False, height = False) 

def TelaProdutos():
    
    ProdutosButton.place(x = 5000)
    FuncionariosButton.place(x = 5000)
    FornecedoresButton.place(x = 5000)
    VoltarButton.place(x = 5000)

ProdutosButton = ttk.Button(text = "Produtos", width = 40, command = TelaProdutos)
ProdutosButton.place(x = 100, y = 35) 

def TelaFuncionarios():

    ProdutosButton.place(x = 5000)
    FuncionariosButton.place(x = 5000)
    FornecedoresButton.place(x = 5000)
    VoltarButton.place(x = 5000)

FuncionariosButton = ttk.Button(text = "Funcionarios", width = 40, command = TelaFuncionarios) 
FuncionariosButton.place(x = 450, y = 35) 

def TelaFornecedores():
    ProdutosButton.place(x = 5000)
    FuncionariosButton.place(x = 5000)
    FornecedoresButton.place(x = 5000)
    VoltarButton.place(x = 5000)
FornecedoresButton = ttk.Button(text = "Fornecedores", width = 40, command = TelaFornecedores) 
FornecedoresButton.place(x = 800, y = 35) 

def Voltar():
    from Login import jan

VoltarButton = ttk.Button(text = "Voltar", width = 40, command = Voltar) 
VoltarButton.place(x = 1150, y = 35) 

jan.mainloop()