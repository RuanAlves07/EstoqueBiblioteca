import customtkinter as ctk
from tkinter import ttk
from tkinter import messagebox
from comunicacao import comunicacao
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configuração inicial do tema
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class DashboardDistribuidora:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard - Distribuidora de Livros")
        self.root.state("normal")  # Estado normal, mas com tamanho grande
        self.root.after(100, lambda: self.root.state("zoomed"))
        self.root.resizable(False, False)
        self.root.configure(bg="#f6f6f6")

        # Importações no topo para evitar erro
        from Login import TelaLoginCadastro
        self.TelaLoginCadastro = TelaLoginCadastro

        # Frame superior com título
        self.frame_titulo = ctk.CTkFrame(self.root, fg_color="transparent")
        self.frame_titulo.pack(pady=20, padx=20, fill="x")

        self.titulo = ctk.CTkLabel(
            self.frame_titulo,
            text="DASHBOARD - DISTRIBUIDORA DE LIVROS",
            font=("Segoe UI", 24, "bold")
        )
        self.titulo.pack(side="left", padx=10)


        # Frame principal com os cards
        self.frame_principal = ctk.CTkFrame(self.root, fg_color="transparent")
        self.frame_principal.pack(pady=10, padx=20, fill="both", expand=True)

        # Linha 0 - Botões para navegação de telas
        self.frame_linha0 = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_linha0.pack(fill="x", pady=5)

        # Produtos
        self.botao_Bestoque = ctk.CTkButton(
            self.frame_linha0,
            text="ABRIR PRODUTOS",
            width=200,
            command=self.abrir_gerenciador_estoque
        )
        self.botao_Bestoque.grid(row=0, column=0, padx=70)

        self.label_Bestoque = ctk.CTkLabel(
            self.frame_linha0,
            text="Na tela de produtos você pode\n"
                 "cadastrar, listar, excluir\n"
                 "e pesquisar os produtos",
            font=("Segoe UI", 14, "bold")
        )
        self.label_Bestoque.grid(row=1, column=0, padx=70)

        # Funcionários
        self.botao_BFuncionario = ctk.CTkButton(
            self.frame_linha0,
            text="ABRIR FUNCIONARIO",
            width=200,
            command=self.abrir_gerenciador_funcionario
        )
        self.botao_BFuncionario.grid(row=0, column=1, padx=70)

        self.label_Bfuncionario = ctk.CTkLabel(
            self.frame_linha0,
            text="Tela de funcionários\n"
                 "Você pode cadastrar, listar, excluir\n"
                 "e pesquisar os funcionários da nossa biblioteca",
            font=("Segoe UI", 14, "bold")
        )
        self.label_Bfuncionario.grid(row=1, column=1, padx=70)

        # Fornecedores
        self.botao_Bfornecedor = ctk.CTkButton(
            self.frame_linha0,
            text="ABRIR FORNECEDOR",
            width=200,
            command=self.abrir_gerenciador_fornecedores
        )
        self.botao_Bfornecedor.grid(row=0, column=2, padx=70)

        self.label_Bfornecedor = ctk.CTkLabel(
            self.frame_linha0,
            text="Aqui você pode cadastrar,\n"
                 "listar, excluir e pesquisar\n"
                 "os nossos fornecedores",
            font=("Segoe UI", 14, "bold")
        )
        self.label_Bfornecedor.grid(row=1, column=2, padx=70)

        # Usuário
        self.botao_Busuario = ctk.CTkButton(
            self.frame_linha0,
            text="CRIAR USUÁRIO",
            width=200,
            command=self.CriarUsuario
        )
        self.botao_Busuario.grid(row=0, column=3, padx=70)

        self.label_Busuario = ctk.CTkLabel(
            self.frame_linha0,
            text="Nessa tela\n"
                 "você pode cadastrar usuários",
            font=("Segoe UI", 14, "bold")
        )
        self.label_Busuario.grid(row=1, column=3, padx=70)

        # Cliente
        self.botao_Bcliente = ctk.CTkButton(
            self.frame_linha0,
            text="ABRIR CLIENTE",
            width=200,
            command=self.abrir_gerenciador_clientes
        )
        self.botao_Bcliente.grid(row=0, column=4, padx=70)

        self.label_Bcliente = ctk.CTkLabel(
            self.frame_linha0,
            text="Aqui você pode cadastrar,\n"
                 "listar, excluir e pesquisar\n"
                 "os nossos clientes",
            font=("Segoe UI", 14, "bold")
        )
        self.label_Bcliente.grid(row=1, column=4, padx=70)

        # Botão Logout
        self.botao_logout = ctk.CTkButton(
            self.frame_titulo,
            text="LOGOUT",
            width=100,
            command=self.logout,
            fg_color="red",
            hover_color="#a52a2a"
        )
        self.botao_logout.place(x=1700)

        # Linha 1 - Cards de resumo
        self.frame_linha1 = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_linha1.pack(fill="y", pady=30)

        # Card Estoque Total
        self.card_estoque = ctk.CTkFrame(self.frame_linha1, width=250, height=150, corner_radius=10)
        self.card_estoque.pack_propagate(False)
        self.card_estoque.pack(side="left", padx=10)
        self.label_estoque = ctk.CTkLabel(
            self.card_estoque, text="Estoque Total", font=("Segoe UI", 14, "bold"))
        self.label_estoque.pack(pady=(15, 5))
        self.valor_estoque = ctk.CTkLabel(self.card_estoque, text="0", font=("Segoe UI", 36, "bold"))
        self.valor_estoque.pack(pady=5)

        # Card Valor Total
        self.card_valor = ctk.CTkFrame(self.frame_linha1, width=250, height=150, corner_radius=10)
        self.card_valor.pack_propagate(False)
        self.card_valor.pack(side="left", padx=10)
        self.label_valor = ctk.CTkLabel(
        self.card_valor, text="Valor Total em Livros", font=("Segoe UI", 14, "bold"))
        self.label_valor.pack(pady=(15, 5))
        self.valor_total = ctk.CTkLabel(self.card_valor, text="R$ 0,00", font=("Segoe UI", 36, "bold"))
        self.valor_total.pack(pady=5)

        # Card Clientes Ativos
        self.card_clientes = ctk.CTkFrame(self.frame_linha1, width=250, height=150, corner_radius=10)
        self.card_clientes.pack_propagate(False)
        self.card_clientes.pack(side="left", padx=10)
        self.label_clientes = ctk.CTkLabel(
        self.card_clientes, text="Clientes Ativos", font=("Segoe UI", 14, "bold"))
        self.label_clientes.pack(pady=(15, 5))
        self.valor_clientes = ctk.CTkLabel(self.card_clientes, text="0", font=("Segoe UI", 36, "bold"))
        self.valor_clientes.pack(pady=5)

        # Card Fornecedores
        self.card_fornecedores = ctk.CTkFrame(self.frame_linha1, width=250, height=150, corner_radius=10)
        self.card_fornecedores.pack_propagate(False)
        self.card_fornecedores.pack(side="left", padx=10)
        self.label_fornecedores = ctk.CTkLabel(
        self.card_fornecedores, text="Fornecedores", font=("Segoe UI", 14, "bold"))
        self.label_fornecedores.pack(pady=(15, 5))
        self.valor_fornecedores = ctk.CTkLabel(
        self.card_fornecedores, text="0", font=("Segoe UI", 36, "bold"))
        self.valor_fornecedores.pack(pady=5)

        # Gráficos
        self.frame_linha2 = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_linha2.pack(fill="both", expand=True, pady=20)

        self.frame_grafico_genero = ctk.CTkFrame(self.frame_linha2, width=400, height=500)
        self.frame_grafico_genero.pack_propagate(False)
        self.frame_grafico_genero.pack(side="left", padx=10, pady=10, fill="both", expand=False)
        self.label_grafico_genero = ctk.CTkLabel(
        self.frame_grafico_genero, text="Estoque por Gênero", font=("Segoe UI", 14, "bold"))
        self.label_grafico_genero.pack(pady=5)

        self.fig_genero, self.ax_genero = plt.subplots(figsize=(5, 3), dpi=100)
        self.canvas_genero = FigureCanvasTkAgg(self.fig_genero, master=self.frame_grafico_genero)
        self.canvas_genero.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        self.frame_grafico_produtos = ctk.CTkFrame(self.frame_linha2, width=200, height=400)
        self.frame_grafico_produtos.pack_propagate(False)
        self.frame_grafico_produtos.pack(side="right", padx=10, pady=10, fill="both", expand=True)
        self.label_grafico_produtos = ctk.CTkLabel(
        self.frame_grafico_produtos, text="Top 5 Produtos em Estoque", font=("Segoe UI", 14, "bold"))
        self.label_grafico_produtos.pack(pady=5)

        self.fig_produtos, self.ax_produtos = plt.subplots(figsize=(5, 3), dpi=100)
        self.canvas_produtos = FigureCanvasTkAgg(self.fig_produtos, master=self.frame_grafico_produtos)
        self.canvas_produtos.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        # Botão Atualizar
        self.botao_atualizar = ctk.CTkButton(
            self.frame_principal, text="Atualizar Dashboard", width=200, command=self.atualizar_dashboard)
        self.botao_atualizar.place(x=100, y=890)

        # Carregar dados iniciais
        self.atualizar_dashboard()

    def atualizar_dashboard(self):
        self.carregar_contadores()
        self.atualizar_graficos()
        self.carregar_produtos_baixo_estoque()

    def carregar_contadores(self):
        db = comunicacao()
        db.cursor.execute("SELECT SUM(quantidade) FROM produto")
        total_estoque = db.cursor.fetchone()[0] or 0
        self.valor_estoque.configure(text=str(total_estoque))

        db.cursor.execute("""
            SELECT SUM(CAST(REPLACE(REPLACE(preco, 'R$', ''), ',', '.') AS DECIMAL(10,2)) * quantidade) 
            FROM produto
        """)
        total_valor = db.cursor.fetchone()[0] or 0
        self.valor_total.configure(text=f"R$ {total_valor:,.2f}")

        db.cursor.execute("SELECT COUNT(*) FROM cliente")
        total_clientes = db.cursor.fetchone()[0] or 0
        self.valor_clientes.configure(text=str(total_clientes))

        db.cursor.execute("SELECT COUNT(*) FROM fornecedor")
        total_fornecedores = db.cursor.fetchone()[0] or 0
        self.valor_fornecedores.configure(text=str(total_fornecedores))

    def atualizar_graficos(self):
        db = comunicacao()
        db.cursor.execute("""
            SELECT 
                CASE genero 
                    WHEN 'L' THEN 'Literatura' 
                    WHEN 'J' THEN 'Juvenil' 
                    WHEN 'I' THEN 'Infantil' 
                    WHEN 'H' THEN 'História/Biografia' 
                    WHEN 'R' THEN 'Referência' 
                    ELSE 'Outros' 
                END as genero, 
                SUM(quantidade) as total 
            FROM produto 
            GROUP BY genero
        """)
        dados_genero = db.cursor.fetchall()
        generos = [dado[0] for dado in dados_genero]
        quantidades = [dado[1] for dado in dados_genero]

        self.ax_genero.clear()
        if len(generos) > 0:
            self.ax_genero.pie(quantidades, labels=generos, autopct='%1.1f%%', startangle=90)
            self.ax_genero.set_title('Distribuição por Gênero')
        else:
            self.ax_genero.text(0.5, 0.5, 'Sem dados disponíveis', ha='center', va='center')
        self.canvas_genero.draw()

        db.cursor.execute("""
            SELECT nome, quantidade 
            FROM produto 
            ORDER BY quantidade DESC 
            LIMIT 5
        """)
        dados_produtos = db.cursor.fetchall()
        produtos = [dado[0] for dado in dados_produtos]
        quantidades = [dado[1] for dado in dados_produtos]

        self.ax_produtos.clear()
        if len(produtos) > 0:
            self.ax_produtos.barh(produtos, quantidades, color='lightgreen')
            self.ax_produtos.set_title('Top 5 Produtos em Estoque')
            self.ax_produtos.set_xlabel('Quantidade')
        else:
            self.ax_produtos.text(0.5, 0.5, 'Sem dados de estoque', ha='center', va='center')
        self.canvas_produtos.draw()

    def carregar_produtos_baixo_estoque(self):
        pass  # Implementar conforme sua estrutura

    def CriarUsuario(self):
        jan = ctk.CTkToplevel(self.root)
        jan.title("Cadastro de Usuário")
        jan.geometry("450x300")
        jan.configure(bg="#f6f3ec")
        jan.resizable(False, False)
        jan.grab_set()
        jan.focus_force()

        form_frame = ctk.CTkFrame(jan, fg_color="transparent")
        form_frame.pack(expand=True, fill="both", padx=20, pady=20)

        campos = [("Usuário:", "UserNomeEntry"), ("Senha:", "SenhaEntry", True),
                  ("Nome Completo:", "UserNomeCEntry"), ("E-mail:", "EmailEntry")]

        for i, (label_text, entry_var, *is_password) in enumerate(campos):
            ctk.CTkLabel(form_frame, text=label_text, font=("Arial", 15)).grid(
                row=i, column=0, sticky="w", padx=10, pady=5)
            entry = ctk.CTkEntry(
                form_frame,
                width=200,
                show="•" if is_password and is_password else ""
            )
            setattr(self, entry_var, entry)
            entry.grid(row=i, column=1, padx=10, pady=5)

        TipoLabel = ctk.CTkLabel(form_frame, text="É Administrador?", font=("Arial", 15))
        TipoLabel.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        self.TipoEntry = ctk.CTkComboBox(
            form_frame,
            values=["Sim", "Não"],
            width=120,
            state="readonly"
        )
        self.TipoEntry.set("Não")
        self.TipoEntry.grid(row=4, column=1, padx=10, pady=5)

        AddButton = ctk.CTkButton(
            form_frame, text="REGISTRAR USUÁRIO", width=200, command=self.RegistrarUsuarios
        )
        AddButton.grid(row=5, column=0, columnspan=2, pady=20)

    def RegistrarUsuarios(self):
        usuario = self.UserNomeEntry.get()
        senha = self.SenhaEntry.get()
        nome = self.UserNomeCEntry.get()
        email = self.EmailEntry.get()
        tipo = self.TipoEntry.get()

        if not nome or not senha or not usuario or not email:
            messagebox.showerror("Erro no Registro", "PREENCHA TODOS OS CAMPOS")
        else:
            db = comunicacao()
            db.RegistrarUsuario(nome, usuario, senha, email, tipo)
            messagebox.showinfo("Sucesso", "Usuário criado com sucesso!")
            self.limpar_campos()

    def logout(self):
        """Fecha o dashboard e retorna à tela de login."""
        self.root.destroy()  # Destrói completamente a janela antiga
        from Login import TelaLoginCadastro
        login_window = ctk.CTk()
        TelaLoginCadastro()
        login_window.mainloop()
        

    def limpar_campos(self):
        self.UserNomeEntry.delete(0, 'end')
        self.SenhaEntry.delete(0, 'end')
        self.UserNomeCEntry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')
        self.TipoEntry.set("Não")

   
    def abrir_gerenciador_estoque(self):
        from produto import TelaProdutos
        janela = ctk.CTkToplevel(self.root)
        janela.grab_set()
        janela.focus_force()
        TelaProdutos(janela)

    def abrir_gerenciador_funcionario(self):
        from funcionarios import GerenciadorFuncionarios
        janela = ctk.CTkToplevel(self.root)
        janela.grab_set()
        janela.focus_force()
        GerenciadorFuncionarios(janela)

    def abrir_gerenciador_fornecedores(self):
        from fornecedor import FornecedorApp
        janela = ctk.CTkToplevel(self.root)
        janela.grab_set()
        janela.focus_force()
        FornecedorApp(janela)

    def abrir_gerenciador_clientes(self):
        from cliente import GerenciadorClientes
        janela = ctk.CTkToplevel(self.root)
        janela.grab_set()
        janela.focus_force()
        GerenciadorClientes(janela)


if __name__ == "__main__":
    root = ctk.CTk()
    app = DashboardDistribuidora(root)
    root.mainloop()