import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import mysql.connector
from comunicacao import comunicacao  
from CTkMenuBar import *

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

        self.enderecoEntry = ctk.CTkEntry(frame, placeholder_text="Endereço: ", width=300, height=40)
        self.enderecoEntry.pack(pady=10)

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
        
        # Recebe as informações do usúario e guarda em cada variavel dedicada 
        nomeCliente = self.clienomeEntry.get().strip()
        cnpj = self.cnpjEntry.get().strip()
        endereco = self.enderecoEntry.get().strip()
        
        
        if nomeCliente == "" or cnpj == "" or endereco == "" :
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
        else:
            db = comunicacao() 
            db.RegistrarCliente(nomeCliente, cnpj, endereco)
            messagebox.showinfo("Success", "Usuario criado com sucesso!")
    
    def limpar_campos(self, jan_clientecad=None):
        self.clienomeEntry.delete(0, 'end')
        self.cnpjEntry.delete(0, 'end')
        self.enderecoEntry.delete(0, 'end')
        
        
    def listar_cliente(self):
        jan_lista = ctk.CTkToplevel(self.root)
        jan_lista.title("Listar Clientes")
        jan_lista.geometry("800x400")
        jan_lista.resizable(True, True)

        colunas = ( "ID" , "Nome", "Cnpj", "Endereço") 
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
        try:
            cursor = db.conn.cursor()
            cursor.execute("SELECT idcliente, NomeCliente, CNPJ	, endereco FROM cliente")
            for row in cursor.fetchall():
                tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar clientes: {e}")

    def atuu_clien(self):
        jan_atualizar = ctk.CTkToplevel(self.root)
        jan_atualizar.title("Atualizar Cliente")
        jan_atualizar.geometry("800x600")
        jan_atualizar.resizable(False, False)

        ctk.CTkLabel(jan_atualizar, text="Digite o id do cliente : ", font=("Arial", 16)).place(x=115, y=50)
        self.idcliente = ctk.CTkEntry(jan_atualizar, width=200)
        self.idcliente.place(x=330, y=55)

        ctk.CTkButton(jan_atualizar, text="Buscar clientes", command=self.buscar_cliente).place(x=330, y=90)

        # Campos atualizáveis
        self.idcliente = ctk.CTkEntry(jan_atualizar, width=300)
        self.clienomeEntry = ctk.CTkEntry(jan_atualizar, width=300)
        self.cnpjEntry = ctk.CTkEntry(jan_atualizar, width=300)
        self.enderecoEntry = ctk.CTkEntry(jan_atualizar, width=300)
        
        

        
        labels = ["Nome", "Cnpj", "Endereço"]
        entries = [self.idcliente, self.clienomeEntry, self.cnpjEntry, self.enderecoEntry]
        for i, label in enumerate(labels):
            ctk.CTkLabel(jan_atualizar, text=label + ":", font=("Arial", 16)).place(x=115, y=150 + i * 50)
            entries[i].place(x=330, y=155 + i * 50)

        ctk.CTkButton(jan_atualizar, text="Salvar Alterações", command=self.salvar_alteracoes).place(x=330, y=420)

        jan_atualizar.grab_set()
        jan_atualizar.focus_force()
    def buscar_cliente(self):
        idcliente = self.idcliente.get()
        if not idcliente:
            messagebox.showwarning("Atenção", "Por favor, insira o id.")
            return

        db = comunicacao()
        cliente = db.buscar_cliente_por_id(idcliente)
        if not cliente:
            messagebox.showerror("Erro", "Cliente não listado.")
            return

        self.idcliente.delete(0, )
        self.idcliente.insert(0, cliente[1])
        self.clienomeEntry.delete(0, )
        self.clienomeEntry.insert(0, cliente[2])
        self.cnpjEntry.delete(0, )
        self.cnpjEntry.insert(0, cliente[3])
        self.enderecoEntry.delete(0, )
        self.enderecoEntry.insert(0, cliente[4])
       
        

    def salvar_alteracoes(self):

        # Recebe as informações do usúario e guarda em cada variavel dedicada 
        idcliente = self.idcliente.get()
        nome = self.clienomeEntry.get()
        cnpj = self.cnpjEntry.get()
        endereco = self.enderecoEntry.get()
      
        

        if not idcliente or "" in [nome, cnpj, endereco]:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        db = comunicacao()
        db.AtualizarCliente(idcliente, nome, cnpj, endereco)
        messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso! ")

    def excluir_clien(self):
        jan_excluir = ctk.CTkToplevel(self.root)
        jan_excluir.title("Excluir Cliente")
        jan_excluir.geometry("800x400")
        jan_excluir.resizable(True, True)

        colunas = ("Id", "Nome", "Cnpj", "Endereco")
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
                db.excluir_clien(id_sel)
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