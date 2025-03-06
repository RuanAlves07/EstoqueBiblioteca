#pip install mysql-connector-python

import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "biblioteca_db"
        )
        self.cursor = self.conn.cursor() 

        print("Conectado ao banco de Dados!")

    def RegistrarNoBanco(self, nome, descricao, genero, quantidade, preco):
        self.cursor.execute("INSERT INTO produto (nome, descricao, genero, quantidade, preco) VALUES (%s, %s, %s, %s, %s)", (nome, descricao, genero, quantidade, preco )) #Insere os dados do usuário na tabela
        self.conn.commit() 