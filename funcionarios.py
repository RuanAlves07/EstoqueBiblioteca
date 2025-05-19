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
  
       
        
    def cadastro_func(self):
        jan_cadastro = ctk.CTkToplevel(self.root)
        jan_cadastro.title("Cadastro de Funcionário")
        jan_cadastro.geometry("800x600")
        jan_cadastro.resizable(False, False)

        frame = ctk.CTkFrame(jan_cadastro, corner_radius=10)
        frame.pack(padx=60, pady=50, fill="both", expand=True)

        title = ctk.CTkLabel(frame, text="CADASTRO DE FUNCIONARIOS", font=("Poppins", 22, "bold"))
        title.pack(pady=20)

        self.funcnomeEntry = ctk.CTkEntry(frame, placeholder_text="Nome: ", width=300, height=40)
        self.funcnomeEntry.pack(pady=10)

        self.telefoneEntry = ctk.CTkEntry(frame, placeholder_text= "Telefone: ", width=300, height=40)
        self.telefoneEntry.pack(pady=10)

        self.enderecoEntry = ctk.CTkEntry(frame, placeholder_text="Endereço: ", width=300, height=40)
        self.enderecoEntry.pack(pady=10)

        self.gmailEntry = ctk.CTkEntry(frame, placeholder_text="Email: ", width=300, height=40)
        self.gmailEntry.pack(pady=10)

        self.datanascEntry = ctk.CTkEntry(frame, placeholder_text="Data de nascimento: ", width=300, height=40)
        self.datanascEntry.pack(pady=10)

        AddButton = ctk.CTkButton(jan_cadastro, text="REGISTRAR FUNCIONARIO", width=200, command=self.RegistrarFuncionario)
        AddButton.pack(pady=10)

        voltButton = ctk.CTkButton(jan_cadastro, text="Fechar", width=100, fg_color="gray", command=jan_cadastro.destroy)
        voltButton.pack(pady=10)


    def RegistrarFuncionario(self):
        nome = self.funcnomeEntry.get().strip()
        telefone = self.telefoneEntry.get().strip()
        enderecofunc = self.enderecoEntry.get().strip()
        email = self.gmailEntry.get().strip()
        datanascimento = self.datanascEntry.get().strip()

        if nome == "" or telefone == "" or enderecofunc == "" or email == "" or datanascimento == "":
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
        else:
            db = comunicacao()
            db.RegistrarFuncionario(nome, telefone, enderecofunc, email, datanascimento)
            messagebox.showinfo("Success", "Usuario criado com sucesso!")
    
    def limpar_campos(self, janela=None):
        self.UsuarioEntry.delete(0, 'end')
        self.TelefoneEntry.delete(0, 'end')
        self.EnderecoEntry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')
        self.NascEntry.delete(0, 'end')

    def listar_func(self):
        jan_lista = ctk.CTkToplevel(self.root)
        jan_lista.title("Listar Funcionários")
        jan_lista.geometry("800x400")
        jan_lista.resizable(True, True)

        colunas = ("ID", "Nome", "Telefone", "Endereço", "Email", "Data de Nascimento")
        tree = ttk.Treeview(jan_lista, columns=colunas, show="headings", height=20)

        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=150 if col == "Nome" or col == "Email" else 100)

        tree.pack(padx=10, pady=10, fill="both", expand=True)

        self.carregar_funcionarios(tree)

    def carregar_funcionarios(self, tree):
        for item in tree.get_children():
            tree.delete(item)

        db = comunicacao()
        try:
            cursor = db.conn.cursor()
            cursor.execute("SELECT idfuncionario, nome, telefone, enderecofunc, email, datanascimento FROM funcionario")
            for row in cursor.fetchall():
                tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar funcionários: {e}")

    def atuu_func(self):
        jan_atualizar = ctk.CTkToplevel(self.root)
        jan_atualizar.title("Atualizar Funcionário")
        jan_atualizar.geometry("800x600")
        jan_atualizar.resizable(False, False)

        frame = ctk.CTkFrame(jan_atualizar, corner_radius=10)
        frame.pack(padx=60, pady=50, fill="both", expand=True)

        title = ctk.CTkLabel(frame, text="ATUALIZAR FUNCIONARIO", font=("Segoe UI", 18, "bold"))
        title.pack(pady=10)

        self.idEntry = ctk.CTkEntry(frame, placeholder_text="Digite o ID do Funcionario", width=300, height=40)
        self.idEntry.pack(pady=10)

        buscar_botao = ctk.CTkButton(frame, text="Buscar Funcionario", width=150, command=self.buscar_funcionario)
        buscar_botao.pack(pady=10)

        self.UsuarioEntry = ctk.CTkEntry(frame, placeholder_text="Nome do usuario", width=300, height=40)
        self.UsuarioEntry.pack(pady=10)

        self.TelefoneEntry = ctk.CTkEntry(frame, placeholder_text="Telefone", width=300, height=40)
        self.TelefoneEntry.pack(pady=10)

        self.EnderecoEntry = ctk.CTkEntry(frame, placeholder_text="Endereço", width=300, height=40)
        self.EnderecoEntry.pack(pady=10)

        self.EmailEntry = ctk.CTkEntry(frame, placeholder_text="Email", width=300, height=40)
        self.EmailEntry.pack(pady=10)

        self.NascEntry = ctk.CTkEntry(frame, placeholder_text="Data de nascimento", width=300, height=40)
        self.NascEntry.pack(pady=10)

        salvar_button = ctk.CTkButton(frame, text="Salvar Alterações", width=120, command=self.salvar_alteracoes)
        salvar_button.pack(pady=10)

        labels = ["Nome", "Telefone", "Endereço", "Email", "Data de Nascimento"]
        entries = [self.UsuarioEntry, self.TelefoneEntry, self.EnderecoEntry, self.EmailEntry, self.NascEntry]

        for i, label in enumerate(labels):
            ctk.CTkLabel(jan_atualizar, text=label + ":", font=("Arial", 16)).place(x=115, y=150 + i * 50)
            entries[i].place(x=330, y=155 + i * 50)

        ctk.CTkButton(jan_atualizar, text="Salvar Alterações", command=self.salvar_alteracoes).place(x=330, y=420)

    def buscar_funcionario(self):
        idfuncionario = self.idEntry.get()
        if not idfuncionario:
            messagebox.showwarning("Atenção", "Por favor, insira o ID.")
            

        db = comunicacao()
        funcionario = db.buscar_funcionario_por_id(idfuncionario)
        if not funcionario:
            messagebox.showerror("Erro", "Funcionário não encontrado.")
            

        self.UsuarioEntry.delete(0, )
        self.UsuarioEntry.insert(0, funcionario[1])
        self.telefoneEntry.delete(0, )
        self.telefoneEntry.insert(0, funcionario[2])
        self.EnderecoEntry.delete(0, )
        self.EnderecoEntry.insert(0, funcionario[3])
        self.EmailEntry.delete(0, )
        self.EmailEntry.insert(0, funcionario[4])
        self.NascEntry.delete(0, )
        self.NascEntry.insert(0, funcionario[5])

    def salvar_alteracoes(self):
        idfuncionario = self.idEntry.get()
        nome = self.UsuarioEntry.get()
        telefone = self.telefoneEntry.get()
        endereco = self.EnderecoEntry.get()
        email = self.EmailEntry.get()
        nascimento = self.NascEntry.get()

        if not idfuncionario or "" in [nome, telefone, endereco, email, nascimento]:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        db = comunicacao()
        db.AtualizarFuncionario(idfuncionario, nome, telefone, endereco, email, nascimento)
        messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso!")

    def excluir_func(self):
        jan_excluir = ctk.CTkToplevel(self.root)
        jan_excluir.title("Excluir Funcionário")
        jan_excluir.geometry("800x400")
        jan_excluir.resizable(True, True)

        colunas = ("ID", "Nome", "Telefone", "Endereço", "Email", "Data de Nascimento")
        tree = ttk.Treeview(jan_excluir, columns=colunas, show="headings", height=8)
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=120 if col in ["Nome", "Email"] else 100)
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


    def sair(self):
        from dash import DashboardDistribuidora
        DashboardDistribuidora(self.root)
        self.root.withdraw()


# Inicializa a aplicação
if __name__ == "__main__":
    root = ctk.CTk()
    app = GerenciadorFuncionarios(root)
    root.mainloop()