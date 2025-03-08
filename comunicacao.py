#pip install mysql-connector-python

import mysql.connector

class comunicacao:
    def __init__(self):
       
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "biblioteca_db"
        )
        self.cursor = self.conn.cursor()

    def RegistrarProduto(self, nome, descricao, genero, quantidade, preco):
        self.cursor.execute("INSERT INTO produto (nome, descricao, genero, quantidade, preco) VALUES (%s, %s, %s, %s, %s)", (nome, descricao, genero, quantidade, preco))
        self.conn.commit() 
    
        



