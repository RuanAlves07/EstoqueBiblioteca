#pip install mysql-connector-python

import mysql.connector


#Login
class login:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "biblioteca_db"
        )
        self.cursor = self.conn.cursor() 

    def RegistrarNoBanco(self, nome, senha, email, telefone):
        self.cursor.execute("INSERT INTO usuario (nome, senha, email, telefone) VALUES (%s, %s, %s, %s)", (nome, senha, email, telefone)) 
        self.conn.commit()

    
        



