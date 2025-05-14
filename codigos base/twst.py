import customtkinter as ctk
import mysql.connector
from tkinter import messagebox


# ====== Funções do Banco ======
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="biblioteca_db"
    )


# ====== Pesquisa de Produtos ======
def pesquisar_produtos(texto, frame_resultados, entry_destino, label_qtde):
    conexao = conectar_banco()
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


# ====== Pesquisa de Clientes ======
def pesquisar_clientes(texto, frame_resultados, entry_destino):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        query = """
        SELECT NomeCliente, Produto, QuantidadeVendas, DataEmissao 
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
                command=lambda n=nome_cliente: [entry_destino.delete(0, "end"), entry_destino.insert(0, n)]
            )
            btn.pack(fill="x", pady=2)

    finally:
        cursor.close()
        conexao.close()


# ====== Dar baixa no estoque ======
def dar_baixa_estoque(nome_produto, quantidade_pedido):
    conexao = conectar_banco()
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


# ====== Adicionar Pedido ======
def adicionar_pedido(nome_cliente, quantidade, produto, metodo_pag, lista_pedidos, label_qtde, frame_tabela):
    if not nome_cliente or not quantidade.isdigit() or not produto or not metodo_pag:
        messagebox.showwarning("Dados inválidos", "Preencha todos os campos corretamente.")
        return

    sucesso = dar_baixa_estoque(produto, int(quantidade))
    if not sucesso:
        return

    pedido = [nome_cliente, quantidade, produto, metodo_pag]
    lista_pedidos.append(pedido)
    atualizar_tabela(lista_pedidos, frame_tabela)  # Agora usa o frame correto
    label_qtde.configure(text="")


# ====== Atualizar Tabela de Pedidos ======
def atualizar_tabela(lista_pedidos, frame_tabela):
    for widget in frame_tabela.winfo_children():
        widget.destroy()

    headers = ["Cliente", "Quantidade", "Produto", "Pagamento"]
    for col, texto in enumerate(headers):
        lbl = ctk.CTkLabel(frame_tabela, text=texto, font=("Arial", 12, "bold"))
        lbl.grid(row=0, column=col, padx=5, pady=5)

    for linha, pedido in enumerate(lista_pedidos, start=1):
        for col, valor in enumerate(pedido):
            lbl = ctk.CTkLabel(frame_tabela, text=str(valor))
            lbl.grid(row=linha, column=col, padx=5, pady=2)


# ====== Janela de Pesquisa de Produto ======
def abrir_janela_pesquisa_produto(entry_produto, root, label_qtde_estoque):
    janela_pesquisa = ctk.CTkToplevel(root)
    janela_pesquisa.title("Pesquisar Produto")
    janela_pesquisa.geometry("600x300")

    entry_pesquisa = ctk.CTkEntry(janela_pesquisa, placeholder_text="Nome ou descrição do produto...")
    entry_pesquisa.pack(pady=10, padx=20, fill="x")

    frame_resultados = ctk.CTkFrame(janela_pesquisa)
    frame_resultados.pack(pady=10, padx=20, fill="both", expand=True)

    def atualizar(event=None):
        pesquisar_produtos(entry_pesquisa.get(), frame_resultados, entry_produto, label_qtde_estoque)

    entry_pesquisa.bind("<KeyRelease>", atualizar)
    janela_pesquisa.grab_set()


# ====== Janela de Pesquisa de Cliente ======
def abrir_janela_pesquisa_cliente(entry_cliente, root):
    janela_pesquisa = ctk.CTkToplevel(root)
    janela_pesquisa.title("Pesquisar Cliente")
    janela_pesquisa.geometry("600x300")

    entry_pesquisa = ctk.CTkEntry(janela_pesquisa, placeholder_text="Nome do Cliente...")
    entry_pesquisa.pack(pady=10, padx=20, fill="x")

    frame_resultados = ctk.CTkFrame(janela_pesquisa)
    frame_resultados.pack(pady=10, padx=20, fill="both", expand=True)

    def atualizar(event=None):
        pesquisar_clientes(entry_pesquisa.get(), frame_resultados, entry_cliente)

    entry_pesquisa.bind("<KeyRelease>", atualizar)
    janela_pesquisa.grab_set()


# ====== Interface Gráfica ======
def criar_tela_pedidos():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Cadastro de Pedidos")
    root.geometry("900x600")

    lista_pedidos = []

    # Frame centralizado
    frame_central = ctk.CTkFrame(root)
    frame_central.pack(expand=True, fill="both", padx=20, pady=20)

    # Frame Cadastro
    frame_cadastro = ctk.CTkFrame(frame_central)
    frame_cadastro.pack(pady=10)

    # Campos centrados
    ctk.CTkLabel(frame_cadastro, text="Nome do Cliente:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_cliente = ctk.CTkEntry(frame_cadastro, width=250, justify="center")
    entry_cliente.grid(row=0, column=1, padx=5, pady=5)
    btn_pesquisar_cliente = ctk.CTkButton(
        frame_cadastro,
        text="🔍",
        width=30,
        command=lambda: abrir_janela_pesquisa_cliente(entry_cliente, root)
    )
    btn_pesquisar_cliente.grid(row=0, column=2, padx=5)

    ctk.CTkLabel(frame_cadastro, text="Quantidade:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_qtde = ctk.CTkEntry(frame_cadastro, width=250, justify="center")
    entry_qtde.grid(row=1, column=1, padx=5, pady=5)

    ctk.CTkLabel(frame_cadastro, text="Produto:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_produto_selecionado = ctk.CTkEntry(frame_cadastro, width=250, justify="center")
    entry_produto_selecionado.grid(row=2, column=1, padx=5, pady=5)
    btn_pesquisar_produto = ctk.CTkButton(
        frame_cadastro,
        text="🔍",
        width=30,
        command=lambda: abrir_janela_pesquisa_produto(entry_produto_selecionado, root, label_qtde_estoque)
    )
    btn_pesquisar_produto.grid(row=2, column=2, padx=5)

    label_qtde_estoque = ctk.CTkLabel(frame_cadastro, text="", text_color="gray")
    label_qtde_estoque.grid(row=3, column=1)

    ctk.CTkLabel(frame_cadastro, text="Método de Pagamento:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    opcoes_pag = ["Cartão de Crédito", "Boleto Bancário", "Pix", "Transferência"]
    combo_pag = ctk.CTkComboBox(frame_cadastro, values=opcoes_pag, width=250, justify="center")
    combo_pag.grid(row=4, column=1, padx=5, pady=5)

    btn_salvar = ctk.CTkButton(
        frame_cadastro,
        text="Salvar Pedido",
        command=lambda: adicionar_pedido(
            entry_cliente.get(),
            entry_qtde.get(),
            entry_produto_selecionado.get(),
            combo_pag.get(),
            lista_pedidos,
            label_qtde_estoque,
            frame_tabela_pedidos  # Passa o frame diretamente
    )
)
    btn_salvar.grid(row=5, column=0, columnspan=3, pady=10)

    # Tabela de Pedidos Recentemente Feitos
    frame_tabela_pedidos = ctk.CTkFrame(frame_central)
    frame_tabela_pedidos.pack(fill="both", expand=True, padx=20, pady=10)

    root.mainloop()


# Executar Aplicação
if __name__ == "__main__":
    criar_tela_pedidos()