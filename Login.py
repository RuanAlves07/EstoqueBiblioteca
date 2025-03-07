from tkinter import * 
from tkinter import messagebox 
from tkinter import ttk 
from comunicacao import login

#Criação da tela
jan = Tk() 
jan.title("Tela de login e cadastro") 
jan.geometry("500x500") 
jan.configure(background = "#f6f3ec") 
jan.resizable(width = False, height = False) 



#Criando forma do usuario fazer login (Usuario e Senha)
LoginLabel = Label(text = "Usuario: ", font = ("Century Gothic", 20), bg = "#f6f3ec", fg = "Black") 
LoginLabel.place(x = 45, y = 80) 
LoginEntry = ttk.Entry(width = 30)  
LoginEntry.place(x = 155, y = 94)

SenhaLabel = Label(text = "Senha: ", font = ("Century Gothic", 20 ), bg = "#f6f3ec", fg = "Black") 
SenhaLabel.place(x = 57, y = 125)
SenhaEntry = ttk.Entry(width = 30, show = "•") 
SenhaEntry.place(x = 155, y = 140)

#Fazer login
def FazerLogin():

    usuario = LoginEntry.get()
    senha = SenhaEntry.get()

    db = login() 
    db.cursor.execute("""SELECT * FROM usuario WHERE nome = %s AND senha = %s""", (usuario, senha))
    VerifyLogin = db.cursor.fetchone()

    if VerifyLogin:
        messagebox.showinfo(title = "INFO LOGIN", message = "Acesso Confirmado, Bem Vindo!")
    else:
        messagebox.showinfo(title = "INFO LOGIN", message = "Acesso Negado. Verifique se esta cadastrado no sistema!")

LoginButton = ttk.Button(text = "LOGIN", width = 15, command = FazerLogin)
LoginButton.place(x = 130, y = 335)

#Registrar um novo usuario
def registrar():

    LoginButton.place(x = 5000)

    EnderecoLabel = Label(text = "Endereço: ", font = ("Century Gothic", 20), bg = "#f6f3ec", fg = "Black") 
    EnderecoLabel.place(x = 10, y = 165)
    EnderecoEntry = ttk.Entry(width = 30)  
    EnderecoEntry.place(x = 155, y = 178) 

    TelefoneLabel = Label(text = "Telefone: ", font = ("Century Gothic", 20), bg = "#f6f3ec", fg = "Black")
    TelefoneLabel.place(x = 25, y = 210) 
    TelefoneEntry = ttk.Entry(width = 30)  
    TelefoneEntry.place(x = 155, y = 225) 

    #Codigo para registrar o usuario no banco
    def RegistrarNoBanco():
        nome = LoginEntry.get()
        senha = SenhaEntry.get()
        endereco = EnderecoEntry.get()
        telefone = TelefoneEntry.get()

        #Mensagem de erro se apertar o botao 'Registrar' sem digitar nada nos campos de textos 
        if nome == "" or senha == "" or endereco == "" or telefone == "":
            messagebox.showerror(title = "Erro de Registro", message = "PREENCHA TODOS OS CAMPOS") 
        else:
            db = login() 
            db.RegistrarNoBanco(nome, endereco, telefone, senha) 
            messagebox.showinfo("Sucesso", "Usuario registrado com sucesso!")

            
            LoginEntry.delete(0, END) 
            SenhaEntry.delete(0, END) 
            EnderecoEntry.delete(0, END) 
            TelefoneEntry.delete(0, END)

    Register = ttk.Button(text = "REGISTRAR", width = 15, command = RegistrarNoBanco) 
    Register.place(x = 240, y = 335)

    #Para voltar para login
    def VoltarLogin():
        EnderecoLabel.place(x = 5000) 
        EnderecoEntry.place(x = 5000) 
        TelefoneLabel.place(x = 5000) 
        TelefoneEntry.place(x = 5000) 
        Register.place(x = 5000) 
        Voltar.place(x = 5000) 
        
        LoginButton.place(x = 130, y = 335) 
        RegisterButton.place(x = 240, y = 335) 

    Voltar = ttk.Button(text = "VOLTAR", width = 15, command = VoltarLogin) 
    Voltar.place(x = 130, y = 335) 
RegisterButton = ttk.Button(text = "REGISTRAR", width = 15, command = registrar) 
RegisterButton.place(x = 240, y = 335) 

jan.mainloop()