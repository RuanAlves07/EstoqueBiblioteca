import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import mysql.connector
from comunicacao import comunicacao  # Certifique-se de que esse módulo existe


class GerenciadorFuncionarios:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Funcionários")
        self.root.geometry("1000x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#2a2d2e")  # Fundo escuro moderno


        # Configuração do tema
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.criar_widgets()

    def criar_widgets(self):
        # Título
        Titulolabel = ctk.CTkLabel(self.root, text="GERENCIADOR DE FUNCIONÁRIOS",
        font=("Arial", 24, "bold"))
        Titulolabel.pack(pady=50)

        # Botões principais
        btn_frame = ctk.CTkFrame(self.root)
        btn_frame.pack(pady=20)

        ctk.CTkButton(btn_frame, text="Cadastrar Funcionário", width=300,
                      command=self.cadastro_func).grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkButton(btn_frame, text="Listar Funcionários", width=300,
                      command=self.listar_func).grid(row=1, column=0, padx=10, pady=10)
        ctk.CTkButton(btn_frame, text="Atualizar Funcionário", width=300,
                      command=self.atuu_func).grid(row=2, column=0, padx=10, pady=10)
        ctk.CTkButton(btn_frame, text="Excluir Funcionário", width=300,
                      command=self.excluir_func).grid(row=3, column=0, padx=10, pady=10)
        ctk.CTkButton(btn_frame, text="Fechar", width=300,
                      command=self.sair).grid(row=4, column=0, padx=10, pady=10)
        
        self.theme_switch = ctk.CTkSwitch(self.root, text="Modo Escuro", command=self.alternar_tema)
        self.theme_switch.place(x=10, y=10)

    

    def alternar_tema(self):
            modo = "Dark" if self.theme_switch.get() == 1 else "Light"
            ctk.set_appearance_mode(modo)    
       
        
    def cadastro_func(self):
        jan_cadastro = ctk.CTkToplevel(self.root)
        jan_cadastro.title("Cadastro de Funcionário")
        jan_cadastro.geometry("800x600")
        jan_cadastro.resizable(False, False)

        # Campos de entrada
        ctk.CTkLabel(jan_cadastro, text="Nome:", font=("Arial", 16)).place(x=115, y=50)
        self.UsuarioEntry = ctk.CTkEntry(jan_cadastro, width=300)
        self.UsuarioEntry.place(x=210, y=60)

        ctk.CTkLabel(jan_cadastro, text="Telefone:", font=("Arial", 16)).place(x=115, y=120)
        self.TelefoneEntry = ctk.CTkEntry(jan_cadastro, width=300)
        self.TelefoneEntry.place(x=240, y=130)

        ctk.CTkLabel(jan_cadastro, text="Endereço:", font=("Arial", 16)).place(x=115, y=190)
        self.EnderecoEntry = ctk.CTkEntry(jan_cadastro, width=300)
        self.EnderecoEntry.place(x=240, y=200)

        ctk.CTkLabel(jan_cadastro, text="Email:", font=("Arial", 16)).place(x=115, y=260)
        self.EmailEntry = ctk.CTkEntry(jan_cadastro, width=300)
        self.EmailEntry.place(x=200, y=270)

        ctk.CTkLabel(jan_cadastro, text="Data de Nascimento:", font=("Arial", 16)).place(x=115, y=330)
        self.NascEntry = ctk.CTkEntry(jan_cadastro, width=300)
        self.NascEntry.place(x=350, y=340)

        # Botão Registrar
        ctk.CTkButton(jan_cadastro, text="REGISTRAR FUNCIONÁRIO", width=200,
                      command=self.RegistrarFuncionario).place(x=300, y=520)
         
       

    def RegistrarFuncionario(self):
        nome = self.UsuarioEntry.get().strip()
        telefone = self.TelefoneEntry.get().strip()
        enderecofunc = self.EnderecoEntry.get().strip()
        email = self.EmailEntry.get().strip()
        datanascimento = self.NascEntry.get().strip()

        if nome == "" or telefone == "" or enderecofunc == "" or email == "" or datanascimento == "":
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
        else:
            db = comunicacao()
            db.RegistrarFuncionario(nome, telefone, enderecofunc, email, datanascimento)
            messagebox.showinfo("Success", "Usuario criado com sucesso!")
        self.limpar_campos()
    def limpar_campos(self, janela=None):
        self.UsuarioEntry.delete(0, 'end')
        self.TelefoneEntry.delete(0, 'end')
        self.EnderecoEntry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')
        self.NascEntry.delete(0, 'end')

    def listar_func(self):
        jan_lista = ctk.CTkToplevel(self.root)
        jan_lista.title("Listar Funcionários")
        jan_lista.geometry("1000x500")
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

        ctk.CTkLabel(jan_atualizar, text="ID do Funcionário:", font=("Arial", 16)).place(x=115, y=50)
        self.idEntry = ctk.CTkEntry(jan_atualizar, width=200)
        self.idEntry.place(x=330, y=55)

        ctk.CTkButton(jan_atualizar, text="Buscar Funcionário", command=self.buscar_funcionario).place(x=330, y=90)

        # Campos atualizáveis
        self.funnomeEntry = ctk.CTkEntry(jan_atualizar, width=300)
        self.telefoneEntry = ctk.CTkEntry(jan_atualizar, width=300)
        self.enderecEntry = ctk.CTkEntry(jan_atualizar, width=300)
        self.emailEntry = ctk.CTkEntry(jan_atualizar, width=300)
        self.nasciEntry = ctk.CTkEntry(jan_atualizar, width=300)

        labels = ["Nome", "Telefone", "Endereço", "Email", "Data de Nascimento"]
        entries = [self.funnomeEntry, self.telefoneEntry, self.enderecEntry, self.emailEntry, self.nasciEntry]

        for i, label in enumerate(labels):
            ctk.CTkLabel(jan_atualizar, text=label + ":", font=("Arial", 16)).place(x=115, y=150 + i * 50)
            entries[i].place(x=330, y=155 + i * 50)

        ctk.CTkButton(jan_atualizar, text="Salvar Alterações", command=self.salvar_alteracoes).place(x=330, y=420)

    def buscar_funcionario(self):
        idfuncionario = self.idEntry.get()
        if not idfuncionario:
            messagebox.showwarning("Atenção", "Por favor, insira o ID.")
            return

        db = comunicacao()
        funcionario = db.buscar_funcionario_por_id(idfuncionario)
        if not funcionario:
            messagebox.showerror("Erro", "Funcionário não encontrado.")
            return

        self.funnomeEntry.delete(0, 'end')
        self.funnomeEntry.insert(0, funcionario[1])
        self.telefoneEntry.delete(0, 'end')
        self.telefoneEntry.insert(0, funcionario[2])
        self.enderecEntry.delete(0, 'end')
        self.enderecEntry.insert(0, funcionario[3])
        self.emailEntry.delete(0, 'end')
        self.emailEntry.insert(0, funcionario[4])
        self.nasciEntry.delete(0, 'end')
        self.nasciEntry.insert(0, funcionario[5])

    def salvar_alteracoes(self):
        idfuncionario = self.idEntry.get()
        nome = self.funnomeEntry.get()
        telefone = self.telefoneEntry.get()
        endereco = self.enderecEntry.get()
        email = self.emailEntry.get()
        nascimento = self.nasciEntry.get()

        if not idfuncionario or "" in [nome, telefone, endereco, email, nascimento]:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        db = comunicacao()
        db.AtualizarFuncionario(idfuncionario, nome, telefone, endereco, email, nascimento)
        messagebox.showinfo("Sucesso", "Funcionário atualizado com sucesso!")

    def excluir_func(self):
        jan_excluir = ctk.CTkToplevel(self.root)
        jan_excluir.title("Excluir Funcionário")
        jan_excluir.geometry("1000x500")
        jan_excluir.resizable(True, True)

        colunas = ("ID", "Nome", "Telefone", "Endereço", "Email", "Data de Nascimento")
        tree = ttk.Treeview(jan_excluir, columns=colunas, show="headings", height=20)
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=150 if col in ["Nome", "Email"] else 100)
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
        from MenuAdm import Menuadm
        Menuadm(self.root)
        self.root.withdraw()


# Inicializa a aplicação
if __name__ == "__main__":
    root = ctk.CTk()
    app = GerenciadorFuncionarios(root)
    root.mainloop()