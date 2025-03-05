import tkinter as tk
from tkinter import messagebox
from comunicacao import criar_produto, atualizar_produto, listar_produto, deletar_produto

class CRUDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PRODUTOS")
        
        self.create_widgets()
    