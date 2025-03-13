
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from comunicacao import comunicacao

class GerenciadorFuncionarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Funcionarios")
        self.root.geometry("400x600")
        self.root.configure(background="#f6f3ec")
        self.root.resizable(width=False, height=False)

        self.criar_widgets()

    def criar_widgets(self):
        # Título
        Titulolabel = tk.Label(self.root, text="GERENCIADOR DE FUNCIONARIOS", font=("Times New Roman", 18))
        Titulolabel.place(x=10, y=75)

        # Botões 
        cadButton = ttk.Button(self.root, text="Cadastrar Funcionario", width=50, command=self.cadastro_func)
        cadButton.place(x=45, y=200)

        excnButton = ttk.Button(self.root, text="Excluir Funcionario", width=50, command=self.excluir_func)
        excnButton.place(x=45, y=300)

        listButton = ttk.Button(self.root, text="Listar Funcionario", width=50, command=self.listar_func)
        listButton.place(x=45, y=400)

        atuButton = ttk.Button(self.root, text="Atualizar Funcionario", width=50, command=self.atuu_func)
        atuButton.place(x=45, y=500)

        voltButton = ttk.Button(self.root, text="Fechar", width=10, command=self.sair)
        voltButton.place(x=10, y=570)

    def cadastro_func(self):
        jan_cadastro = tk.Toplevel(self.root)
        jan_cadastro.title("Cadastro de Funcionarios")
        jan_cadastro.geometry("800x600")
        jan_cadastro.configure(background="#f6f3ec")
        jan_cadastro.resizable(width=False, height=False)

        # Campos de entrada
        tk.Label(jan_cadastro, text="Nome:", font=("Times New Roman", 20)).place(x=115, y=50)
        self.UsuarioEntry = ttk.Entry(jan_cadastro, width=40)
        self.UsuarioEntry.place(x=210, y=60)

        tk.Label(jan_cadastro, text="Telefone:", font=("Times New Roman", 20)).place(x=115, y=120)
        self.TelefoneEntry = ttk.Entry(jan_cadastro, width=40)
        self.TelefoneEntry.place(x=240, y=130)

        tk.Label(jan_cadastro, text="Endereço:", font=("Times New Roman", 20)).place(x=115, y=190)
        self.EnderecoEntry = ttk.Entry(jan_cadastro, width=40)
        self.EnderecoEntry.place(x=240, y=200)

        tk.Label(jan_cadastro, text="Email:", font=("Times New Roman", 20)).place(x=115, y=260)
        self.EmailEntry = ttk.Entry(jan_cadastro, width=40)
        self.EmailEntry.place(x=200, y=270)

        tk.Label(jan_cadastro, text="Data de Nascimento:", font=("Times New Roman", 20)).place(x=115, y=330)
        self.NascEntry = ttk.Entry(jan_cadastro, width=40)
        self.NascEntry.place(x=350, y=340)

        # Botões
        ttk.Button(jan_cadastro, text="REGISTRAR FUNCIONARIO", width=30, command=self.RegistrarFuncionario).place(x=300, y=520)
        ttk.Button(jan_cadastro, text="Fechar", width=10, command=jan_cadastro.destroy).place(x=10, y=570)

    def RegistrarFuncionario(self):
        nome = self.UsuarioEntry.get()
        telefone = self.TelefoneEntry.get()
        enderecofunc = self.EnderecoEntry.get()
        email = self.EmailEntry.get()
        data_nascimento = self.NascEntry.get()

        if nome == "" or telefone == "" or enderecofunc == "" or email == "" or data_nascimento == "":
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
        else:
            db = comunicacao()
            db.RegistrarFuncionario(nome, telefone, enderecofunc, email, data_nascimento)
            messagebox.showinfo("Success", "Usuario criado com sucesso!")





    def listar_func(self):
        def listar_selecionado():
            item_selecionado = tree.selection()
            if not item_selecionado:
                messagebox.showwarning("Atenção", "Selecione um Funcionario para procurar.")
                return

            funcionario_id = tree.item(item_selecionado)["values"][0]

            resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja procurar este funcionario ?")
            if resposta:
                db = comunicacao()
                db.ExcluirFuncionario(funcionario_id)
                self.carregar_funcionarios(tree)  # Atualiza a treeview após a exclusão
                messagebox.showinfo("Sucesso", "Funcionario achado com sucesso!")


        def carregar_funcionarios():
            item_selecionado = tree.selection()
            if not item_selecionado:
                messagebox.showwarning("Atenção", "Selocione um funcionario para procurar.")
                return

            funcionario_id = tree.item(item_selecionado)["values"][0]

            resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja procurar este funcionario?")
            if resposta:
                db = comunicacao()
                db.ListarFuncionario()
                self.carregar_funcionarios()

                carregar_funcionarios()
                messagebox.showinfo("Sucesso", "Funcionario achado com sucesso!")

        janela = Toplevel(self.root)
        janela.title("Listar Fornecedores")
        janela.geometry("700x400")
        janela.configure(background="#f6f3ec")
        janela.resizable(width=False, height=False)

        colunas = ("ID", "Nome", "Telefone", "Endereço", "Email" "Data de Nascimento")
        tree = ttk.Treeview(janela, columns=colunas, show="headings")

        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.heading("Telefone", text="Telefone")
        tree.heading("Endereço", text="Endereço")
        tree.heading("Email", text="Email")
        tree.heading("Data de Nascimento", text="Endereço")

        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=150)
        tree.column("Telefone ", width=150)
        tree.column("Endereço", width=120, anchor="center")
        tree.column("Email ", width=180)
        tree.column("Data de Nascimento", width=200)

        tree.pack(pady=10, padx=10, fill=BOTH, expand=True)

        bt_fechar = ttk.Button(janela, text="Fechar", width=10, command=janela.destroy)
        bt_fechar.pack(pady=5)

        carregar_funcionarios()
       

        
    def atuu_func(self):
        jan_atualizar = tk.Toplevel(self.root)
        jan_atualizar.title("Atualizar Funcionarios")
        jan_atualizar.geometry("400x600")
        jan_atualizar.configure(background="#f6f3ec")
        jan_atualizar.resizable(width=False, height=False)

    def excluir_func(self):
        def excluir_selecionado():
            item_selecionado = tree.selection()
            if not item_selecionado:
                messagebox.showwarning("Atenção", "Selecione um Funcionario para excluir.")
                return

            idfuncionario = tree.item(item_selecionado)["values"][0]
            

            resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este funcionario ?")
            if resposta:
                db = comunicacao()
                try:
                    db.ExcluirFuncionario(idfuncionario)
                    self.carregar_funcionarios(tree)  # Atualiza a treeview após a exclusão
                    messagebox.showinfo("Sucesso", "Funcionario excluído !")
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao excluir funcionário: {e}")

        jan_excluir = tk.Toplevel(self.root)
        jan_excluir.title("Excluir Funcionarios")
        jan_excluir.geometry("700x400")
        jan_excluir.configure(background="#f6f3ec")
        jan_excluir.resizable(width=False, height=False)

        # Tabela (Treeview)
        colunas = ("ID", "Nome", "Telefone", "Endereco", "Email", "Data de nascimento")
        tree = ttk.Treeview(jan_excluir, columns=colunas, show="headings")
        for col in colunas:
            tree.heading(col, text=col)
        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=150)
        tree.column("Telefone", width=150)
        tree.column("Endereco", width=120, anchor="center")
        tree.column("Email", width=150)
        tree.column("data_nascimento", width=200)
        tree.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Botões
        bt_excluir = ttk.Button(jan_excluir, text="Excluir Selecionado", command=excluir_selecionado)
        bt_excluir.pack(pady=5)
        
        bt_fechar = ttk.Button(jan_excluir, text="Fechar", width=10, command=jan_excluir.destroy)
        bt_fechar.pack(pady=5)

        # Carregar funcionários na tabela
        self.carregar_funcionarios(tree)
    
    def carregar_funcionarios(self, tree):
        # Limpa a treeview antes de carregar novos dados
        for item in tree.get_children():
            tree.delete(item)

        # Obtém os dados dos fornecedores do banco de dados
        db = comunicacao()
        cursor = db.conn.cursor()  # Cria um novo cursor

        try:
            cursor.execute("SELECT idfuncionario, nome, telefone, enderecofunc, email, datanascimento FROM funcionario")
            funcionarios = cursor.fetchall()  # Consome todos os resultados

            # Insere os fornecedores na treeview
            for funcionario in funcionarios:
                tree.insert("", "end", values=funcionario)
        finally:
            cursor.close()  # Fecha o cursor após o uso


    def sair(self):
        self.root.destroy()



root = tk.Tk()
app = GerenciadorFuncionarios(root)
root.mainloop()



























