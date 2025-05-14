import customtkinter as ctk
import mysql.connector
from tkinter import messagebox


class AppPedidos:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Pedidos")
        self.root.geometry("900x600")

        self.lista_pedidos = []

        # Frame centralizado
        self.frame_central = ctk.CTkFrame(self.root)
        self.frame_central.pack(expand=True, fill="both", padx=20, pady=20)

        self.criar_interface()

    def conectar_banco(self):
        try:
            return mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="biblioteca_db"
            )
        except mysql.connector.Error as err:
            messagebox.showerror("Erro de Banco", f"Não foi possível conectar ao banco: {err}")
            raise

    def pesquisar_produtos(self, texto, frame_resultados, entry_destino, label_qtde):
        conexao = self.conectar_banco()
        cursor = conexao.cursor()

        try:
            query = """
            SELECT idproduto, nome, descricao, quantidade, preco 
            FROM produto 
            WHERE nome LIKE %s OR descricao LIKE %s
            """
            parametro = f"%{texto}%"
            cursor.execute(query, (parametro, parametro))
            resultados = cursor.fetchall()

            for widget in frame_resultados.winfo_children():
                widget.destroy()

            if not texto.strip():
                label_qtde.configure(text="")
                return

            for idx, prod in enumerate(resultados):
                idprod, nome, desc, qtde, preco = prod
                texto_prod = f"{nome} - {desc} | R$ {float(preco):.2f} | Estoque: {qtde}"

                btn = ctk.CTkButton(
                    frame_resultados,
                    text=texto_prod,
                    anchor="w",
                    command=lambda n=nome, q=qtde: [
                        entry_destino.delete(0, "end"),
                        entry_destino.insert(0, n),
                        label_qtde.configure(text=f"Estoque disponível: {q}")
                    ]
                )
                btn.pack(fill="x", pady=2)

        finally:
            cursor.close()
            conexao.close()

    def pesquisar_clientes(self, texto, frame_resultados, entry_destino):
        conexao = self.conectar_banco()
        cursor = conexao.cursor()

        try:
            query = """
            SELECT NomeCliente, Produto, QuantidadeCompras, DataEmissao 
            FROM cliente 
            WHERE NomeCliente LIKE %s
            """
            parametro = f"%{texto}%"
            cursor.execute(query, (parametro,))
            resultados = cursor.fetchall()

            for widget in frame_resultados.winfo_children():
                widget.destroy()

            if not texto.strip():
                return

            for cli in resultados:
                nome_cliente, produto, qtde_venda, data_emissao = cli
                texto_cli = f"{nome_cliente} - Última compra: {produto}, Qtde: {qtde_venda}, Data: {data_emissao}"

                btn = ctk.CTkButton(
                    frame_resultados,
                    text=texto_cli,
                    anchor="w",
                    command=lambda n=nome_cliente: [
                        entry_destino.delete(0, "end"),
                        entry_destino.insert(0, n)
                    ]
                )
                btn.pack(fill="x", pady=2)

        finally:
            cursor.close()
            conexao.close()

    def dar_baixa_estoque(self, nome_produto, quantidade_pedido):
        conexao = self.conectar_banco()
        cursor = conexao.cursor()

        try:
            cursor.execute("SELECT idproduto, quantidade FROM produto WHERE nome = %s", (nome_produto,))
            resultado = cursor.fetchone()

            if not resultado:
                raise Exception(f"Produto '{nome_produto}' não encontrado.")

            idproduto, estoque_atual = resultado

            if quantidade_pedido > estoque_atual:
                raise Exception(f"Estoque insuficiente para '{nome_produto}'. Disponível: {estoque_atual}")

            cursor.execute(
                "UPDATE produto SET quantidade = quantidade - %s WHERE idproduto = %s",
                (quantidade_pedido, idproduto)
            )
            conexao.commit()
            return True

        except Exception as e:
            messagebox.showerror("Erro", str(e))
            return False

        finally:
            cursor.close()
            conexao.close()

    def adicionar_pedido(self, nome_cliente, quantidade, produto, metodo_pag, label_qtde):
        if not nome_cliente or not quantidade.isdigit() or not produto or not metodo_pag:
            messagebox.showwarning("Dados inválidos", "Preencha todos os campos corretamente.")
            return

        sucesso = self.dar_baixa_estoque(produto, int(quantidade))
        if not sucesso:
            return

        pedido = [nome_cliente, quantidade, produto, metodo_pag]
        self.lista_pedidos.append(pedido)
        self.atualizar_tabela()
        label_qtde.configure(text="")

    def atualizar_tabela(self):
        for widget in self.frame_tabela_pedidos.winfo_children():
            widget.destroy()

        headers = ["Cliente", "Quantidade", "Produto", "Pagamento"]
        for col, texto in enumerate(headers):
            lbl = ctk.CTkLabel(self.frame_tabela_pedidos, text=texto, font=("Arial", 12, "bold"))
            lbl.grid(row=0, column=col, padx=5, pady=5)

        for linha, pedido in enumerate(self.lista_pedidos, start=1):
            for col, valor in enumerate(pedido):
                lbl = ctk.CTkLabel(self.frame_tabela_pedidos, text=str(valor))
                lbl.grid(row=linha, column=col, padx=5, pady=2)

    def abrir_janela_pesquisa_produto(self, entry_produto, label_qtde_estoque):
        janela_pesquisa = ctk.CTkToplevel(self.root)
        janela_pesquisa.title("Pesquisar Produto")
        janela_pesquisa.geometry("600x300")

        entry_pesquisa = ctk.CTkEntry(janela_pesquisa, placeholder_text="Nome ou descrição do produto...")
        entry_pesquisa.pack(pady=10, padx=20, fill="x")

        frame_resultados = ctk.CTkFrame(janela_pesquisa)
        frame_resultados.pack(pady=10, padx=20, fill="both", expand=True)

        def atualizar(event=None):
            self.pesquisar_produtos(entry_pesquisa.get(), frame_resultados, entry_produto, label_qtde_estoque)

        entry_pesquisa.bind("<KeyRelease>", atualizar)
        janela_pesquisa.grab_set()

    def abrir_janela_pesquisa_cliente(self, entry_cliente):
        janela_pesquisa = ctk.CTkToplevel(self.root)
        janela_pesquisa.title("Pesquisar Cliente")
        janela_pesquisa.geometry("600x300")

        entry_pesquisa = ctk.CTkEntry(janela_pesquisa, placeholder_text="Nome do Cliente...")
        entry_pesquisa.pack(pady=10, padx=20, fill="x")

        frame_resultados = ctk.CTkFrame(janela_pesquisa)
        frame_resultados.pack(pady=10, padx=20, fill="both", expand=True)

        def atualizar(event=None):
            self.pesquisar_clientes(entry_pesquisa.get(), frame_resultados, entry_cliente)

        entry_pesquisa.bind("<KeyRelease>", atualizar)
        janela_pesquisa.grab_set()

    def criar_interface(self):
        self.frame_cadastro = ctk.CTkFrame(self.frame_central)
        self.frame_cadastro.pack(pady=10)

        # Campos centrados
        ctk.CTkLabel(self.frame_cadastro, text="Nome do Cliente:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_cliente = ctk.CTkEntry(self.frame_cadastro, width=250, justify="center")
        self.entry_cliente.grid(row=0, column=1, padx=5, pady=5)
        btn_pesquisar_cliente = ctk.CTkButton(
            self.frame_cadastro,
            text="🔍",
            width=30,
            command=lambda: self.abrir_janela_pesquisa_cliente(self.entry_cliente)
        )
        btn_pesquisar_cliente.grid(row=0, column=2, padx=5)

        ctk.CTkLabel(self.frame_cadastro, text="Quantidade:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_qtde = ctk.CTkEntry(self.frame_cadastro, width=250, justify="center")
        self.entry_qtde.grid(row=1, column=1, padx=5, pady=5)

        ctk.CTkLabel(self.frame_cadastro, text="Produto:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_produto_selecionado = ctk.CTkEntry(self.frame_cadastro, width=250, justify="center")
        self.entry_produto_selecionado.grid(row=2, column=1, padx=5, pady=5)
        btn_pesquisar_produto = ctk.CTkButton(
            self.frame_cadastro,
            text="🔍",
            width=30,
            command=lambda: self.abrir_janela_pesquisa_produto(self.entry_produto_selecionado, self.label_qtde_estoque)
        )
        btn_pesquisar_produto.grid(row=2, column=2, padx=5)

        self.label_qtde_estoque = ctk.CTkLabel(self.frame_cadastro, text="", text_color="gray")
        self.label_qtde_estoque.grid(row=3, column=1)

        ctk.CTkLabel(self.frame_cadastro, text="Método de Pagamento:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        opcoes_pag = ["Cartão de Crédito", "Boleto Bancário", "Pix", "Transferência"]
        self.combo_pag = ctk.CTkComboBox(self.frame_cadastro, values=opcoes_pag, width=250, justify="center")
        self.combo_pag.grid(row=4, column=1, padx=5, pady=5)

        btn_salvar = ctk.CTkButton(
            self.frame_cadastro,
            text="Salvar Pedido",
            command=lambda: self.adicionar_pedido(
                self.entry_cliente.get(),
                self.entry_qtde.get(),
                self.entry_produto_selecionado.get(),
                self.combo_pag.get(),
                self.label_qtde_estoque
            )
        )
        btn_salvar.grid(row=5, column=0, columnspan=3, pady=10)

        # Tabela de Pedidos Recentemente Feitos
        self.frame_tabela_pedidos = ctk.CTkFrame(self.frame_central)
        self.frame_tabela_pedidos.pack(fill="both", expand=True, padx=20, pady=10)


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app_root = ctk.CTk()
    AppPedidos(app_root)
    app_root.mainloop()