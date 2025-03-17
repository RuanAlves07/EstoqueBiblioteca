from tkinter import * 
from tkinter import messagebox 
from tkinter import ttk 
from comunicacao import comunicacao

class TelaLoginCadastro:
    def __init__(self):
        # Criação da tela
        self.root = Tk()
        self.root.title("Tela de login e cadastro")
        self.root.geometry("400x300")
        self.root.configure(background="#f6f3ec")
        self.root.resizable(width=False, height=False)

        self.BemvindoLabel = Label(self.root, text="Seja Bem-vindo(a)!", font=("Times New Roman", 20), bg="#f6f3ec", fg="Black")
        self.BemvindoLabel.place(x=90, y=30)

        # Criando forma do usuário fazer login (Usuário e Senha)
        self.LoginLabel = Label(self.root, text="Usuario: ", font=("Times New Roman", 20), bg="#f6f3ec", fg="Black")
        self.LoginLabel.place(x=45, y=83)
        self.LoginEntry = ttk.Entry(self.root, width=30)
        self.LoginEntry.place(x=155, y=94)

        self.SenhaLabel = Label(self.root, text="Senha: ", font=("Times New Roman", 20), bg="#f6f3ec", fg="Black")
        self.SenhaLabel.place(x=57, y=130)
        self.SenhaEntry = ttk.Entry(self.root, width=30, show="•")
        self.SenhaEntry.place(x=155, y=140)

        # Botão de login
        self.LoginButton = ttk.Button(self.root, text="LOGIN", width=15, command=self.FazerLogin)
        self.LoginButton.place(x=170, y=235)

        # Iniciar a janela
        self.root.mainloop()

    # Def para fazer login
    def FazerLogin(self):
    nome = self.LoginEntry.get()
    senha = self.SenhaEntry.get()

    db = comunicacao() 
    db.cursor.execute("SELECT * FROM login WHERE nome = %s AND senha = %s", (nome, senha))
    VerifyLogin = db.cursor.fetchone()

    if VerifyLogin:
        messagebox.showinfo(title="INFO LOGIN", message="Acesso Confirmado, Bem Vindo!")
        self.root.destroy()

        adm = VerifyLogin[0]

        if adm == 1:
            from MenuAdm import Menuadm
            root_menu = Tk()  
            Menuadm(root_menu)
            root_menu.mainloop()

        else:
            from MenuUsuario import MenuU
            root_menu = Tk() 
            MenuU(root_menu)
            root_menu.mainloop()
    else:
        messagebox.showinfo(title="INFO LOGIN", message="Acesso Negado. Verifique se está cadastrado no sistema!")


if __name__ == "__main__":
    app = TelaLoginCadastro()