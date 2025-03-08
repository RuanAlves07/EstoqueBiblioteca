from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

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
    UsuarioEntry.place (x = 210, y = 60)

    TelefoneLabel =  Label(jan, text="Telefone:", font=("Times New Roman", 20))
    TelefoneLabel.place(x = 115, y = 120)
    TelefoneEntry = ttk.Entry(jan, width=40) # Criar um campo de entrada para o telefone
    TelefoneEntry.place (x = 240, y = 130)

    EnderecoLabel =  Label(jan, text="Endereço:", font=("Times New Roman", 20))
    EnderecoLabel.place(x = 115, y = 190)
    EnderecoEntry = ttk.Entry(jan, width=40) # Criar um campo de entrada para o endereço
    EnderecoEntry.place (x = 240, y = 200)

    EmailLabel =  Label(jan, text="Email:", font=("Times New Roman", 20))
    EmailLabel.place(x = 115, y = 260)
    EmailEntry = ttk.Entry(jan, width=40) # Criar um campo de entrada para o email
    EmailEntry.place (x = 200, y = 270)

    NascLabel =  Label(jan, text="Data de Nascimento:", font=("Times New Roman", 20))
    NascLabel.place(x = 115, y = 330)
    NascEntry = ttk.Entry(jan, width=40) # Criar um campo de entrada para o email
    NascEntry.place (x = 350, y = 340)



    def testebanco():
        
        nome = UsuarioEntry.get()
        telefone = TelefoneEntry.get()
        enderecofunc = EnderecoEntry.get()
        email = EmailEntry.get()
        data_nascimento = NascEntry.get()

        conn = conectar_banco()
        cursor = conn.cursor()
        query = ("insert funcionario (nome, telefone, enderecofunc, email, datanascimento) VALUES (%s, %s, %s, %s, %s)")
        cursor.execute(query, (nome, telefone, enderecofunc, email,  data_nascimento))#Insere os dados do usuário na tabela
        conn.commit() # Confirma a inserção dos dados
        cursor.close()
        conn.close()

        if nome == "" or telefone == "" or enderecofunc == "" or email == "" or data_nascimento == "":
                messagebox.showerror(title="Erro no Registro",message="PREENCHA TODOS OS CAMPOS") # Exibe mensagm de erro
        else:
                messagebox.showinfo("Sucesso","Funcionario registrado com sucesso!") # Exibe mensagem de Sucesso


    AddButton = ttk.Button(jan, text = "REGISTRAR FUNCIONARIO", width = 30, command=testebanco) # Cria um botão para registrar 
    AddButton.place(x = 300, y = 520)

    voltButton = ttk.Button(jan, text = "Fechar", width = 10,command=jan.withdraw) # Cria um botão para voltar 
    voltButton.place(x = 10, y = 570)

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",  # Alterar se o MySQL estiver em outro servidor
        user="root",  # Seu usuário do MySQL
        password="",  # Sua senha do MySQL
        database="biblioteca_db"  # Nome do banco de dados
    )
    

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

def excluir_func():    

     # Função para carregar fornecedores na tabela
    def carregar_funcionarios():
        # Limpa a tabela antes de carregar novos dados
        for item in tree.get_children():
            tree.delete(item)

        # Conectar ao MySQL
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT idfuncionario, nome, telefone, enderecofunc, email, data_nascimento FROM funcionario")
        funcionarios = cursor.fetchall()
        conn.close()

        # Adicionar os funcionarios na tabela (Treeview)
        for funcionario in funcionarios:
            tree.insert("", "end", values=funcionario)
        

     # Função para excluir o funcionario selecionado
    def excluir_selecionado2():
        item_selecionado = tree.selection()
        if not item_selecionado:
            messagebox.showwarning("Atenção", "Selecione um funcionario para excluir.")
            return

        funcionario_id = tree.item(item_selecionado)["values"][0]

        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este fornecedor?")
        if resposta:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM funcionario WHERE idfuncionario = %s", (funcionario_id))
            conn.commit()
            conn.close()

            carregar_funcionarios()
            messagebox.showinfo("Sucesso", "Funcionario excluído com sucesso!")

    jan = Tk()
    jan.title("Excluir Fornecedores")
    jan.geometry("700x400")
    jan.configure(background="#f6f3ec")
    jan.resizable(width=False, height=False)
     # Criar a tabela (Treeview) para exibir os funcionarios
    colunas = ("ID", "Nome", "Telefone", "Endereco", "Email", "data_nascimento")
    tree = ttk.Treeview(jan, columns=colunas, show="headings")

    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Telefone", text="Telefone")
    tree.heading("Endereco", text="Endereco")
    tree.heading("Email", text="Email")
    tree.heading("data_nascimento", text="data_nascimento")

    tree.column("ID", width=50, anchor="center")
    tree.column("Nome", width=150)
    tree.column("Telefone", width=150)
    tree.column("Endereco", width=120, anchor="center")
    tree.column("Email", width=150)
    tree.column("data_nascimento", width=200)

    tree.pack(pady=10, padx=10, fill=BOTH, expand=True)

    # Criar botão para excluir funcionario
    bt_excluir = ttk.Button(jan, text="Excluir Selecionado", command=excluir_selecionado2)
    bt_excluir.pack(pady=5)

    # Criar botão para fechar a janela
    bt_fechar = ttk.Button(jan, text="Fechar", width=10, command=jan.destroy)
    bt_fechar.pack(pady=5)

    carregar_funcionarios()        

def sair():
    jan.withdraw()



Titulolabel = Label(text = "GERENCIADOR DE FUNCiONARIOS", font =("Times New Roman", 18))
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

