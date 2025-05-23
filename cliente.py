import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import mysql.connector
from comunicacao import comunicacao  
from CTkMenuBar import *
from tkinter import END, messagebox

class GerenciadorClientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Clientes")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f6f6f6")  # Fundo escuro moderno


        # Configuração do tema
        ctk.set_appearance_mode("Light") 
        ctk.set_default_color_theme("blue")

        BarraNavegabilidade = CTkMenuBar(root)
        botao_1 = BarraNavegabilidade.add_cascade("Produtos", command = self.GoToproduto) # Aba do menu que direciona o usuário à tela produto 
        botao_2 = BarraNavegabilidade.add_cascade("Fornecedores", command = self.TelaFornecedores) # Aba do menu que direciona o usuário à tela fornecedores 
        botao_3 = BarraNavegabilidade.add_cascade("Funcionarios", command = self.TelaFuncionarios) # Aba do menu que direciona o usuário à tela funcionarios 
        botao_4 = BarraNavegabilidade.add_cascade("Clientes", command = self.TelaClientes) # Aba do menu que direciona o usuário à tela clientes 
 
     # Título
        Titulolabel = ctk.CTkLabel(self.root, text="GERENCIADOR DE CLIENTES",
        font=("Segoe UI", 22, "bold"))
        Titulolabel.pack(pady=70)

        # Botões principais
        self.cadButton = ctk.CTkButton(self.root, text="Cadastrar Cliente", width=300, command=self.cadastro_clien)
        self.cadButton.pack(pady=10)

        self.excnButton = ctk.CTkButton(self.root, text="Excluir Cliente", width=300, command=self.excluir_clien)
        self.excnButton.pack(pady=10)

        self.listButton = ctk.CTkButton(self.root, text="Listar Cliente", width=300, command=self.listar_cliente)
        self.listButton.pack(pady=10)

        self.atuButton = ctk.CTkButton(self.root, text="Atualizar Cliente", width=300, command=self.atuu_clien)
        self.atuButton.pack(pady=10)

        self.PedidoButton = ctk.CTkButton(self.root, text="Pedidos", width=300, command=self.TelaPedidos)
        self.PedidoButton.pack(pady=10)

       

        
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

        
    def cadastro_clien(self):
        jan_clientecad = ctk.CTkToplevel(self.root)
        jan_clientecad.title("Cadastro de Cliente")
        jan_clientecad.geometry("800x600")
        jan_clientecad.resizable(False, False)

        frame = ctk.CTkFrame(jan_clientecad, corner_radius=10) 
        frame.pack(padx=60, pady=50, fill="both", expand=True)
        
        # Título
        title = ctk.CTkLabel(frame, text="CADASTRO DE CLIENTES", font=("Segoe UI", 18, "bold")) 
        title.pack(pady=20)

        # Botões principais
        self.clienomeEntry = ctk.CTkEntry(frame, placeholder_text="Nome: ", width=300, height=40)
        self.clienomeEntry.pack(pady=10)

        self.cnpjEntry = ctk.CTkEntry(frame, placeholder_text= "Cnpj: ", width=300, height=40)
        self.cnpjEntry.pack(pady=10)

        self.ruaEntry = ctk.CTkEntry(frame, placeholder_text="Rua", width=300, height=40)
        self.ruaEntry.pack(pady=10)

        self.bairroEntry = ctk.CTkEntry(frame, placeholder_text="Bairro", width=300, height=40)
        self.bairroEntry.pack(pady=10)

        self.cidadeEntry = ctk.CTkEntry(frame, placeholder_text="Cidade", width=300, height=40)
        self.cidadeEntry.pack(pady=10)

        self.estadoEntry = ctk.CTkEntry(frame, placeholder_text="Estado (UF)", width=300, height=40)
        self.estadoEntry.pack(pady=10)

        jan_clientecad.grab_set()
        jan_clientecad.focus_force()  


        AddButton = ctk.CTkButton(jan_clientecad, text="REGISTRAR CLIENTE", width=200, command=self.RegistrarCliente)
        AddButton.pack(pady=10)

    def TelaPedidos(self):
        from pedido import AppPedidos
        nova_janela = ctk.CTkToplevel(self.root)
        nova_janela.grab_set()
        nova_janela.focus_force()
        AppPedidos(nova_janela)


    def RegistrarCliente(self):
        nomeCliente = self.clienomeEntry.get()
        cnpj = self.cnpjEntry.get()
        rua = self.ruaEntry.get()
        bairro = self.bairroEntry.get()
        cidade = self.cidadeEntry.get()
        estado = self.estadoEntry.get()

        if nomeCliente == "" or cnpj == "" or rua == "" or bairro == '' or cidade == '' or estado == '':
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
        else:
            db = comunicacao()

            db.LinkEndereco(rua, bairro, cidade, estado)
            idendereco = db.cursor.lastrowid  # Pega o ID do novo endereço

            db.RegistrarCliente(nomeCliente, cnpj, idendereco)

            db.conn.commit()

            messagebox.showinfo("Sucesso", "Cliente registrado com sucesso!")
            self.limpar_campos()

    
    def limpar_campos(self, jan_clientecad=None):
        self.clienomeEntry.delete(0, 'end')
        self.cnpjEntry.delete(0, 'end')
        self.ruaEntry.delete(0, 'end')
        self.bairroEntry.delete(0, 'end')
        self.cidadeEntry.delete(0, 'end')
        self.estadoEntry.delete(0, 'end')
        
        
    def listar_cliente(self):
        jan_lista = ctk.CTkToplevel(self.root)
        jan_lista.title("Listar Clientes")
        jan_lista.geometry("800x400")
        jan_lista.resizable(True, True)

        colunas = ("ID", "Nome", "CNPJ","Rua", "Bairro", "Cidade", "Estado")
        tree = ttk.Treeview(jan_lista, columns=colunas, show="headings", height=20)

        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=150 if col == "Nome" or col == "ID" else 100)

        tree.pack(padx=10, pady=10, fill="both", expand=True)

        self.carregar_clientes(tree)
        jan_lista.grab_set()
        jan_lista.focus_force()

    def carregar_clientes(self, tree):
        for item in tree.get_children():
            tree.delete(item)

        db = comunicacao()
        query = """SELECT c.idcliente, c.NomeCliente, c.CNPJ, e.rua, e.bairro, e.cidade, e.estado FROM cliente c LEFT JOIN endereco e ON c.idendereco = e.idendereco"""
        try:
            db.cursor.execute(query)
            clientes = db.cursor.fetchall()

            for cliente in clientes:
                tree.insert("", "end", values=cliente)
        finally:
            db.conn.close()
    def atuu_clien(self):
        jan_atualizar = ctk.CTkToplevel(self.root)
        jan_atualizar.title("Atualizar Cliente")
        jan_atualizar.geometry("800x600")
        jan_atualizar.resizable(False, False)

        ctk.CTkLabel(jan_atualizar, text="Digite o id do cliente: ", font=("Arial", 16)).place(x=115, y=50)
        self.idclientes = ctk.CTkEntry(jan_atualizar, width=200)
        self.idclientes.place(x=330, y=55)

        ctk.CTkButton(jan_atualizar, text="Buscar clientes", command=self.buscar_cliente).place(x=330, y=90)

        # Campos atualizáveis
        self.idcliente = ctk.CTkEntry(jan_atualizar, width=300)
        self.clienomeEntry = ctk.CTkEntry(jan_atualizar, width=300)
        self.cnpjEntry = ctk.CTkEntry(jan_atualizar, width=300)
        self.ruaEntry = ctk.CTkEntry(jan_atualizar, width=300)
        self.bairroEntry = ctk.CTkEntry(jan_atualizar,  width=300)
        self.cidadeEntry = ctk.CTkEntry(jan_atualizar,  width=300)
        self.estadoEntry = ctk.CTkEntry(jan_atualizar,  width=300)
        
        labels = ["Nome", "Cnpj", "rua", "bairro", "cidade", "estado"]
        entries = [self.clienomeEntry, self.cnpjEntry, self.ruaEntry, self.bairroEntry, self.cidadeEntry, self.estadoEntry]
        for i, label in enumerate(labels):
            ctk.CTkLabel(jan_atualizar, text=label + ":", font=("Arial", 16)).place(x=115, y=150 + i * 50)
            entries[i].place(x=330, y=155 + i * 50)

        ctk.CTkButton(jan_atualizar, text="Salvar Alterações", command=self.salvar_alteracoes).place(x=330, y=470)

        jan_atualizar.grab_set()
        jan_atualizar.focus_force()
    def buscar_cliente(self):
        idcliente = self.idclientes.get()

        if not idcliente:
            messagebox.showwarning("Atenção", "Por favor, insira o ID do cliente.")
            return

        db = comunicacao()
        try:
            query = """SELECT c.idcliente, c.NomeCliente, c.CNPJ, e.rua, e.bairro, e.cidade, e.estado FROM cliente c INNER JOIN endereco e ON c.idendereco = e.idendereco WHERE c.idcliente = %s"""
            db.cursor.execute(query, (idcliente,))
            cliente = db.cursor.fetchone()

            if not cliente:
                messagebox.showerror("Erro", "Cliente não encontrado.")
                return

            # Preenchimento dos campos - Garantindo que os widgets existam
            self.clienomeEntry.delete(0, 'end')
            self.clienomeEntry.insert(0, cliente[1])  

            self.cnpjEntry.delete(0, 'end')
            self.cnpjEntry.insert(0, cliente[2])

            self.ruaEntry.delete(0, 'end')
            self.ruaEntry.insert(0, cliente[3])

            self.bairroEntry.delete(0, 'end')
            self.bairroEntry.insert(0, cliente[4])

            self.cidadeEntry.delete(0, 'end')
            self.cidadeEntry.insert(0, cliente[5])

            self.estadoEntry.delete(0, 'end')
            self.estadoEntry.insert(0, cliente[6])

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar cliente: {e}")
            

    def salvar_alteracoes(self):
        idcliente = self.idclientes.get()
        nome = self.clienomeEntry.get()
        cnpj = self.cnpjEntry.get()
        rua = self.ruaEntry.get()
        bairro = self.bairroEntry.get()
        cidade = self.cidadeEntry.get()
        estado = self.estadoEntry.get()

        if not all([nome, cnpj, rua, bairro, cidade, estado]):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        db = comunicacao()
        try:
            db.AtualizarEnderecoCliente(rua, bairro, cidade, estado, idcliente)
            db.AtualizarCliente(idcliente, nome, cnpj)
            messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao atualizar cliente: {e}")

    def excluir_clien(self):
        jan_excluir = ctk.CTkToplevel(self.root)
        jan_excluir.title("Excluir Cliente")
        jan_excluir.geometry("800x400")
        jan_excluir.resizable(True, True)

        colunas = ("Id", "Nome", "Cnpj", "rua", "bairro", "cidade", "estado")
        tree = ttk.Treeview(jan_excluir, columns=colunas, show="headings", height=8)
        for col in colunas: 
            tree.heading(col, text=col)
            tree.column(col, width=120 if col in ["Nome", "Id"] else 100)
        tree.pack(padx=10, pady=10, fill="both", expand=True)

        self.carregar_clientes(tree)

        jan_excluir.grab_set()
        jan_excluir.focus_force()
        def excluir_selecionado():
            selecionado = tree.selection()
            if not selecionado:
                messagebox.showwarning("Atenção", "Selecione um cliente.")
                return
            id_sel = tree.item(selecionado)["values"][0]
            resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir?")
            if resposta:
                db = comunicacao()
                db.ExcluirCliente(id_sel)
                self.carregar_clientes(tree)
                messagebox.showinfo("Sucesso", "cliente excluído.")

        ctk.CTkButton(jan_excluir, text="Excluir Selecionado", command=excluir_selecionado).pack(pady=10)


    def sair(self):
        from dash import DashboardDistribuidora
        DashboardDistribuidora(self.root)
        self.root.withdraw() 


# Inicializa a aplicação
if __name__ == "__main__":
    root = ctk.CTk()
    app = GerenciadorClientes(root)
    root.mainloop()
    