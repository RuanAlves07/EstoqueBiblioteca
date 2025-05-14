import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import mysql.connector
from comunicacao import comunicacao  # Certifique-se de que esse módulo existe

class GerenciadorClientes:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Clientes")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f6f6f6")  # Fundo escuro moderno


        # Configuração do tema
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")

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

        self.voltButton = ctk.CTkButton(self.root, text="Fechar", width=100, fg_color="gray", command=self.sair)
        self.voltButton.pack(pady=20)

        # Switch para alternância de tema
        self.theme_switch = ctk.CTkSwitch(self.root, text="Modo Escuro", command=self.alternar_tema)
        self.theme_switch.place(x=10, y=10)

    def alternar_tema(self):
            modo = "Dark" if self.theme_switch.get() == 1 else "Light"
            ctk.set_appearance_mode(modo)    
       
        
    def cadastro_clien(self):
        jan_clientecad = ctk.CTkToplevel(self.root)
        jan_clientecad.title("Cadastro de Cliente")
        jan_clientecad.geometry("800x600")
        jan_clientecad.resizable(False, False)

        frame = ctk.CTkFrame(jan_clientecad, corner_radius=10)
        frame.pack(padx=60, pady=50, fill="both", expand=True)

        title = ctk.CTkLabel(frame, text="CADASTRO DE CLIENTES", font=("Segoe UI", 18, "bold"))
        title.pack(pady=20)

        self.numeroNFEntry = ctk.CTkEntry(frame, placeholder_text="Número da nota fiscal: ", width=300, height=40)
        self.numeroNFEntry.pack(pady=10)

        self.clienomeEntry = ctk.CTkEntry(frame, placeholder_text="Nome: ", width=300, height=40)
        self.clienomeEntry.pack(pady=10)

        self.qtdecomprasEntry = ctk.CTkEntry(frame, placeholder_text= "Quantidade de compras: ", width=300, height=40)
        self.qtdecomprasEntry.pack(pady=10)

        self.produtoEntry = ctk.CTkEntry(frame, placeholder_text="Produto: ", width=300, height=40)
        self.produtoEntry.pack(pady=10)

        self.dataemissaoEntry = ctk.CTkEntry(frame, placeholder_text="Data Emissão: ", width=300, height=40)
        self.dataemissaoEntry.pack(pady=10)


        AddButton = ctk.CTkButton(jan_clientecad, text="REGISTRAR FUNCIONARIO", width=200, command=self.RegistrarCliente)
        AddButton.pack(pady=10)

        voltButton = ctk.CTkButton(jan_clientecad, text="Fechar", width=100, fg_color="gray", command=jan_clientecad.destroy)
        voltButton.pack(pady=10)


    def RegistrarCliente(self):
        numeroNF = self.numeroNFEntry.get().strip()
        nome = self.clienomeEntry.get().strip()
        qtdecompras = self.qtdecomprasEntry.get().strip()
        produto = self.produtoEntry.get().strip()
        dataemissao = self.dataemissaoEntry.get().strip()
        

        if numeroNF == "" or nome == "" or qtdecompras == "" or produto == "" or dataemissao :
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
        else:
            db = comunicacao()
            db.RegistrarCliente(numeroNF, nome, qtdecompras, produto, dataemissao)
            messagebox.showinfo("Success", "Usuario criado com sucesso!")
    
    def limpar_campos(self, jan_clientecad=None):
        self.numeroNFEntry.delete(0, 'end')
        self.clienomeEntry.delete(0, 'end')
        self.qtdecomprasEntry.delete(0, 'end')
        self.produtoEntry.delete(0, 'end')
        self.dataemissaoEntry.delete(0, 'end')
        
    def listar_cliente(self):
        jan_lista = ctk.CTkToplevel(self.root)
        jan_lista.title("Listar Funcionários")
        jan_lista.geometry("800x400")
        jan_lista.resizable(True, True)

        colunas = ("Número da NF", "Nome", "Quantidade de Compras", "Produto", "Data de Emissão")
        tree = ttk.Treeview(jan_lista, columns=colunas, show="headings", height=20)

        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=150 if col == "Nome" or col == "Data de Emissão" else 100)

        tree.pack(padx=10, pady=10, fill="both", expand=True)

        self.carregar_clientes(tree)

    def carregar_clientes(self, tree):
        for item in tree.get_children():
            tree.delete(item)

        db = comunicacao()
        try:
            cursor = db.conn.cursor()
            cursor.execute("SELECT numeroNFe, NomeCliente, QuantidadeVendas	, Produto, DataEmissao FROM cliente")
            for row in cursor.fetchall():
                tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar clientes: {e}")

    def atuu_clien(self):
        jan_atualizar = ctk.CTkToplevel(self.root)
        jan_atualizar.title("Atualizar Cliente")
        jan_atualizar.geometry("800x600")
        jan_atualizar.resizable(False, False)

        ctk.CTkLabel(jan_atualizar, text="Número da nota fiscal: ", font=("Arial", 16)).place(x=115, y=50)
        self.numeroNFEntry = ctk.CTkEntry(jan_atualizar, width=200)
        self.numeroNFEntry.place(x=330, y=55)

        ctk.CTkButton(jan_atualizar, text="Buscar clientes", command=self.buscar_cliente).place(x=330, y=90)

        # Campos atualizáveis
        self.numeroNFEntry = ctk.CTkEntry(jan_atualizar, width=300)
        self.clienomeEntry = ctk.CTkEntry(jan_atualizar, width=300)
        self.qtdecomprasEntry = ctk.CTkEntry(jan_atualizar, width=300)
        self.produtoEntry = ctk.CTkEntry(jan_atualizar, width=300)
        self.dataemissaoEntry = ctk.CTkEntry(jan_atualizar, width=300)
        

        #Sou bixa
        labels = ["Número da nota fiscal", "Nome", "Quantidade de Compras", "Produto", "Data de Emissão"]
        entries = [self.numeroNFEntry, self.clienomeEntry, self.qtdecomprasEntry, self.produtoEntry, self.dataemissaoEntry]
        for i, label in enumerate(labels):
            ctk.CTkLabel(jan_atualizar, text=label + ":", font=("Arial", 16)).place(x=115, y=150 + i * 50)
            entries[i].place(x=330, y=155 + i * 50)

        ctk.CTkButton(jan_atualizar, text="Salvar Alterações", command=self.salvar_alteracoes).place(x=330, y=420)

    def buscar_cliente(self):
        numeroNFe = self.numeroNFEntry.get()
        if not numeroNFe:
            messagebox.showwarning("Atenção", "Por favor, insira o número da nota fiscal.")
            return

        db = comunicacao()
        cliente = db.buscar_cliente_por_id(numeroNFe)
        if not cliente:
            messagebox.showerror("Erro", "Funcionário não encontrado.")
            return

        self.numeroNFEntry.delete(0, 'end')
        self.numeroNFEntry.insert(0, cliente[1])
        self.clienomeEntry.delete(0, 'end')
        self.clienomeEntry.insert(0, cliente[2])
        self.qtdecomprasEntry.delete(0, 'end')
        self.qtdecomprasEntry.insert(0, cliente[3])
        self.produtoEntry.delete(0, 'end')
        self.produtoEntry.insert(0, cliente[4])
        self.dataemissaoEntry.delete(0, 'end')
        self.dataemissaoEntry.insert(0, cliente[5])
        

    def salvar_alteracoes(self):
        numeroNF = self.numeroNFEntry.get()
        nome = self.clienomeEntry.get()
        qtdecompras = self.qtdecomprasEntry.get()
        produto = self.produtoEntry.get()
        dataemissao = self.dataemissaoEntry.get()
        

        if not numeroNF or "" in [nome, qtdecompras, produto, dataemissao]:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        db = comunicacao()
        db.AtualizarFuncionario(numeroNF, nome, qtdecompras, produto, dataemissao)
        messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")

    def excluir_clien(self):
        jan_excluir = ctk.CTkToplevel(self.root)
        jan_excluir.title("Excluir Cliente")
        jan_excluir.geometry("800x400")
        jan_excluir.resizable(True, True)

        colunas = ("Número da nota fiscal", "Nome", "Quantidade de Compras", "Produto", "Data de Emissão")
        tree = ttk.Treeview(jan_excluir, columns=colunas, show="headings", height=8)
        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=120 if col in ["Nome", "Data de Emissão"] else 100)
        tree.pack(padx=10, pady=10, fill="both", expand=True)

        self.carregar_clientes(tree)

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
        from MenuAdm import Menuadm
        Menuadm(self.root)
        self.root.withdraw()


# Inicializa a aplicação
if __name__ == "__main__":
    root = ctk.CTk()
    app = GerenciadorClientes(root)
    root.mainloop()