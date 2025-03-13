from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from comunicacao import comunicacao

class FornecedorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fornecedor")
        self.root.geometry("400x600")
        self.root.configure(background="#f6f3ec")
        self.root.resizable(width=False, height=False)

        self.cadButton = ttk.Button(root, text="Cadastrar Fornecedor", width=50, command=self.cadastro_forn)
        self.cadButton.place(x=45, y=200)

        self.excnButton = ttk.Button(root, text="Excluir Fornecedor", width=50, command=self.excluir_forn)
        self.excnButton.place(x=45, y=300)

        self.listButton = ttk.Button(root, text="Listar Fornecedor", width=50, command=self.listar_forn)
        self.listButton.place(x=45, y=400)

        self.atuButton = ttk.Button(root, text="Atualizar Fornecedor", width=50, command=self.atuu_funci)
        self.atuButton.place(x=45, y=500)

        self.voltButton = ttk.Button(root, text="Fechar", width=10, command=self.sair)
        self.voltButton.place(x=10, y=570)
        
        Titulolabel = Label(self.root, text="GERENCIADOR DE FORNECEDORES", font=("Times New Roman", 18))
        Titulolabel.place(x=10, y=75)

    def cadastro_forn(self):
        jan = Toplevel(self.root)
        jan.title("Cadastro de Fornecedores")
        jan.geometry("800x600")
        jan.configure(background="#f6f3ec")
        jan.resizable(width=False, height=False)

        forlabel = Label(jan, text="NOME EMPRESARIAL: ", font=("Times New Roman", 15))
        forlabel.place(x=115, y=55)
        self.fornomeEntry = ttk.Entry(jan, width=30)
        self.fornomeEntry.place(x=330, y=60)

        fornecedores_ficticio = Label(jan, text="NOME DE FANTASIA: ", font=("Times New Roman", 15))
        fornecedores_ficticio.place(x=115, y=150)
        self.ficticioEntry = ttk.Entry(jan, width=40)
        self.ficticioEntry.place(x=330, y=160)

        fornecedores_cnpj = Label(jan, text="CNPJ DA EMPRESA: ", font=("Times New Roman", 15))
        fornecedores_cnpj.place(x=115, y=255)
        self.cnpjEntry = ttk.Entry(jan, width=40)
        self.cnpjEntry.place(x=330, y=260)

        fornecedores_END = Label(jan, text="ENDEREÇO DA EMPRESA: ", font=("Times New Roman", 15))
        fornecedores_END.place(x=85, y=350)
        self.endEntry = ttk.Entry(jan, width=40)
        self.endEntry.place(x=330, y=360)

        AddButton = ttk.Button(jan, text="REGISTRAR FORNECEDOR", width=30, command=self.RegistrarNoBanco)
        AddButton.place(x=300, y=520)

        voltButton = ttk.Button(jan, text="Fechar", width=10, command=jan.destroy)
        voltButton.place(x=10, y=570)

    def RegistrarNoBanco(self):
        nomeforn = self.fornomeEntry.get()
        nomefant = self.ficticioEntry.get()
        cnpj = self.cnpjEntry.get()
        end = self.endEntry.get()
        db = comunicacao()
        db.RegistrarFornecedor(nomeforn, nomefant, cnpj, end)
        if nomeforn == "" or nomefant == "" or cnpj == "" or cnpj == "" or end == "":
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
        else:
            messagebox.showinfo("Sucesso", "Fornecedor registrado com sucesso!")
            self.limpar_campos()
    def limpar_campos(self):
        self.fornomeEntry.delete(0, END)  # Limpa o campo NOME EMPRESARIAL
        self.ficticioEntry.delete(0, END)  # Limpa o campo NOME DE FANTASIA
        self.cnpjEntry.delete(0, END)  # Limpa o campo CNPJ
        self.endEntry.delete(0, END)  # Limpa o campo ENDEREÇO
    def excluir_forn(self):
        def excluir_selecionado():
            item_selecionado = tree.selection()
            if not item_selecionado:
                messagebox.showwarning("Atenção", "Selecione um fornecedor para excluir.")
                return

            fornecedor_id = tree.item(item_selecionado)["values"][0]

            resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este fornecedor?")
            if resposta:
                db = comunicacao()
                db.ExcluirFornecedor(fornecedor_id)
                self.carregar_fornecedores(tree)  # Atualiza a treeview após a exclusão
                messagebox.showinfo("Sucesso", "Fornecedor excluído com sucesso!")

        janela = Toplevel(self.root)
        janela.title("Excluir Fornecedores")
        janela.geometry("700x400")
        janela.configure(background="#f6f3ec")
        janela.resizable(width=False, height=False)

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

        bt_excluir = ttk.Button(janela, text="Excluir Selecionado", command=excluir_selecionado)
        bt_excluir.pack(pady=5)

        bt_fechar = ttk.Button(janela, text="Fechar", width=10, command=janela.destroy)
        bt_fechar.pack(pady=5)

        # Carrega os fornecedores na treeview
        self.carregar_fornecedores(tree)

    def carregar_fornecedores(self, tree):
        # Limpa a treeview antes de carregar novos dados
        for item in tree.get_children():
            tree.delete(item)

        # Obtém os dados dos fornecedores do banco de dados
        db = comunicacao()
        cursor = db.conn.cursor()  # Cria um novo cursor

        
        cursor.execute("SELECT idfornecedor, nome, nomefantasia, CNPJ, endereco FROM fornecedor")
        fornecedores = cursor.fetchall()  # Consome todos os resultados

            # Insere os fornecedores na treeview
        for fornecedor in fornecedores:
            tree.insert("", "end", values=fornecedor)


    def listar_forn(self):
        janela = Toplevel(self.root)
        janela.title("Listar Fornecedores")
        janela.geometry("700x400")
        janela.configure(background="#f6f3ec")
        janela.resizable(width=False, height=False)

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

        bt_fechar = ttk.Button(janela, text="Fechar", width=10, command=janela.destroy)
        bt_fechar.pack(pady=5)

        # Carrega os fornecedores na treeview
        self.carregar_fornecedores(tree)

    def atuu_funci(self):
        jan = Toplevel(self.root)
        jan.title("Atualizar Fornecedores")
        jan.geometry("800x600")
        jan.configure(background="#f6f3ec")
        jan.resizable(width=False, height=False)

        # Campo para inserir o ID do fornecedor
        id_label = Label(jan, text="ID DO FORNECEDOR: ", font=("Times New Roman", 15))
        id_label.place(x=115, y=55)
        self.idEntry = ttk.Entry(jan, width=30)
        self.idEntry.place(x=330, y=60)

        # Botão para buscar o fornecedor
        buscar_button = ttk.Button(jan, text="Buscar Fornecedor", width=20, command=self.buscar_fornecedor)
        buscar_button.place(x=330, y=100)

        # Campos para editar as informações do fornecedor
        forlabel = Label(jan, text="NOME EMPRESARIAL: ", font=("Times New Roman", 15))
        forlabel.place(x=115, y=150)
        self.fornomeEntry = ttk.Entry(jan, width=30)
        self.fornomeEntry.place(x=330, y=155)

        fornecedores_ficticio = Label(jan, text="NOME DE FANTASIA: ", font=("Times New Roman", 15))
        fornecedores_ficticio.place(x=115, y=200)
        self.ficticioEntry = ttk.Entry(jan, width=40)
        self.ficticioEntry.place(x=330, y=205)

        fornecedores_cnpj = Label(jan, text="CNPJ DA EMPRESA: ", font=("Times New Roman", 15))
        fornecedores_cnpj.place(x=115, y=250)
        self.cnpjEntry = ttk.Entry(jan, width=40)
        self.cnpjEntry.place(x=330, y=255)

        fornecedores_END = Label(jan, text="ENDEREÇO DA EMPRESA: ", font=("Times New Roman", 15))
        fornecedores_END.place(x=85, y=300)
        self.endEntry = ttk.Entry(jan, width=40)
        self.endEntry.place(x=330, y=305)

        # Botão para salvar as alterações
        salvar_button = ttk.Button(jan, text="Salvar Alterações", width=20, command=self.salvar_alteracoes)
        salvar_button.place(x=330, y=350)

    def buscar_fornecedor(self):
        idfornecedor = self.idEntry.get()
        if not idfornecedor:
            messagebox.showwarning("Atenção", "Por favor, insira o ID do fornecedor.")
            return

        db = comunicacao()
        fornecedor = db.buscar_fornecedor_por_id(idfornecedor)

        if not fornecedor:
            messagebox.showerror("Erro", "Fornecedor não encontrado.")
            return

        # Preenche os campos com as informações do fornecedor
        self.fornomeEntry.delete(0, END)
        self.fornomeEntry.insert(0, fornecedor[1])  # Nome empresarial

        self.ficticioEntry.delete(0, END)
        self.ficticioEntry.insert(0, fornecedor[2])  # Nome fantasia

        self.cnpjEntry.delete(0, END)
        self.cnpjEntry.insert(0, fornecedor[3])  # CNPJ

        self.endEntry.delete(0, END)
        self.endEntry.insert(0, fornecedor[4])  # Endereço

    def salvar_alteracoes(self):
        idfornecedor = self.idEntry.get()
        nomeforn = self.fornomeEntry.get()
        nomefant = self.ficticioEntry.get()
        cnpj = self.cnpjEntry.get()
        end = self.endEntry.get()

        if not idfornecedor:
            messagebox.showwarning("Atenção", "Por favor, insira o ID do fornecedor.")
            return

        if nomeforn == "" or nomefant == "" or cnpj == "" or end == "":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        db = comunicacao()
        db.AtualizarFornecedor(idfornecedor, nomeforn, nomefant, cnpj, end)
        messagebox.showinfo("Sucesso", "Fornecedor atualizado com sucesso!")
    def sair(self):
        from MenuAdm import TelaLoginCadastro
        TelaLoginCadastro(self.root)


root = Tk()
app = FornecedorApp(root)
root.mainloop()