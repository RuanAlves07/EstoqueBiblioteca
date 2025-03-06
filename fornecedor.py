from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

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


def conectar_banco():
    return mysql.connector.connect(
        host="localhost",  # Alterar se o MySQL estiver em outro servidor
        user="root",  # Seu usuário do MySQL
        password="root",  # Sua senha do MySQL
        database="biblioteca_db"  # Nome do banco de dados
    )

def excluir_forn():
    # Função para carregar fornecedores na tabela
    def carregar_fornecedores():
        # Limpa a tabela antes de carregar novos dados
        for item in tree.get_children():
            tree.delete(item)

        # Conectar ao MySQL
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, nomefantasia, cnpj, endereco FROM fornecedor")
        fornecedores = cursor.fetchall()
        conn.close()

        # Adicionar os fornecedores na tabela (Treeview)
        for fornecedor in fornecedores:
            tree.insert("", "end", values=fornecedor)

    # Função para excluir o fornecedor selecionado
    def excluir_selecionado():
        item_selecionado = tree.selection()
        if not item_selecionado:
            messagebox.showwarning("Atenção", "Selecione um fornecedor para excluir.")
            return

        fornecedor_id = tree.item(item_selecionado)["values"][0]

        resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este fornecedor?")
        if resposta:
            conn = conectar_banco()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM fornecedor WHERE id = %s", (fornecedor_id,))
            conn.commit()
            conn.close()

            carregar_fornecedores()
            messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso!")

    # Criar a janela principal
    janela = Tk()
    janela.title("Excluir Fornecedores")
    janela.geometry("700x400")
    janela.configure(background="#f6f3ec")
    janela.resizable(width=False, height=False)

    # Criar a tabela (Treeview) para exibir os fornecedores
    colunas = ("ID", "Nome", "Nome Fantasia", "CNPJ", "Endereço")
    tree = ttk.Treeview(janela, columns=colunas, show="headings")

    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Nome Fantasia", text="Nome Fantasia")
    tree.heading("CNPJ", text="CNPJ")
    tree.heading("Endereço", text="Endereço")

    tree.column("ID", width=50, anchor="center")
    tree.column("Nome", width=150)
    tree.column("Nome Fantasia", width=150)
    tree.column("CNPJ", width=120, anchor="center")
    tree.column("Endereço", width=200)

    tree.pack(pady=10, padx=10, fill=BOTH, expand=True)

    # Criar botão para excluir fornecedor
    btn_excluir = ttk.Button(janela, text="Excluir Selecionado", command=excluir_selecionado)
    btn_excluir.pack(pady=5)

    # Criar botão para fechar a janela
    btn_fechar = ttk.Button(janela, text="Fechar", width=10, command=janela.destroy)
    btn_fechar.pack(pady=5)

    carregar_fornecedores()


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

    voltButton = ttk.Button(jan, text = "Fechar", width = 10,command=jan.withdraw) # Cria um botão e faz maluquise
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

voltButton = ttk.Button( text = "Fechar", width = 10,command=sair) # Cria um botão gay
voltButton.place(x = 10, y = 570) # Posiciona o botão 


jan.mainloop()