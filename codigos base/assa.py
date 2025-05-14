import customtkinter as ctk
import mysql.connector
from tkinter import messagebox


# Configuração do Banco de Dados
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Substitua pelo seu usuário
        password="",  # Substitua pela sua senha
        database="biblioteca_db"  # Substitua pelo nome do seu banco
    )


# Função de Pesquisa
def pesquisar_fornecedor(entry_pesquisa, tabela):
    texto = entry_pesquisa.get().strip()
    if not texto:
        messagebox.showwarning("Campo Vazio", "Digite algo para pesquisar.")
        return

    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        query = """
        SELECT idfornecedor, nome, nomefantasia, CNPJ, endereco 
        FROM fornecedor 
        WHERE nome LIKE %s OR nomefantasia LIKE %s OR CNPJ LIKE %s
        """
        parametro = f"%{texto}%"
        cursor.execute(query, (parametro, parametro, parametro))
        resultados = cursor.fetchall()

        # Limpa a tabela antes de atualizar
        for widget in tabela.winfo_children():
            widget.destroy()

        # Cabeçalho da tabela
        headers = ["ID", "Nome", "Nome Fantasia", "CNPJ", "Endereço"]
        for col, header in enumerate(headers):
            lbl = ctk.CTkLabel(tabela, text=header, font=("Arial", 12, "bold"))
            lbl.grid(row=0, column=col, padx=5, pady=5)

        # Resultados da pesquisa
        for linha, row in enumerate(resultados, start=1):
            for col, valor in enumerate(row):
                lbl = ctk.CTkLabel(tabela, text=str(valor))
                lbl.grid(row=linha, column=col, padx=5, pady=2)

        if not resultados:
            messagebox.showinfo("Sem Resultados", "Nenhum fornecedor encontrado.")

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao pesquisar: {e}")
    finally:
        cursor.close()
        conexao.close()


# Interface Gráfica
def criar_app():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Pesquisa de Fornecedores")
    root.geometry("800x400")

    # Barra de Pesquisa
    frame_pesquisa = ctk.CTkFrame(root)
    frame_pesquisa.pack(pady=10, padx=20, fill="x")

    label_pesquisa = ctk.CTkLabel(frame_pesquisa, text="Pesquisar:")
    label_pesquisa.pack(side="left", padx=5)

    entry_pesquisa = ctk.CTkEntry(frame_pesquisa, placeholder_text="Nome, CNPJ ou Nome Fantasia...")
    entry_pesquisa.pack(side="left", expand=True, fill="x", padx=5)

    btn_pesquisar = ctk.CTkButton(
        frame_pesquisa,
        text="🔍",
        width=40,
        command=lambda: pesquisar_fornecedor(entry_pesquisa, frame_tabela)
    )
    btn_pesquisar.pack(side="left", padx=5)

    # Tabela de Resultados
    frame_tabela = ctk.CTkFrame(root)
    frame_tabela.pack(pady=10, padx=20, fill="both", expand=True)

    root.mainloop()


# Executar Aplicação
if __name__ == "__main__":
    criar_app()