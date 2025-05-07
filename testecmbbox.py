import customtkinter as ctk
import sqlite3

# -----------------------------
# Função para buscar fornecedores no banco
def fornecedores12():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Insere alguns dados de exemplo (caso esteja vazio)
    cursor.execute("SELECT COUNT(*) FROM fornecedores")
    if cursor.fetchone()[0] == 0:
        exemplos = [("Fornecedor A",), ("Fornecedor B",), ("Fornecedor C",)]
        cursor.executemany("INSERT INTO fornecedores (nome) VALUES (?)", exemplos)
        conn.commit()

    # Busca os nomes dos fornecedores
    cursor.execute("SELECT nome FROM fornecedores")
    resultados = cursor.fetchall()
    conn.close()

    return [nome[0] for nome in resultados]

# -----------------------------
# Configuração da interface
ctk.set_appearance_mode("System")  # Modo claro/escuro do sistema
ctk.set_default_color_theme("blue")  # Tema azul

app = ctk.CTk()  # Cria a janela principal
app.title("Exemplo ComboBox com Banco")
app.geometry("400x300")

# Frame para organizar os widgets
form_frame = ctk.CTkFrame(app)
form_frame.pack(padx=20, pady=50, fill="both", expand=True)

# Label
label = ctk.CTkLabel(form_frame, text="Selecione um Fornecedor:")
label.pack(pady=10)

# ComboBox
combo = ctk.CTkComboBox(
    form_frame,
    values=fornecedores12(),  # Carrega os valores do banco
    width=200,
    state="readonly"
)
combo.pack(pady=10)

# Inicia o loop da interface
app.mainloop()