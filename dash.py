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
        self.root.geometry("1920x1080")
        self.root.resizable(True, True)
        self.root.configure(bg="#f6f6f6")

        # Frame superior com título
        self.frame_titulo = ctk.CTkFrame(self.root, fg_color="transparent")
        self.frame_titulo.pack(pady=20, padx=20, fill="x")
        
        self.titulo = ctk.CTkLabel(
            self.frame_titulo, 
            text="DASHBOARD - DISTRIBUIDORA DE LIVROS", 
            font=("Segoe UI", 24, "bold")
        )
        self.titulo.pack(side="left", padx=10)
        
        # Switch para alternância de tema
        self.theme_switch = ctk.CTkSwitch(
            self.frame_titulo, 
            text="Modo Escuro", 
            command=self.alternar_tema
        )
        self.theme_switch.pack(side="right", padx=10)

        # Frame principal com os cards
        self.frame_principal = ctk.CTkFrame(self.root, fg_color="transparent")
        self.frame_principal.pack(pady=10, padx=20, fill="both", expand=True)

        # Linha 0 - Botões para navegação de telas

        self.frame_linha0 = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_linha0.pack(fill="x", pady=5)

        
        #Botão de abrir estoque
        self.botao_Bestoque = ctk.CTkButton(
            self.frame_linha0,
            text="ABRIR PRODUTOS", 
            width=200, 
            command=self.abrir_gerenciador_estoque
        )
        self.botao_Bestoque.place(x = 400, y = 50)

        #Descrição de produtos
        self.label_Bestoque = ctk.CTkLabel(
            self.frame_linha0, 
            text="Na tela de produtos você pode\ncadastrar, listar, excluir\ne pesquisar os produtos", 
            font=("Segoe UI", 14, "bold")
        )
        self.label_Bestoque.place(x = 395, y = 90)


        #Botão para funcionairos
        self.botao_BFuncionario = ctk.CTkButton(
            self.frame_linha0,
            text="ABRIR FUNCIONARIO", 
            width=200, 
            command=self.abrir_gerenciador_funcionario
        )
        self.botao_BFuncionario.place(x = 850, y = 50)


        #descrição para funcionarios
        self.label_Bfuncionario = ctk.CTkLabel(
            self.frame_linha0, 
            text="Tela de funcionários\nVocê pode cadastrar, listar, excluir\ne pesquisar os funcionários da nossa biblioteca", 
            font=("Segoe UI", 14, "bold")
        )
        self.label_Bfuncionario.place(x = 790, y = 90)


        #Botão para fornecedor
        self.botao_Bfornecedor = ctk.CTkButton(
            self.frame_linha0,
            text="ABRIR FORNECEDOR", 
            width=200, 
            command=self.abrir_gerenciador_fornecedores
        )
        self.botao_Bfornecedor.place(x = 1350, y = 50)


        self.label_Bfornecedor = ctk.CTkLabel(
            self.frame_linha0, 
            text="Aqui você pode cadastrar,\nlistar, excluir e pesquisar\nos nossos fornecedores", 
            font=("Segoe UI", 14, "bold")
        )
        self.label_Bfornecedor.place(x = 1360, y = 90)

   

        # Linha 1 - Cards de resumo
      
    
        self.frame_linha1 = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_linha1.pack(fill="y", pady=30)


        # Card 1 - Estoque Total
        self.card_estoque = ctk.CTkFrame(self.frame_linha1, width=250, height=150, corner_radius=10)
        self.card_estoque.pack_propagate(False)
        self.card_estoque.pack(side="left", padx=10)
        
        self.label_estoque = ctk.CTkLabel(
            self.card_estoque, 
            text="Estoque Total", 
            font=("Segoe UI", 14, "bold")
        )
        self.label_estoque.pack(pady=(15, 5))
        
        self.valor_estoque = ctk.CTkLabel(
            self.card_estoque, 
            text="0", 
            font=("Segoe UI", 36, "bold")
        )
        self.valor_estoque.pack(pady=5)
        


        # Card 2 - Valor Total em Livros
        self.card_valor = ctk.CTkFrame(self.frame_linha1, width=250, height=150, corner_radius=10)
        self.card_valor.pack_propagate(False)
        self.card_valor.pack(side="left", padx=10)
        
        self.label_valor = ctk.CTkLabel(
            self.card_valor, 
            text="Valor Total em Livros", 
            font=("Segoe UI", 14, "bold")
        )
        self.label_valor.pack(pady=(15, 5))
        
        self.valor_total = ctk.CTkLabel(
            self.card_valor, 
            text="R$ 0,00", 
            font=("Segoe UI", 36, "bold")
        )
        self.valor_total.pack(pady=5)
              

        # Card 3 - Clientes Ativos
        self.card_clientes = ctk.CTkFrame(self.frame_linha1, width=250, height=150, corner_radius=10)
        self.card_clientes.pack_propagate(False)
        self.card_clientes.pack(side="left", padx=10)
        
        self.label_clientes = ctk.CTkLabel(
            self.card_clientes, 
            text="Clientes Ativos", 
            font=("Segoe UI", 14, "bold")
        )
        self.label_clientes.pack(pady=(15, 5))

        
        
        self.valor_clientes = ctk.CTkLabel(
            self.card_clientes, 
            text="0", 
            font=("Segoe UI", 36, "bold")
        )
        self.valor_clientes.pack(pady=5)
        

        # Card 4 - Fornecedores
        self.card_fornecedores = ctk.CTkFrame(self.frame_linha1, width=250, height=150, corner_radius=10)
        self.card_fornecedores.pack_propagate(False)
        self.card_fornecedores.pack(side="left", padx=10)
        
        self.label_fornecedores = ctk.CTkLabel(
            self.card_fornecedores, 
            text="Fornecedores", 
            font=("Segoe UI", 14, "bold")
        )
        self.label_fornecedores.pack(pady=(15, 5))
        
        self.valor_fornecedores = ctk.CTkLabel(
            self.card_fornecedores, 
            text="0", 
            font=("Segoe UI", 36, "bold")
        )
        self.valor_fornecedores.pack(pady=5)


        # Linha 2 - Gráficos
        self.frame_linha2 = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_linha2.pack(fill="both", expand=True, pady= 20)


        # Frame do gráfico de estoque por gênero
        self.frame_grafico_genero = ctk.CTkFrame(self.frame_linha2, width=200, height=500)
        self.frame_grafico_genero.pack_propagate(False)
        self.frame_grafico_genero.pack(side="left", padx=10, pady=10, fill="both", expand=True)
        
        self.label_grafico_genero = ctk.CTkLabel(
            self.frame_grafico_genero, 
            text="Estoque por Gênero", 
            font=("Segoe UI", 14, "bold")
        )
        self.label_grafico_genero.pack(pady=5)
        
        # Criar gráfico de pizza para gêneros
        self.fig_genero, self.ax_genero = plt.subplots(figsize=(5, 3), dpi=100)
        self.canvas_genero = FigureCanvasTkAgg(self.fig_genero, master=self.frame_grafico_genero)
        self.canvas_genero.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        # Frame do gráfico de top produtos
        self.frame_grafico_produtos = ctk.CTkFrame(self.frame_linha2, width=200, height=400)
        self.frame_grafico_produtos.pack_propagate(False)
        self.frame_grafico_produtos.pack(side="right", padx=10, pady=10, fill="both", expand=True)
        
        self.label_grafico_produtos = ctk.CTkLabel(
            self.frame_grafico_produtos, 
            text="Top 5 Produtos em Estoque", 
            font=("Segoe UI", 14, "bold")
        )
        self.label_grafico_produtos.pack(pady=5)
        
        # Criar gráfico de barras para produtos
        self.fig_produtos, self.ax_produtos = plt.subplots(figsize=(5, 3), dpi=100)
        self.canvas_produtos = FigureCanvasTkAgg(self.fig_produtos, master=self.frame_grafico_produtos)
        self.canvas_produtos.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

        # Linha 3 - Tabela de produtos com baixo estoque
        self.frame_linha3 = ctk.CTkFrame(self.frame_principal, fg_color="transparent")
        self.frame_linha3.pack(fill="both", expand=True, pady=10)
        
        # Tabela de produtos
        self.colunas_produtos = ("ID", "Nome", "Gênero", "Quantidade", "Preço")
        self.tree_produtos = ttk.Treeview(
            self.frame_linha3, 
            columns=self.colunas_produtos, 
            show="headings",
            selectmode="browse"
        )

        # Botão de atualização
        self.botao_atualizar = ctk.CTkButton(
            self.root, 
            text="Atualizar Dashboard", 
            width=200, 
            command=self.atualizar_dashboard
        )
        self.botao_atualizar.pack(pady=20)

        # Carregar dados iniciais
        self.atualizar_dashboard()

    def alternar_tema(self):
        modo = "Dark" if self.theme_switch.get() == 1 else "Light"
        ctk.set_appearance_mode(modo)
        
        # Atualizar cores dos gráficos para o tema escuro
        if modo == "Dark":
            plt.style.use('dark_background')
            self.ax_genero.set_facecolor('#2b2b2b')
            self.fig_genero.set_facecolor('#2b2b2b')
            self.ax_produtos.set_facecolor('#2b2b2b')
            self.fig_produtos.set_facecolor('#2b2b2b')
        else:
            plt.style.use('default')
            self.ax_genero.set_facecolor('white')
            self.fig_genero.set_facecolor('white')
            self.ax_produtos.set_facecolor('white')
            self.fig_produtos.set_facecolor('white')
        
        self.atualizar_graficos()

    def atualizar_dashboard(self):
        # Atualizar contadores
        self.carregar_contadores()
        
        # Atualizar gráficos
        self.atualizar_graficos()
        
        # Atualizar tabela de produtos
        self.carregar_produtos_baixo_estoque()

    def carregar_contadores(self):
        db = comunicacao()
        
        # Total em estoque
        db.cursor.execute("SELECT SUM(quantidade) FROM produto")
        total_estoque = db.cursor.fetchone()[0] or 0
        self.valor_estoque.configure(text=str(total_estoque))
        
        # Valor total em livros (considerando preço * quantidade)
        db.cursor.execute("""
            SELECT SUM(CAST(REPLACE(REPLACE(preco, 'R$', ''), ',', '.') AS DECIMAL(10,2)) * quantidade) 
            FROM produto
        """)
        total_valor = db.cursor.fetchone()[0] or 0
        self.valor_total.configure(text=f"R$ {total_valor:,.2f}")

        '''
        
        # Clientes ativos
        db.cursor.execute("SELECT COUNT(*) FROM cliente")
        total_clientes = db.cursor.fetchone()[0] or 0
        self.valor_clientes.configure(text=str(total_clientes))

        '''
        
        # Fornecedores
        db.cursor.execute("SELECT COUNT(*) FROM fornecedor")
        total_fornecedores = db.cursor.fetchone()[0] or 0
        self.valor_fornecedores.configure(text=str(total_fornecedores))

    def atualizar_graficos(self):
        db = comunicacao()
        
        # Gráfico de estoque por gênero
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
        
        # Gráfico de top produtos em estoque
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
        # Limpar a tabela
        for item in self.tree_produtos.get_children():
            self.tree_produtos.delete(item)
        
        # Consultar produtos com baixo estoque (menos de 10 unidades)
        db = comunicacao()
        db.cursor.execute("""
            SELECT idproduto, nome, genero, quantidade, preco
            FROM produto
            WHERE quantidade < 10
            ORDER BY quantidade ASC
            LIMIT 10
        """)
        
        produtos = db.cursor.fetchall()
        
        # Preencher a tabela
        for produto in produtos:
            self.tree_produtos.insert("", "end", values=produto)

    def abrir_gerenciador_estoque(self):
        from produto import TelaProdutos
        janela = ctk.CTkToplevel(self.root)
        janela.grab_set()       
        janela.focus_force()    
        TelaProdutos(janela)

    def abrir_gerenciador_produtos(self):
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

if __name__ == "__main__":
    root = ctk.CTk()
    app = DashboardDistribuidora(root)
    root.mainloop()