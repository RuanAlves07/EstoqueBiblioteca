import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import mysql.connector
from comunicacao import comunicacao  
from CTkMenuBar import *


class GerenciadorFuncionarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Funcionários")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f6f6f6")  


        # Configuração do tema
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")

        BarraNavegabilidade = CTkMenuBar(root)
        botao_1 = BarraNavegabilidade.add_cascade("Produtos", command = self.GoToproduto)
        botao_2 = BarraNavegabilidade.add_cascade("Fornecedores", command = self.TelaFornecedores)
        botao_3 = BarraNavegabilidade.add_cascade("Funcionarios", command = self.TelaFuncionarios)
        botao_4 = BarraNavegabilidade.add_cascade("Clientes", command = self.TelaClientes)

     # Título
        Titulolabel = ctk.CTkLabel(self.root, text="GERENCIADOR DE FUNCIONÁRIOS",
        font=("Poppins", 22, "bold"))
        Titulolabel.pack(pady=70)

        # Botões principais
        self.cadButton = ctk.CTkButton(self.root, text="Cadastrar Funcionario", width=300, command=self.cadastro_func)
        self.cadButton.place(x=250, y=200)

        self.excnButton = ctk.CTkButton(self.root, text="Excluir Funcionario", width=300, command=self.excluir_func)
        self.excnButton.place(x=250, y=300)

        self.listButton = ctk.CTkButton(self.root, text="Listar Funcionario", width=300, command=self.listar_func)
        self.listButton.place(x=250, y=500)

        self.atuButton = ctk.CTkButton(self.root, text="Atualizar Funcionario", width=300, command=self.atuu_func)
        self.atuButton.place(x=250, y=400)


    def GoToproduto(self):
        from produto import TelaProdutos
        nova_janela = ctk.CTkToplevel(self.root)
        nova_janela.grab_set()       
        nova_janela.focus_force()    
        TelaProdutos(nova_janela)

    def TelaFornecedores(self):
        from fornecedor import FornecedorApp
        nova_janela = ctk.CTkToplevel(self.root)
        nova_janela.grab_set()
        nova_janela.focus_force()
        FornecedorApp(nova_janela)

    def TelaFuncionarios(self):
        from funcionarios import GerenciadorFuncionarios
        nova_janela = ctk.CTkToplevel(self.root)
        nova_janela.grab_set()       
        nova_janela.focus_force()    
        GerenciadorFuncionarios(nova_janela)
  
    def TelaClientes(self):
        from cliente import GerenciadorClientes
        janela = ctk.CTkToplevel(self.root)
        janela.grab_set()
        janela.focus_force()
        GerenciadorClientes(janela)
        
    def cadastro_func(self):
        jan_cadastro = ctk.CTkToplevel(self.root)
        jan_cadastro.title("Cadastro de Funcionário")
        jan_cadastro.geometry("900x800")
        jan_cadastro.resizable(False, False)

        frame = ctk.CTkFrame(jan_cadastro, corner_radius=10)
        frame.pack(padx=60, pady=50, fill="both", expand=True)

        title = ctk.CTkLabel(frame, text="CADASTRO DE FUNCIONARIOS", font=("Poppins", 22, "bold"))
        title.pack(pady=20)

        self.funcnomeEntry = ctk.CTkEntry(frame, placeholder_text="Nome: ", width=300, height=40)
        self.funcnomeEntry.pack(pady=10)

        self.telefoneEntry = ctk.CTkEntry(frame, placeholder_text= "Telefone: ", width=300, height=40)
        self.telefoneEntry.pack(pady=10)

        self.gmailEntry = ctk.CTkEntry(frame, placeholder_text="Email: ", width=300, height=40)
        self.gmailEntry.pack(pady=10)

        self.datanascEntry = ctk.CTkEntry(frame, placeholder_text="Data de nascimento: ", width=300, height=40)
        self.datanascEntry.pack(pady=10)

        self.ruafuncEntry = ctk.CTkEntry(frame, placeholder_text="Rua: ", width=300, height=40)
        self.ruafuncEntry.pack(pady=10)

        self.bairrofuncEntry = ctk.CTkEntry(frame, placeholder_text="Bairro: ", width=300, height=40)
        self.bairrofuncEntry.pack(pady=10)

        self.cidadefuncEntry = ctk.CTkEntry(frame, placeholder_text="Cidade: ", width=300, height=40)
        self.cidadefuncEntry.pack(pady=10)

        self.estadofuncEntry = ctk.CTkEntry(frame, placeholder_text="Estado (UF): ", width=300, height=40)
        self.estadofuncEntry.pack(pady=10)

        AddButton = ctk.CTkButton(jan_cadastro, text="REGISTRAR FUNCIONARIO", width=200, command=self.RegistrarFuncionario)
        AddButton.pack(pady=10)

        voltButton = ctk.CTkButton(jan_cadastro, text="Fechar", width=100, fg_color="gray", command=jan_cadastro.destroy)
        voltButton.pack(pady=10)
        jan_cadastro.grab_set()
        jan_cadastro.focus_force()

    def RegistrarFuncionario(self):
        nome = self.funcnomeEntry.get()
        telefone = self.telefoneEntry.get()
        email = self.gmailEntry.get()
        datanascimento = self.datanascEntry.get()
        rua = self.ruafuncEntry.get()
        bairro = self.bairrofuncEntry.get()
        cidade = self.cidadefuncEntry.get()
        estado = self.estadofuncEntry.get()

        if nome == "" or telefone == "" or email == "" or datanascimento == "" or rua == "" or bairro == "" or cidade == "" or estado == "":
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
        else:
            db = comunicacao()
            db.LinkEndereco(rua, bairro, cidade, estado)
            idendereco = db.cursor.lastrowid

            db.RegistrarFuncionario(nome,telefone, email, datanascimento, idendereco)
            db.conn.commit()
            messagebox.showinfo("Sucesso", "Funcionario registrado com sucesso!")
    
    def limpar_campos(self, janela=None):
        self.funcnomeEntry.delete(0, 'end')
        self.telefoneEntry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')
        self.NascEntry.delete(0, 'end')
        self.ruafuncEntry.delete(0, 'end')
        self.bairrofuncEntry.delete(0, 'end')
        self.cidadefuncEntry.delete(0, 'end')
        self.estadofuncEntry.delete(0, 'end')

    def listar_func(self):
        jan_lista = ctk.CTkToplevel(self.root)
        jan_lista.title("Listar Funcionários")
        jan_lista.geometry("800x400")
        jan_lista.resizable(True, True)

        colunas = ("ID", "Nome", "Telefone", "Email", "Data de Nascimento", "Rua", "Bairro", "Cidade", "Estado")
        tree = ttk.Treeview(jan_lista, columns=colunas, show="headings", height=20)

        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=47 if col == "Nome" or col == "Email" else 100)

        tree.pack(padx=10, pady=10, fill="both", expand=True)

        self.carregar_funcionarios(tree)
        self.carregar_funcionarios_com_endereco(tree)
        jan_lista.grab_set()
        jan_lista.focus_force()

    def carregar_funcionarios(self, tree):
        for item in tree.get_children():
            tree.delete(item)

        db = comunicacao()
        try:
            cursor = db.conn.cursor()
            cursor.execute("SELECT idfuncionario, nome, telefone, email, datanascimento FROM funcionario")
            for row in cursor.fetchall():
                tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar funcionários: {e}")

    def atuu_func(self):
        jan_atualizar = ctk.CTkToplevel(self.root)
        jan_atualizar.title("Atualizar Funcionário")
        jan_atualizar.geometry("900x830")
        jan_atualizar.resizable(False, False)
        frame = ctk.CTkFrame(jan_atualizar, corner_radius=10)
        frame.pack(padx=80, pady=50, fill="both", expand=True)

        title = ctk.CTkLabel(frame, text="ATUALIZAR FUNCIONÁRIO", font=("Segoe UI", 18, "bold"))
        title.pack(pady=10)

        self.idEntry = ctk.CTkEntry(frame, placeholder_text="Digite o ID do Funcionário", width=300, height=40)
        self.idEntry.pack(padx=10)

        buscar_botao = ctk.CTkButton(frame, text="Buscar Funcionário", width=150, command=self.buscar_funcionario)
        buscar_botao.pack(pady=10)

        self.funcnomeEntry = ctk.CTkEntry(frame, placeholder_text="Nome do Usuário", width=300, height=40)
        self.funcnomeEntry.pack(pady=10)

        self.telefoneEntry = ctk.CTkEntry(frame, placeholder_text="Telefone", width=300, height=40)
        self.telefoneEntry.pack(pady=10)

        self.EmailEntry = ctk.CTkEntry(frame, placeholder_text="Email", width=300, height=40)
        self.EmailEntry.pack(pady=10)

        self.NascEntry = ctk.CTkEntry(frame, placeholder_text="Data de Nascimento", width=300, height=40)
        self.NascEntry.pack(pady=10)

        self.ruafuncEntry = ctk.CTkEntry(frame, placeholder_text="Rua: ", width=300, height=40)
        self.ruafuncEntry.pack(pady=10)

        self.bairrofuncEntry = ctk.CTkEntry(frame, placeholder_text="Bairro: ", width=300, height=40)
        self.bairrofuncEntry.pack(pady=10)

        self.cidadefuncEntry = ctk.CTkEntry(frame, placeholder_text="Cidade: ", width=300, height=40)
        self.cidadefuncEntry.pack(pady=10)

        self.estadofuncEntry = ctk.CTkEntry(frame, placeholder_text="Estado (UF): ", width=300, height=40)
        self.estadofuncEntry.pack(pady=10)

        salvar_button = ctk.CTkButton(frame, text="Salvar Alterações", width=150, command=self.salvar_alteracoes)
        salvar_button.pack(pady=10)

        voltar_button = ctk.CTkButton(frame, text="Fechar", width=100, fg_color="gray", command=jan_atualizar.destroy)
        voltar_button.pack(pady=10)
        jan_atualizar.grab_set()
        jan_atualizar.focus_force()

    def buscar_funcionario(self):
        idfuncionario = self.idEntry.get()
        if not idfuncionario:
            messagebox.showwarning("Atenção", "Por favor, insira o ID do funcionario.")
            return

        db = comunicacao()
        try:
            # Consulta SQL para buscar o funcionario com informações do endereço
            query = """SELECT f.idfuncionario, f.nome, f.telefone, f.email, f.datanascimento,e.rua, e.bairro, e.cidade, e.estado FROM funcionario f INNER JOIN endereco e ON f.idendereco = e.idendereco WHERE f.idfuncionario = %s"""
            db.cursor.execute(query, (idfuncionario,))
            funcionario = db.cursor.fetchone()

            if not funcionario:
                messagebox.showerror("Erro", "Funcionario não encontrado.")
                return

            # Limpa e preenche os campos corretamente
            self.funcnomeEntry.delete(0, ctk.END)
            self.funcnomeEntry.insert(0, funcionario[1])

            self.telefoneEntry.delete(0, ctk.END)
            self.telefoneEntry.insert(0, funcionario[2])

            self.EmailEntry.delete(0, ctk.END)
            self.EmailEntry.insert(0, funcionario[3])

            self.NascEntry.delete(0, ctk.END)
            self.NascEntry.insert(0, funcionario[4])

            self.ruafuncEntry.delete(0, ctk.END)
            self.ruafuncEntry.insert(0, funcionario[5])

            self.bairrofuncEntry.delete(0, ctk.END)
            self.bairrofuncEntry.insert(0, funcionario[6])

            self.cidadefuncEntry.delete(0, ctk.END)
            self.cidadefuncEntry.insert(0, funcionario[7])

            self.estadofuncEntry.delete(0, ctk.END)
            self.estadofuncEntry.insert(0, funcionario[8])

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar funcionario: {e}")
        finally:
            db.conn.close()

    def carregar_funcionarios_com_endereco(self, tree):
        for item in tree.get_children():
            tree.delete(item)

        db = comunicacao()
        query = """SELECT f.idfuncionario, f.nome, f.telefone, f.email, f.datanascimento, e.rua, e.bairro, e.cidade, e.estado FROM funcionario f LEFT JOIN endereco e ON f.idendereco = e.idendereco"""
        try:
            db.cursor.execute(query)
            funcionarios = db.cursor.fetchall()

            for funcionario in funcionarios:
                tree.insert("", "end", values=funcionario)
        finally:
            db.conn.close()
        

    def salvar_alteracoes(self):
        idfuncionario = self.idEntry.get()
        nome = self.funcnomeEntry.get()
        telefone = self.telefoneEntry.get()
        email = self.EmailEntry.get()
        nascimento = self.NascEntry.get()
        ruafunc = self.ruafuncEntry.get()
        bairrofunc = self.bairrofuncEntry.get()
        cidadefunc = self.cidadefuncEntry.get()
        estadofunc = self.estadofuncEntry.get()

        if not idfuncionario or "" in [nome, telefone, email, nascimento, ruafunc ,bairrofunc,  cidadefunc, estadofunc]:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        db = comunicacao()
        db.cursor.execute("""UPDATE endereco SET rua = %s, bairro = %s, cidade = %s, estado = %s WHERE idendereco = (SELECT idendereco FROM funcionario WHERE idfuncionario = %s)""", ( ruafunc, bairrofunc, cidadefunc, estadofunc,idfuncionario))

        # Atualiza o funcionario
        db.cursor.execute("""UPDATE funcionario SET nome = %s, telefone = %s, email = %s , datanascimento = %s WHERE idfuncionario = %s""", (nome, telefone, email, nascimento,  idfuncionario))
        db.conn.commit()
        messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso!")

    def excluir_func(self):
        jan_excluir = ctk.CTkToplevel(self.root)
        jan_excluir.title("Excluir Funcionário")
        jan_excluir.geometry("800x400")
        jan_excluir.resizable(True, True)

        colunas = ("ID", "Nome", "Telefone", "Email", "Data de Nascimento", "Rua", "Bairro", "Cidade", "Estado")
        tree = ttk.Treeview(jan_excluir, columns=colunas, show="headings", height=8)
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=47 if col in ["Nome", "Email"] else 100)
        tree.pack(padx=10, pady=10, fill="both", expand=True)

        self.carregar_funcionarios(tree)

        def excluir_selecionado():
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Atenção", "Selecione um funcionário.")
                return
            id_sel = tree.item(selecionado)["values"][0]
            resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir?")
            if resposta:
                db = comunicacao()
                db.ExcluirFuncionario(id_sel)
                self.carregar_funcionarios(tree)
                messagebox.showinfo("Sucesso", "Funcionário excluído.")

        ctk.CTkButton(jan_excluir, text="Excluir Selecionado", command=excluir_selecionado).pack(pady=10)

        self.carregar_funcionarios_com_endereco(tree)
        jan_excluir.grab_set()
        jan_excluir.focus_force()

    def sair(self):
        from dash import DashboardDistribuidora
        DashboardDistribuidora(self.root)
        self.root.withdraw()


# Inicializa a aplicação
if __name__ == "__main__":
    root = ctk.CTk()
    app = GerenciadorFuncionarios(root)
    root.mainloop()