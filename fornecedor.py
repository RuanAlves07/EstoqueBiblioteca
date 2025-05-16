import customtkinter as ctk
from tkinter import messagebox
from comunicacao import comunicacao
from tkinter import ttk
from CTkMenuBar import *

# Configuração inicial do tema
ctk.set_appearance_mode("Light")  # Pode ser "Dark" ou "System"
ctk.set_default_color_theme("blue")  # Cores personalizáveis


class FornecedorApp:
    def __init__(self, root):

        self.root = root
        self.root.title("Gerenciador de Fornecedores")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f6f6f6")

        BarraNavegabilidade = CTkMenuBar(root)
        botao_1 = BarraNavegabilidade.add_cascade("Produtos", command = self.GoToproduto)
        botao_2 = BarraNavegabilidade.add_cascade("Fornecedores", command = self.TelaFornecedores)
        botao_3 = BarraNavegabilidade.add_cascade("Funcionarios", command = self.TelaFuncionarios)

     # Título  
        Titulolabel = ctk.CTkLabel(self.root, text="GERENCIADOR DE FORNECEDORES",
        font=("Times New Roman", 22, "bold"))
        Titulolabel.place(x=220 , y = 75)

        # Botão para ir no menu de registro dos produto
        AButton = ctk.CTkButton(root, text="ADICIONAR FORNECEDORES", width=300, command=self.cadastro_forn)
        AButton.place(x=250, y=200)

        # Botão para ir no menu de remoção de produto
        RemoveButton = ctk.CTkButton(root, text="EXCLUIR FORNECEDORES", width=300, command=self.excluir_forn)
        RemoveButton.place(x=250, y=300)

        # Botão para ir no menu de atualização de informação de produtos
        UpdateButton = ctk.CTkButton(root, text="ATUALIZAR FORNECEDORES", width=300, command=self.atuu_funci)
        UpdateButton.place(x=250, y=400)

        # Botão para ir no menu de listagem de todos os produtos registrados
        ListButton = ctk.CTkButton(root, text="LISTAR FORNECEDORES", width=300, command=self.listar_forn)
        ListButton.place(x=250, y=500)

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


    def alternar_tema(self):
        modo = "Dark" if self.theme_switch.get() == 1 else "Light"
        ctk.set_appearance_mode(modo)

    def cadastro_forn(self):
        jan = ctk.CTkToplevel(self.root)
        jan.title("Cadastro de Fornecedores")
        jan.geometry("800x600")
        jan.resizable(False, False)

        frame = ctk.CTkFrame(jan, corner_radius=10)
        frame.pack(padx=60, pady=50, fill="both", expand=True)

        title = ctk.CTkLabel(frame, text="CADASTRO DE FORNECEDOR", font=("Segoe UI", 18, "bold"))
        title.pack(pady=20)

        self.fornomeEntry = ctk.CTkEntry(frame, placeholder_text="Nome Empresarial", width=300, height=40)
        self.fornomeEntry.pack(pady=10)

        self.ficticioEntry = ctk.CTkEntry(frame, placeholder_text="Nome de Fantasia", width=300, height=40)
        self.ficticioEntry.pack(pady=10)

        self.cnpjEntry = ctk.CTkEntry(frame, placeholder_text="CNPJ da Empresa", width=300, height=40)
        self.cnpjEntry.pack(pady=10)

        self.endEntry = ctk.CTkEntry(frame, placeholder_text="Endereço da Empresa", width=300, height=40)
        self.endEntry.pack(pady=10)

        AddButton = ctk.CTkButton(jan, text="REGISTRAR FORNECEDOR", width=200, command=self.RegistrarNoBanco)
        AddButton.pack(pady=10)

        voltButton = ctk.CTkButton(jan, text="Fechar", width=100, fg_color="gray", command=jan.destroy)
        voltButton.pack(pady=10)
        jan.grab_set()
        jan.focus_force()
    def RegistrarNoBanco(self):
        nome = self.fornomeEntry.get()
        nomefantasia = self.ficticioEntry.get()
        CNPJ = self.cnpjEntry.get()
        endereco = self.endEntry.get()

        if "" in [nome, nomefantasia, CNPJ, endereco]:
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        db = comunicacao()
        db.RegistrarFornecedor(nome, nomefantasia, CNPJ, endereco)
        messagebox.showinfo("Sucesso", "Fornecedor registrado com sucesso!")
        self.limpar_campos()

    def limpar_campos(self):
        self.fornomeEntry.delete(0, 'end')
        self.ficticioEntry.delete(0, 'end')
        self.cnpjEntry.delete(0, 'end')
        self.endEntry.delete(0, 'end')

    def excluir_forn(self):
        def excluir_selecionado():
            item_selecionado = tree.selection()
            if not item_selecionado:
                messagebox.showwarning("Atenção", "Selecione um fornecedor.")
                return
            fornecedor_id = tree.item(item_selecionado)["values"][0]
            if messagebox.askyesno("Confirmação", f"Excluir fornecedor ID {fornecedor_id}?"):
                db = comunicacao()
                db.ExcluirFornecedor(fornecedor_id)
                self.carregar_fornecedores(tree)
                messagebox.showinfo("Sucesso", "Fornecedor excluído!")

        janela = ctk.CTkToplevel(self.root)
        janela.title("Excluir Fornecedor")
        janela.geometry("800x400")

        colunas = ("ID", "Nome", "Nome Fantasia", "CNPJ", "Endereço")
    
        # Use ttk.Treeview em vez de ctk.Treeview
        tree = ttk.Treeview(janela, columns=colunas, show="headings", selectmode="browse")
    
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
    
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        bt_excluir = ctk.CTkButton(janela, text="Excluir Selecionado", width=150, command=excluir_selecionado)
        bt_excluir.pack(pady=10)

        bt_fechar = ctk.CTkButton(janela, text="Fechar", width=100, fg_color="gray", command=janela.destroy)
        bt_fechar.pack(pady=5)
        janela.grab_set()
        janela.focus_force()
        self.carregar_fornecedores(tree)

    def carregar_fornecedores(self, tree):
        for item in tree.get_children():
            tree.delete(item)
        db = comunicacao()
        cursor = db.conn.cursor()
        cursor.execute("SELECT idfornecedor, nome, nomefantasia, CNPJ, endereco FROM fornecedor")
        fornecedores = cursor.fetchall()
        for f in fornecedores:
            tree.insert("", "end", values=f)

    def listar_forn(self):
        janela = ctk.CTkToplevel(self.root)
        janela.title("Lista de Fornecedores")
        janela.geometry("800x400")

        colunas = ("ID", "Nome", "Nome Fantasia", "CNPJ", "Endereço")
    
        # Use ttk.Treeview em vez de ctk.Treeview
        tree = ttk.Treeview(janela, columns=colunas, show="headings", selectmode="browse")
    
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
    
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        bt_fechar = ctk.CTkButton(janela, text="Fechar", width=100, fg_color="gray", command=janela.destroy)
        bt_fechar.pack(pady=5)

        self.carregar_fornecedores(tree)

        self.carregar_fornecedores(tree)
        janela.grab_set()
        janela.focus_force()

    def atuu_funci(self):
        jan = ctk.CTkToplevel(self.root)
        jan.title("Atualizar Fornecedor")
        jan.geometry("800x600")
        jan.resizable(False, False)

        frame = ctk.CTkFrame(jan, corner_radius=10)
        frame.pack(padx=60, pady=50, fill="both", expand=True)

        title = ctk.CTkLabel(frame, text="ATUALIZAR FORNECEDOR", font=("Segoe UI", 18, "bold"))
        title.pack(pady=10)

        self.idEntry = ctk.CTkEntry(frame, placeholder_text="Digite o ID do Fornecedor", width=300, height=40)
        self.idEntry.pack(pady=10)

        buscar_button = ctk.CTkButton(frame, text="Buscar Fornecedor", width=150, command=self.buscar_fornecedor)
        buscar_button.pack(pady=10)

        self.fornomeEntry = ctk.CTkEntry(frame, placeholder_text="Nome Empresarial", width=300, height=40)
        self.fornomeEntry.pack(pady=10)

        self.ficticioEntry = ctk.CTkEntry(frame, placeholder_text="Nome de Fantasia", width=300, height=40)
        self.ficticioEntry.pack(pady=10)

        self.cnpjEntry = ctk.CTkEntry(frame, placeholder_text="CNPJ da Empresa", width=300, height=40)
        self.cnpjEntry.pack(pady=10)

        self.endEntry = ctk.CTkEntry(frame, placeholder_text="Endereço da Empresa", width=300, height=40)
        self.endEntry.pack(pady=10)

        salvar_button = ctk.CTkButton(frame, text="Salvar Alterações", width=150, command=self.salvar_alteracoes)
        salvar_button.pack(pady=20)
        jan.grab_set()
        jan.focus_force()

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
        self.fornomeEntry.delete(0, )
        self.fornomeEntry.insert(0, fornecedor[1])  # Nome empresarial

        self.ficticioEntry.delete(0, )
        self.ficticioEntry.insert(0, fornecedor[2])  # Nome fantasia

        self.cnpjEntry.delete(0, )
        self.cnpjEntry.insert(0, fornecedor[3])  # CNPJ

        self.endEntry.delete(0, )
        self.endEntry.insert(0, fornecedor[4])  # Endereço


    def salvar_alteracoes(self):
        idfornecedor = self.idEntry.get()
        nome = self.fornomeEntry.get()
        nomefantasia = self.ficticioEntry.get()
        CNPJ = self.cnpjEntry.get()
        endereco= self.endEntry.get()

        if not idfornecedor:
            messagebox.showwarning("Atenção", "Por favor, insira o ID do fornecedor.")
            return

        if nome == "" or nomefantasia == "" or CNPJ == "" or endereco == "":
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        db = comunicacao()
        db.AtualizarFornecedor(idfornecedor, nome, nomefantasia, CNPJ, endereco)
        messagebox.showinfo("Sucesso", "Fornecedor atualizado com sucesso!")

    def sair(self):
        from dash import DashboardDistribuidora
        DashboardDistribuidora(self.root)
        self.root.withdraw()


if __name__ == "__main__":
    root = ctk.CTk()
    app = FornecedorApp(root)
    root.mainloop()