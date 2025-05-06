import customtkinter as ctk
from tkinter import messagebox, ttk
from comunicacao import comunicacao


class ClienteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Clientes")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#f6f6f6")

        # Título principal
        Titulolabel = ctk.CTkLabel(
            self.root,
            text="GERENCIADOR DE CLIENTES",
            font=("Segoe UI", 22, "bold")
        )
        Titulolabel.pack(pady=70)

        # Botões principais
        self.cadButton = ctk.CTkButton(self.root, text="Cadastrar Cliente", width=300, command=self.cadastro_cli)
        self.cadButton.pack(pady=10)

        self.excnButton = ctk.CTkButton(self.root, text="Excluir Cliente", width=300, command=self.excluir_cli)
        self.excnButton.pack(pady=10)

        self.listButton = ctk.CTkButton(self.root, text="Listar Clientes", width=300, command=self.listar_cli)
        self.listButton.pack(pady=10)

''

        self.voltButton = ctk.CTkButton(self.root, text="Fechar", width=100, fg_color="gray", command=self.sair)
        self.voltButton.pack(pady=20)

        # Switch para alternância de tema
        self.theme_switch = ctk.CTkSwitch(self.root, text="Modo Escuro", command=self.alternar_tema)
        self.theme_switch.place(x=10, y=10)

    def alternar_tema(self):
        modo = "Dark" if self.theme_switch.get() == 1 else "Light"
        ctk.set_appearance_mode(modo)

    def cadastro_cli(self):
        jan = ctk.CTkToplevel(self.root)
        jan.title("Cadastro de Clientes")
        jan.geometry("800x600")
        jan.resizable(False, False)

        frame = ctk.CTkFrame(jan, corner_radius=10)
        frame.pack(padx=60, pady=50, fill="both", expand=True)

        title = ctk.CTkLabel(frame, text="CADASTRO DE CLIENTE", font=("Segoe UI", 18, "bold"))
        title.pack(pady=20)

        self.nomeEntry = ctk.CTkEntry(frame, placeholder_text="Nome Completo ou Empresa", width=300, height=40)
        self.nomeEntry.pack(pady=10)

        self.fantasiaEntry = ctk.CTkEntry(frame, placeholder_text="Nome Fantasia (opcional)", width=300, height=40)
        self.fantasiaEntry.pack(pady=10)

        self.cpfcnpjEntry = ctk.CTkEntry(frame, placeholder_text="CPF ou CNPJ", width=300, height=40)
        self.cpfcnpjEntry.pack(pady=10)

        self.enderecoEntry = ctk.CTkEntry(frame, placeholder_text="Endereço do Cliente", width=300, height=40)
        self.enderecoEntry.pack(pady=10)

        AddButton = ctk.CTkButton(jan, text="REGISTRAR CLIENTE", width=200, command=self.RegistrarNoBanco)
        AddButton.pack(pady=10)

        voltButton = ctk.CTkButton(jan, text="Fechar", width=100, fg_color="gray", command=jan.destroy)
        voltButton.pack(pady=10)

    def RegistrarNoBanco(self):
        nome = self.nomeEntry.get()
        fantasia = self.fantasiaEntry.get()
        cpfcnpj = self.cpfcnpjEntry.get()
        endereco = self.enderecoEntry.get()

        if "" in [nome, cpfcnpj, endereco]:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios!")
            return
        if not self.validar_documento(cpfcnpj):
            messagebox.showerror("Erro", "CPF ou CNPJ inválido.")
            return

        db = comunicacao()
        db.RegistrarCliente(nome, fantasia, cpfcnpj, endereco)
        messagebox.showinfo("Sucesso", "Cliente registrado com sucesso!")
        self.limpar_campos()

    def limpar_campos(self):
        self.nomeEntry.delete(0, 'end')
        self.fantasiaEntry.delete(0, 'end')
        self.cpfcnpjEntry.delete(0, 'end')
        self.enderecoEntry.delete(0, 'end')

    def validar_documento(self, doc):
        # Remove caracteres não numéricos
        doc = ''.join(filter(str.isdigit, doc))
        if len(doc) == 11:
            return self.validar_cpf(doc)
        elif len(doc) == 14:
            return self.validar_cnpj(doc)
        else:
            return False

    def validar_cpf(self, cpf):
        if len(set(cpf)) == 1:
            return False
        soma = sum(int(a) * b for a, b in zip(cpf[:9], range(10, 1, -1)))
        d1 = 11 - (soma % 11)
        d1 = d1 if d1 < 10 else 0
        soma = sum(int(a) * b for a, b in zip(cpf[:10], range(11, 1, -1)))
        d2 = 11 - (soma % 11)
        d2 = d2 if d2 < 10 else 0
        return d1 == int(cpf[9]) and d2 == int(cpf[10])

    def validar_cnpj(self, cnpj):
        if len(set(cnpj)) == 1:
            return False
        pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        d1 = sum(int(d) * p for d, p in zip(cnpj[:12], pesos_1)) % 11
        d1 = 0 if d1 < 2 else 11 - d1
        pesos_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        d2 = sum(int(d) * p for d, p in zip(cnpj[:13], pesos_2)) % 11
        d2 = 0 if d2 < 2 else 11 - d2
        return d1 == int(cnpj[12]) and d2 == int(cnpj[13])

    def excluir_cli(self):
        def excluir_selecionado():
            item_selecionado = tree.selection()
            if not item_selecionado:
                messagebox.showwarning("Atenção", "Selecione um cliente.")
                return
            cliente_id = tree.item(item_selecionado)["values"][0]
            if messagebox.askyesno("Confirmação", f"Excluir cliente ID {cliente_id}?"):
                db = comunicacao()
                db.ExcluirCliente(cliente_id)
                self.carregar_clientes(tree)
                messagebox.showinfo("Sucesso", "Cliente excluído!")

        janela = ctk.CTkToplevel(self.root)
        janela.title("Excluir Cliente")
        janela.geometry("800x400")

        colunas = ("ID", "Nome", "Nome Fantasia", "CPF/CNPJ", "Endereço")
        tree = ttk.Treeview(janela, columns=colunas, show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.heading("Nome Fantasia", text="Nome Fantasia")
        tree.heading("CPF/CNPJ", text="CPF/CNPJ")
        tree.heading("Endereço", text="Endereço")
        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=150)
        tree.column("Nome Fantasia", width=150)
        tree.column("CPF/CNPJ", width=120, anchor="center")
        tree.column("Endereço", width=200)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        bt_excluir = ctk.CTkButton(janela, text="Excluir Selecionado", width=150, command=excluir_selecionado)
        bt_excluir.pack(pady=10)

        bt_fechar = ctk.CTkButton(janela, text="Fechar", width=100, fg_color="gray", command=janela.destroy)
        bt_fechar.pack(pady=5)

        self.carregar_clientes(tree)

    def carregar_clientes(self, tree):
        for item in tree.get_children():
            tree.delete(item)
        db = comunicacao()
        cursor = db.conn.cursor()
        cursor.execute("SELECT idcliente, nome, nomefantasia, cpf_cnpj, endereco FROM cliente")
        clientes = cursor.fetchall()
        for c in clientes:
            tree.insert("", "end", values=c)

    def listar_cli(self):
        janela = ctk.CTkToplevel(self.root)
        janela.title("Lista de Clientes")
        janela.geometry("800x400")

        colunas = ("ID", "Nome", "Nome Fantasia", "CPF/CNPJ", "Endereço")
        tree = ttk.Treeview(janela, columns=colunas, show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.heading("Nome Fantasia", text="Nome Fantasia")
        tree.heading("CPF/CNPJ", text="CPF/CNPJ")
        tree.heading("Endereço", text="Endereço")
        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=150)
        tree.column("Nome Fantasia", width=150)
        tree.column("CPF/CNPJ", width=120, anchor="center")
        tree.column("Endereço", width=200)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        bt_fechar = ctk.CTkButton(janela, text="Fechar", width=100, fg_color="gray", command=janela.destroy)
        bt_fechar.pack(pady=5)

        self.carregar_clientes(tree)

    def attu_cli(self):
        jan = ctk.CTkToplevel(self.root)
        jan.title("Atualizar Cliente")
        jan.geometry("800x600")
        jan.resizable(False, False)

        frame = ctk.CTkFrame(jan, corner_radius=10)
        frame.pack(padx=60, pady=50, fill="both", expand=True)

        title = ctk.CTkLabel(frame, text="ATUALIZAR CLIENTE", font=("Segoe UI", 18, "bold"))
        title.pack(pady=10)

        self.idEntry = ctk.CTkEntry(frame, placeholder_text="Digite o ID do Cliente", width=300, height=40)
        self.idEntry.pack(pady=10)

        buscar_button = ctk.CTkButton(frame, text="Buscar Cliente", width=150, command=self.buscar_cliente)
        buscar_button.pack(pady=10)

        self.nomeEntry = ctk.CTkEntry(frame, placeholder_text="Nome Completo ou Empresa", width=300, height=40)
        self.nomeEntry.pack(pady=10)

        self.fantasiaEntry = ctk.CTkEntry(frame, placeholder_text="Nome Fantasia (opcional)", width=300, height=40)
        self.fantasiaEntry.pack(pady=10)

        self.cpfcnpjEntry = ctk.CTkEntry(frame, placeholder_text="CPF ou CNPJ", width=300, height=40)
        self.cpfcnpjEntry.pack(pady=10)

        self.enderecoEntry = ctk.CTkEntry(frame, placeholder_text="Endereço do Cliente", width=300, height=40)
        self.enderecoEntry.pack(pady=10)

        salvar_button = ctk.CTkButton(frame, text="Salvar Alterações", width=150, command=self.salvar_alteracoes)
        salvar_button.pack(pady=20)

    def buscar_cliente(self):
        idcliente = self.idEntry.get()
        if not idcliente:
            messagebox.showwarning("Atenção", "Por favor, insira o ID do cliente.")
            return
        db = comunicacao()
        cliente = db.buscar_cliente_por_id(idcliente)
        if not cliente:
            messagebox.showerror("Erro", "Cliente não encontrado.")
            return
        self.nomeEntry.delete(0, END)
        self.nomeEntry.insert(0, cliente[1])
        self.fantasiaEntry.delete(0, END)
        self.fantasiaEntry.insert(0, cliente[2])
        self.cpfcnpjEntry.delete(0, END)
        self.cpfcnpjEntry.insert(0, cliente[3])
        self.enderecoEntry.delete(0, END)
        self.enderecoEntry.insert(0, cliente[4])

    def salvar_alteracoes(self):
        idcliente = self.idEntry.get()
        nome = self.nomeEntry.get()
        fantasia = self.fantasiaEntry.get()
        cpfcnpj = self.cpfcnpjEntry.get()
        endereco = self.enderecoEntry.get()

        if not idcliente:
            messagebox.showwarning("Atenção", "Por favor, insira o ID do cliente.")
            return
        if "" in [nome, cpfcnpj, endereco]:
            messagebox.showerror("Erro", "Campos obrigatórios incompletos.")
            return
        if not self.validar_documento(cpfcnpj):
            messagebox.showerror("Erro", "CPF ou CNPJ inválido.")

        db = comunicacao()
        db.AtualizarCliente(idcliente, nome, fantasia, cpfcnpj, endereco)
        messagebox.showinfo("Sucesso", "Cliente atualizado com sucesso!")

    def sair(self):
        from MenuAdm import Menuadm
        Menuadm(self.root)
        self.root.withdraw()


if __name__ == "__main__":
    root = ctk.CTk()
    app = ClienteApp(root)
    root.mainloop()