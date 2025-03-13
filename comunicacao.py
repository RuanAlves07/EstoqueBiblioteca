#pip install mysql-connector-python

import mysql.connector

class comunicacao:
    def __init__(self):
       
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "biblioteca_db"
        )
        self.cursor = self.conn.cursor()
            
    def RegistrarProduto(self, nome, descricao, genero, quantidade, preco):
        self.cursor.execute("INSERT INTO produto (nome, descricao, genero, quantidade, preco) VALUES (%s, %s, %s, %s, %s)", (nome, descricao, genero, quantidade, preco))
        self.conn.commit() 

    def ExcluirProduto(self, idproduto):
        self.cursor.execute("DELETE FROM produto WHERE idproduto = %s",(idproduto)) 
        self.conn.commit()
    
    def carregar_produto(self):
        self.cursor.execute("SELECT idproduto, nome, descricao, genero, quantidade, preco FROM usuario")
        produtos = self.cursor.fetchall()
        return produtos

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
        query = "DELETE FROM fornecedor WHERE idfornecedor = %s"
        self.cursor.execute(query, (idfornecedor,))  # Note a vírgula após idfornecedor
        self.conn.commit()

    def carregar_fornecedores(self):
        self.cursor.execute("SELECT idfornecedor, nome, nomefantasia, CNPJ, endereco FROM fornecedor")
        fornecedores = self.cursor.fetchall()
        return fornecedores
    
    def buscar_fornecedor_por_id(self, idfornecedor):
        self.cursor.execute("SELECT * FROM fornecedor WHERE idfornecedor = %s", (idfornecedor,))
        return self.cursor.fetchone()  # Retorna uma tupla com os dados do fornecedor
        
    def AtualizarFornecedor(self, idfornecedor, nome, nomefantasia, CNPJ, endereco):
        query = "UPDATE fornecedor SET nome = %s, nomefantasia = %s, CNPJ = %s, endereco = %s WHERE idfornecedor = %s "
        self.cursor.execute(query, (nome, nomefantasia, CNPJ, endereco, idfornecedor))
        self.conn.commit()
        
    def ListarFornecedor(self, idfornecedor):
        self.cursor.execute("SELECT * FROM fornecedor WHERE idfornecedor = %s", (idfornecedor)) 
        return self.cursor.fetchone() 
    
    def RegistrarFuncionario(self, nome, telefone, enderecofunc, email, datanascimento):
        self.cursor.execute("INSERT INTO funcionario (nome, telefone, enderecofunc, email, datanascimento) VALUES (%s, %s, %s, %s, %s)", (nome, telefone, enderecofunc, email, datanascimento))
        self.conn.commit() 

    def ExcluirFuncionario(self, idfuncionario):
        
        try:
            query = "DELETE FROM funcionario WHERE idfuncionario = %s"
            self.cursor.execute(query, idfuncionario)
            self.conn.commit()
            print("Funcionário excluído com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao excluir funcionário: {err}")
        finally:
            self.cursor.close()
            self.conn.close()

    def carregar_funcionario(self):
        self.cursor.execute("SELECT idfuncionario, nome, telefone, enderecofunc, email, data_nascimento FROM funcionario")
        self.conn.commit()


    def AtualizarFuncionario(self, idfuncionario, nome, telefone, enderecofunc, email, datanascimento):
        self.cursor.execute("UPDATE funcionario SET nome = %s, telefone = %s, enderecofunc = %s, email = %s, datanascimento = %s WHERE idfuncionario = %s ",(idfuncionario, nome, telefone, enderecofunc, email, datanascimento)) 
        self.conn.commit() 

    def ListarFuncionario(self, idfuncionario):
        self.cursor.execute("SELECT * FROM funcionario WHERE idfuncionario = %s", (idfuncionario)) 
        return self.cursor.fetchone() 
    
    def buscar_funcionario_por_id(self, idfuncionario):
        self.cursor.execute("SELECT * FROM funcionario WHERE idfuncionario = %s", (idfuncionario,))
        return self.cursor.fetchone()  # Retorna uma tupla com os dados do fornecedor
    



