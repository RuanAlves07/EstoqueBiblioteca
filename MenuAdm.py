import customtkinter as ctk
from tkinter import messagebox
from comunicacao import comunicacao
from tkinter import *
from tkinter import ttk

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class Menuadm:
    def __init__(self, root):
        self.root = root
        self.root.title("MenuAdm")
        self.root.geometry("1000x600")
        self.root.configure(bg="transparent")
        self.root.resizable(False, False)

        # Centralizar conteúdo na janela principal
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Frame principal centralizado
        main_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        main_frame.grid(row=0, column=0, padx=20, pady=20)

        # Título centralizado
        self.BV = ctk.CTkLabel(main_frame, text="BEM-VINDO", font=("Arial", 24, "bold"))
        self.BV.pack(pady=20)

        self.InfoLabel = ctk.CTkLabel(
            main_frame,
            text="Por favor, selecione uma das opções abaixo",
            font=("Arial", 14),
        )
        self.InfoLabel.pack(pady=10)

        # Frame de botões
        frame_botoes = ctk.CTkFrame(main_frame)
        frame_botoes.pack()

        # Botões para "Funcionários", "Fornecedores" e "Produtos"
        btn_funcionarios = ctk.CTkButton(frame_botoes, text="Funcionários", width=180, command=self.TelaFuncionarios)
        btn_funcionarios.grid(row=0, column=0, padx=20, pady=10)

        btn_fornecedores = ctk.CTkButton(frame_botoes, text="Fornecedores", width=180, command=self.TelaFornecedores)
        btn_fornecedores.grid(row=0, column=1, padx=20, pady=10)

        btn_produtos = ctk.CTkButton(frame_botoes, text="Produtos", width=180, command=self.TelaProdutos)
        btn_produtos.grid(row=0, column=2, padx=20, pady=10)

        # Descrições abaixo de cada botão
        desc_funcionarios = ctk.CTkLabel(frame_botoes, text="Tela de funcionários\nVocê pode cadastrar, listar, excluir\ne pesquisar os funcionários da nossa biblioteca", font=("Arial", 10), wraplength=180, justify="center")
        desc_funcionarios.grid(row=1, column=0, padx=20, pady=(0, 20))

        desc_fornecedores = ctk.CTkLabel(frame_botoes, text="Aqui você pode cadastrar,\nlistar, excluir e pesquisar\nos nossos fornecedores", font=("Arial", 10), wraplength=180, justify="center")
        desc_fornecedores.grid(row=1, column=1, padx=20, pady=(0, 20))

        desc_produtos = ctk.CTkLabel(frame_botoes, text="Na tela de produtos você pode\ncadastrar, listar, excluir\ne pesquisar os produtos", font=("Arial", 10), wraplength=180, justify="center")
        desc_produtos.grid(row=1, column=2, padx=20, pady=(0, 20))

        # Botão de cadastro de usuário
        cadButton = ctk.CTkButton(main_frame, text="Cadastrar Usuário", width=180, command=self.CriarUsuario)
        cadButton.pack(pady=10)

        # Label explicando o cadastro
        label_desc = ctk.CTkLabel(main_frame, text="Você pode cadastrar o seu usuário aqui", font=("Arial", 10))
        label_desc.pack()

    def TelaFuncionarios(self):
        from funcionarios import GerenciadorFuncionarios
        nova_janela = ctk.CTkToplevel(self.root)
        nova_janela.grab_set()       
        nova_janela.focus_force()    
        GerenciadorFuncionarios(nova_janela)

    def TelaFornecedores(self):
        from fornecedor import FornecedorApp
        nova_janela = ctk.CTkToplevel(self.root)
        nova_janela.grab_set()
        nova_janela.focus_force()
        FornecedorApp(nova_janela)

    def TelaProdutos(self):
        from produto import TelaProdutos
        nova_janela = ctk.CTkToplevel(self.root)
        nova_janela.grab_set()
        nova_janela.focus_force()
        TelaProdutos(nova_janela)

    def CriarUsuario(self):
        jan = ctk.CTkToplevel(self.root)
        jan.title("Cadastro de Usuário")
        jan.geometry("650x300")
        jan.configure(bg="#f6f3ec")
        jan.resizable(False, False)
        self.center_window(jan, 650, 300)
        jan.grab_set()
        jan.focus_force()

        # Frame centralizado
        form_frame = ctk.CTkFrame(jan, fg_color="transparent")
        form_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Campos do formulário
        campos = [("Usuário:", "UserNomeEntry"), ("Senha:", "SenhaEntry", True), ("Nome Completo:", "UserNomeCEntry"), ("E-mail:", "EmailEntry"),]

        for i, (label_text, entry_var, *is_password) in enumerate(campos):
            ctk.CTkLabel(form_frame, text=label_text, font=("Arial", 15)).grid(
                row=i, column=0, sticky="w", padx=10, pady=5)
            entry = ctk.CTkEntry(
                form_frame,
                width=200,
                show="•" if is_password and is_password[0] else ""
            )
            setattr(self, entry_var, entry)
            entry.grid(row=i, column=1, padx=10, pady=5)

        # Campo de tipo de usuário
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
        nome = self.UserNomeEntry.get()
        senha = self.SenhaEntry.get()
        usuario = self.UserNomeCEntry.get()
        email = self.EmailEntry.get()
        tipo = self.TipoEntry.get()

        if not nome or not senha or not usuario or not email:
            messagebox.showerror("Erro no Registro", "PREENCHA TODOS OS CAMPOS")
        else:
            db = comunicacao()
            db.RegistrarCliente(nome, senha, usuario, email, tipo) 
            messagebox.showinfo("Sucesso", "Usuário criado com sucesso!")
            self.limpar_campos()

    def limpar_campos(self):
        self.UserNomeEntry.delete(0, 'end')
        self.SenhaEntry.delete(0, 'end')
        self.UserNomeCEntry.delete(0, 'end')
        self.EmailEntry.delete(0, 'end')
        self.TipoEntry.set("Não")

    def center_window(self, window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = Menuadm(root)
    root.mainloop()