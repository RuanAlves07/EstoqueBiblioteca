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

    def ExcluirProduto(self, idproduto):
        self.cursor.execute("DELETE FROM produto WHERE idproduto = %s",(idproduto)) 
        self.conn.commit()

    def AtualizarProduto(self, idproduto, nome, descricao, genero, quantidade, preco):
        self.cursor.execute("UPDATE produto SET nome = %s, descricao = %s, genero = %s, quantidade = %s, preco = %s WHERE idproduto = %s ",(idproduto, nome, descricao, genero, quantidade, preco)) 
        self.conn.commit() 

    def ListarProduto(self, idproduto):
        self.cursor.execute("SELECT * FROM produto WHERE idproduto = %s", (idproduto)) 
        return self.cursor.fetchone() 
    
    def RegistrarFornecedor(self, nome, nomefantasia, CNPJ, endereco):
        self.cursor.execute("INSERT INTO fornecedor (nome, nomefantasia, CNPJ, endereco) VALUES (%s, %s, %s, %s)",(nome, nomefantasia, CNPJ, endereco))
        self.conn.commit()

    def ExcluirFornecedor(self, idfornecedor):
        self.cursor.execute("DELETE FROM fornecedor WHERE idfornecedor = %s",(idfornecedor))    
        self.conn.commit()

    def AtualizarFornecedor(self, idfornecedor, nome, nomefantasia, CNPJ, endereco):
        self.cursor.execute("UPDATE produto SET nome = %s, nomefantasia = %s, CNPJ = %s, endereco = %s WHERE idfornecedor = %s ",(idfornecedor, nome, nomefantasia, CNPJ, endereco)) 
        self.conn.commit()
    
    def ListarFornecedor(self, idfornecedor):
        self.cursor.execute("SELECT * FROM fornecedor WHERE idfornecedor = %s", (idfornecedor)) 
        return self.cursor.fetchone() 
        



