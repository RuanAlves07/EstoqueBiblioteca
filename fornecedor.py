from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
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
        db.RegistrarFornecedor(nomeforn,nomefant,cnpj,end)
        if nomeforn == "" or nomefant == "" or cnpj == "" or cnpj == "" or end == "":
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
        else:
            messagebox.showinfo("Sucesso", "Fornecedor registrado com sucesso!")



    def excluir_forn(self):
        def carregar_fornecedores():
            for item in tree.get_children():
                tree.delete(item)

            conn = self.conectar_banco()
            cursor = conn.cursor()
            cursor.execute("SELECT idfornecedor, nome, nomefantasia, CNPJ, endereco FROM fornecedor")
            fornecedores = cursor.fetchall()
            conn.close()

            for fornecedor in fornecedores:
                tree.insert("", "end", values=fornecedor)

        def excluir_selecionado():
            item_selecionado = tree.selection()
            if not item_selecionado:
                messagebox.showwarning("Atenção", "Selecione um fornecedor para excluir.")
                return

            fornecedor_id = tree.item(item_selecionado)["values"][0]

            resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este fornecedor?")
            if resposta:
                db = comunicacao()
                db.ExcluirFornecedor()
                self.carregar_fornecedores()

                carregar_fornecedores()
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

        carregar_fornecedores()

    def listar_forn(self):
        def carregar_fornecedores():
            for item in tree.get_children():
                tree.delete(item)

            conn = self.conectar_banco()
            cursor = conn.cursor()
            cursor.execute("SELECT idfornecedor, nome, nomefantasia, CNPJ, endereco FROM fornecedor")
            fornecedores = cursor.fetchall()
            conn.close()

            for fornecedor in fornecedores:
                tree.insert("", "end", values=fornecedor)

        def excluir_selecionado():
            item_selecionado = tree.selection()
            if not item_selecionado:
                messagebox.showwarning("Atenção", "Selecione um fornecedor para excluir.")
                return

            fornecedor_id = tree.item(item_selecionado)["values"][0]

            resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir este fornecedor?")
            if resposta:
                db = comunicacao()
                db.ExcluirFornecedor()
                self.carregar_fornecedores()

                carregar_fornecedores()
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

        bt_fechar = ttk.Button(janela, text="Fechar", width=10, command=janela.destroy)
        bt_fechar.pack(pady=5)

        carregar_fornecedores()

    def atuu_funci(self):
        jan = Toplevel(self.root)
        jan.title("Atualizar Fornecedores")
        jan.geometry("400x600")
        jan.configure(background="#f6f3ec")
        jan.resizable(width=False, height=False)

        voltButton = ttk.Button(jan, text="Fechar", width=10, command=jan.destroy)
        voltButton.place(x=10, y=570)

    def sair(self):
        self.root.destroy()
        from Menu import TelaLoginCadastro
        TelaLoginCadastro(self.root)

if __name__ == "__main__":
    root = Tk()
    app = FornecedorApp(root)
    root.mainloop()