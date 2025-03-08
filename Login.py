from tkinter import * 
from tkinter import messagebox 
from tkinter import ttk 
from comunicacao import login


#Banco de dados
""" class login:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "biblioteca_db"
        )mast
        self.cursor = self.conn.cursor()  """
#Criação da tela
jan = Tk() 
jan.title("Tela de login e cadastro") 
jan.geometry("400x300") 
jan.configure(background = "#f6f3ec") 
jan.resizable(width = False, height = False) 



#Criando forma do usuario fazer login (Usuario e Senha)
LoginLabel = Label(text = "Usuario: ", font = ("Times New Roman", 20), bg = "#f6f3ec", fg = "Black") 
LoginLabel.place(x = 45, y = 83) 
LoginEntry = ttk.Entry(width = 30)  
LoginEntry.place(x = 155, y = 94)

SenhaLabel = Label(text = "Senha: ", font = ("Times New Roman", 20 ), bg = "#f6f3ec", fg = "Black") 
SenhaLabel.place(x = 57, y = 130)
SenhaEntry = ttk.Entry(width = 30, show = "•") 
SenhaEntry.place(x = 155, y = 140)
#sou gay
#Fazer login
def FazerLogin():

    nome = LoginEntry.get()
    senha = SenhaEntry.get()

    db = login() 
    db.cursor.execute("""SELECT * FROM usuario WHERE nome = %s AND senha = %s""", (nome, senha))
    VerifyLogin = db.cursor.fetchone()

    if VerifyLogin:
        messagebox.showinfo(title = "INFO LOGIN", message = "Acesso Confirmado, Bem Vindo!")
        from Menu import TelaLoginCadastro
        TelaLoginCadastro()

    else:
        messagebox.showinfo(title = "INFO LOGIN", message = "Acesso Negado. Verifique se esta cadastrado no sistema!")

LoginButton = ttk.Button(text = "LOGIN", width = 15, command = FazerLogin)
LoginButton.place(x = 170, y = 235)



jan.mainloop()