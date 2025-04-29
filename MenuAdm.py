import customtkinter as ctk
from tkinter import messagebox
from comunicacao import comunicacao

# Import das telas externas (mantém como estão)

ctk.set_appearance_mode("Light")  # Modo claro
ctk.set_default_color_theme("blue")  # Tema azul


class Menuadm:
    def __init__(self, root):
        self.Abrir_Menu(root)

    def BuscarUsuario(self, nome):
        self.cursor.execute("SELECT * FROM login WHERE nome = %s", (nome,))

    def Abrir_Menu(self, root):
        self.root = root
        self.root.title("MenuAdm")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f6f3ec")
        self.root.resizable(False, False)

        # Centralizar título
        self.BV = ctk.CTkLabel(self.root, text="BEM-VINDO", font=("Arial", 24, "bold"))
        self.BV.pack(pady=50)

        self.InfoLabel = ctk.CTkLabel(
            self.root,
            text="Por favor, selecione uma das opções abaixo",
            font=("Arial", 14),
        )
        self.InfoLabel.pack(pady=10)

        # Frame principal para os botões
        frame_botoes = ctk.CTkFrame(self.root, fg_color="transparent")
        frame_botoes.pack(pady=30)

        # Botão Funcionários
        self.FuncionariosButton = ctk.CTkButton(
            frame_botoes, text="Funcionários", width=180, command=self.TelaFuncionarios
        )
        self.FuncionariosButton.grid(row=0, column=0, padx=40)

        desc_func = (
            "Tela de funcionários\n"
            "Você pode cadastrar, listar, excluir\n"
            "e pesquisar os funcionários da nossa biblioteca"
        )
        ctk.CTkLabel(frame_botoes, text=desc_func, font=("Arial", 10), wraplength=180).grid(
            row=1, column=0, padx=40, pady=(0, 20)
        )

        # Botão Fornecedores
        self.FornecedoresButton = ctk.CTkButton(
            frame_botoes, text="Fornecedores", width=180, command=self.TelaFornecedores
        )
        self.FornecedoresButton.grid(row=0, column=1, padx=40)

        desc_forn = (
            "Aqui você pode cadastrar,\nlistar, excluir "
            "e pesquisar\nos nossos fornecedores"
        )
        ctk.CTkLabel(frame_botoes, text=desc_forn, font=("Arial", 10), wraplength=180).grid(
            row=1, column=1, padx=40, pady=(0, 20)
        )

        # Botão Produtos
        self.ProdutosButton = ctk.CTkButton(
            frame_botoes, text="Produtos", width=180, command=self.TelaProdutos
        )
        self.ProdutosButton.grid(row=0, column=2, padx=40)

        desc_prod = (
            "Na tela de produtos você pode\n"
            "cadastrar, listar, excluir\n"
            "e pesquisar os produtos"
        )
        ctk.CTkLabel(frame_botoes, text=desc_prod, font=("Arial", 10), wraplength=180).grid(
            row=1, column=2, padx=40, pady=(0, 20)
        )

        # Botão Cadastrar Usuário (na parte inferior)
        cadButton = ctk.CTkButton(
            self.root, text="Cadastrar Usuário", width=180, command=self.CriarUsuario
        )
        cadButton.pack(pady=20)

        ctk.CTkLabel(
            self.root,
            text="Você pode cadastrar o seu usuário aqui",
            font=("Arial", 10),
        ).pack()

    def TelaFuncionarios(self):
        from funcionarios import GerenciadorFuncionarios
        nova_janela = ctk.CTkToplevel(self.root)
        GerenciadorFuncionarios(nova_janela)

    def TelaFornecedores(self):
        from fornecedor import FornecedorApp
        nova_janela = ctk.CTkToplevel(self.root)
        FornecedorApp(nova_janela)

    def TelaProdutos(self):
        from produto import TelaProdutos
        nova_janela = ctk.CTkToplevel(self.root)
        TelaProdutos(nova_janela)

    def CriarUsuario(self):
        jan = ctk.CTkToplevel(self.root)
        jan.title("Cadastro de Usuário")
        jan.geometry("650x300")  # Aumentei altura pra caber o novo campo
        jan.configure(bg="#f6f3ec")
        jan.resizable(False, False)

        # Centraliza a janela
        self.center_window(jan, 650, 300)
        jan.grab_set()
        jan.focus_force()

        # Campos do formulário
        UsuarioLabel = ctk.CTkLabel(jan, text="Usuário:", font=("Arial", 15))
        UsuarioLabel.place(x=20, y=35)
        self.UserNomeEntry = ctk.CTkEntry(jan, width=200)
        self.UserNomeEntry.place(x=100, y=40)

        SenhaLabel = ctk.CTkLabel(jan, text="Senha:", font=("Arial", 15))
        SenhaLabel.place(x=30, y=80)
        self.SenhaEntry = ctk.CTkEntry(jan, width=200, show="•")
        self.SenhaEntry.place(x=100, y=85)

        NomeCompletoLabel = ctk.CTkLabel(jan, text="Nome Completo:", font=("Arial", 15))
        NomeCompletoLabel.place(x=300, y=35)
        self.UserNomeCEntry = ctk.CTkEntry(jan, width=230)
        self.UserNomeCEntry.place(x=430, y=40)

        EmailLabel = ctk.CTkLabel(jan, text="E-mail:", font=("Arial", 15))
        EmailLabel.place(x=350, y=80)
        self.EmailEntry = ctk.CTkEntry(jan, width=230)
        self.EmailEntry.place(x=430, y=85)

        # Campo de tipo de usuário (Admin ou Usuário)
        TipoLabel = ctk.CTkLabel(jan, text="É Administrador?", font=("Arial", 15))
        TipoLabel.place(x=20, y=130)

        self.TipoEntry = ctk.CTkComboBox(
            jan,
            values=["Sim", "Não"],
            width=120,
            state="readonly"
        )
        self.TipoEntry.set("Não")  # Valor padrão
        self.TipoEntry.place(x=170, y=130)

        AddButton = ctk.CTkButton(
            jan, text="REGISTRAR USUÁRIO", width=200, command=self.RegistrarUsuarios
        )
        AddButton.place(x=220, y=230)

    def RegistrarUsuarios(self):
        nome = self.UserNomeEntry.get()
        senha = self.SenhaEntry.get()
        usuario = self.UserNomeCEntry.get()
        email = self.EmailEntry.get()

        if not nome or not senha or not usuario or not email:
            messagebox.showerror(title="Erro no Registro", message="PREENCHA TODOS OS CAMPOS")
        else:
            db = comunicacao()
            db.RegistrarCliente(nome, senha, usuario, email)  # Adiciona email se for suportado
            messagebox.showinfo("Sucesso", "Usuário criado com sucesso!")
            self.limpar_campos()

    def limpar_campos(self):
        self.UserNomeEntry.delete(0, 'end')
        self.SenhaEntry.delete(0, 'end')
        self.UserNomeCEntry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')

    def center_window(self, window, width, height):
        """Centraliza qualquer janela na tela"""
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    root = ctk.CTk()
    app = Menuadm(root)
    root.mainloop()