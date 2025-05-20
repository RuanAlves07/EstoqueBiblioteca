# pip install mysql-connector-python - Comunicação com o BD
# pip3 install customtkinter - Comunicação com customtkinter, front end
# python -m pip install -U pip - Comunicação com a Dasboard e BD
# python -m pip install -U matplotlib - Geração dos graficos
# pip install pillow - Biblioteca para imagens (Obrigatorio para tela de login)
# pip install CTkMenuBar - Funcionalidade da barra de navegação


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

    def RegistrarCliente(self,  NomeCliente, cnpj, endereco):
        self.cursor.execute("INSERT INTO cliente ( NomeCliente, CNPJ, endereco) VALUES (%s, %s, %s)", ( NomeCliente, cnpj, endereco))
        self.conn.commit() 

    def RegistrarUsuario(self, nome, usuario, senha, email, userperm):
        self.cursor.execute("INSERT INTO usuarios ( nome, usuario, senha, email, userperm) VALUES (%s, %s, %s, %s, %s)", ( nome, usuario, senha, email, userperm))
        self.conn.commit() 

    def RegistrarProduto(self, idfornecedor, nome, descricao, genero, quantidade, preco):
        self.cursor.execute("""INSERT INTO produto (idfornecedor, nome, descricao, genero, quantidade, preco)VALUES (%s, %s, %s, %s, %s, %s) """, (idfornecedor, nome, descricao, genero, quantidade, preco))
        self.conn.commit()

    def ExcluirProduto(self, idproduto):
        self.cursor.execute("DELETE FROM produto WHERE idproduto = %s", (idproduto,)) 
        self.conn.commit()
    
    def carregar_produto(self):
        self.cursor.execute("SELECT idproduto, nome, descricao, genero, quantidade, preco FROM produto")
        produtos = self.cursor.fetchall()
        return produtos

    def AtualizarProduto(self, idproduto, nome, descricao, genero, quantidade, preco):
        self.cursor.execute("UPDATE produto SET nome = %s, descricao = %s, genero = %s, quantidade = %s, preco = %s WHERE idproduto = %s ",(nome, descricao, genero, quantidade, preco, idproduto)) 
        self.conn.commit() 

    def ListarProduto(self, idproduto):
        self.cursor.execute("SELECT * FROM produto WHERE idproduto = %s", (idproduto,)) 
        return self.cursor.fetchone() 
    
    def PuxarProdutoPorID(self, idproduto):
        self.cursor.execute("SELECT * FROM produto WHERE idproduto = %s", (idproduto,))
        return self.cursor.fetchone()
    
    def RegistrarFornecedor(self, nome, nomefantasia, CNPJ, idendereco):
        self.cursor.execute("""INSERT INTO fornecedor (nome, nomefantasia, CNPJ, idendereco) VALUES (%s, %s, %s, %s)""", (nome, nomefantasia, CNPJ, idendereco))
        self.conn.commit()

    def ExcluirFornecedor(self, idfornecedor):
        query = "DELETE FROM fornecedor WHERE idfornecedor = %s"
        self.cursor.execute(query, (idfornecedor,))  
        self.conn.commit()

    def carregar_fornecedores_com_endereco(self):
        query = """SELECT f.idfornecedor, f.nome, f.nomefantasia, f.CNPJ, e.rua, e.bairro, e.cidade, e.estado FROM fornecedor f LEFT JOIN endereco e ON f.idendereco = e.idendereco"""
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def buscar_fornecedor_por_id(self, idfornecedor):
        self.cursor.execute("SELECT * FROM fornecedor WHERE idfornecedor = %s", (idfornecedor,))
        return self.cursor.fetchone()  
        
    def AtualizarFornecedor(self, idfornecedor, nome, nomefantasia, CNPJ):
        self.cursor.execute("""UPDATE fornecedor SET nome = %s, nomefantasia = %s, CNPJ = %s WHERE idfornecedor = %s""", (nome, nomefantasia, CNPJ, idfornecedor))
        self.conn.commit()

    def AtualizarEndereco(self, rua, bairro, cidade, estado, idfornecedor):
        self.cursor.execute("""UPDATE endereco SET rua = %s, bairro = %s, cidade = %s, estado = %s WHERE idendereco = (SELECT idendereco FROM fornecedor WHERE idfornecedor = %s)""", (rua, bairro, cidade, estado, idfornecedor))  # Ordem correta dos parâmetros
        self.conn.commit()

    def ListarFornecedor(self, idfornecedor):
        self.cursor.execute("SELECT * FROM fornecedor WHERE idfornecedor = %s", (idfornecedor)) 
        return self.cursor.fetchone() 
    
    def RegistrarFuncionario(self, nome, telefone, email, datanascimento):
        self.cursor.execute("INSERT INTO funcionario (nome, telefone, email, datanascimento) VALUES (%s, %s, %s, %s, %s)", (nome, telefone, email, datanascimento))
        self.conn.commit() 

    def ExcluirFuncionario(self, idfuncionario):
        
        self.cursor.execute("DELETE FROM funcionario WHERE idfuncionario = %s", (idfuncionario,)) 
        self.conn.commit()

    def carregar_funcionario(self):
        self.cursor.execute("SELECT idfuncionario, nome, telefone, email, data_nascimento FROM funcionario")
        self.conn.commit()

    def AtualizarFuncionario(self, idfuncionario, nome, telefone, email, datanascimento):
        self.cursor.execute("UPDATE funcionario SET nome = %s, telefone = %s,  email = %s, datanascimento = %s WHERE idfuncionario = %s ",(nome, telefone, email, datanascimento,idfuncionario)) 
        self.conn.commit() 

    def ListarFuncionario(self, idfuncionario):
        self.cursor.execute("SELECT * FROM funcionario WHERE idfuncionario = %s", (idfuncionario)) 
        return self.cursor.fetchone() 
    
    def buscar_funcionario_por_id(self, idfuncionario):
        self.cursor.execute("SELECT * FROM funcionario WHERE idfuncionario = %s", (idfuncionario,))
        return self.cursor.fetchone()  
 
    def fornecedores12(self):
        self.cursor.execute("SELECT nome FROM fornecedor")
        self.conn.commit() 

    def buscar_cliente_por_id(self, idcliente):
        self.cursor.execute("SELECT * FROM cliente WHERE idcliente = %s", (idcliente,))
        return self.cursor.fetchone()  
    
    def AtualizarCliente(self, idcliente, NomeCliente, CNPJ, endereço,):
        self.cursor.execute("UPDATE cliente SET idcliente = %s, NomeCliente = %s, CNPJ = %s, quantidade = %s, endereço = %s WHERE idproduto = %s ",(idcliente, NomeCliente, CNPJ, endereço)) 
        self.conn.commit() 

    def LinkEndereco(self, rua, bairro, cidade, estado):
        self.cursor.execute("""INSERT INTO endereco (rua, bairro, cidade, estado) VALUES (%s, %s, %s, %s)""", (rua, bairro, cidade, estado))
        self.conn.commit()
    
    def AtualizarEnderecoFunc(self, rua, bairro, cidade, estado, idfuncionario):
        self.cursor.execute("""
            UPDATE endereco 
            SET rua = %s, bairro = %s, cidade = %s, estado = %s 
            WHERE idendereco = (
                SELECT idendereco FROM funcionario 
                WHERE idfuncionario = %s
            )
        """, (rua, bairro, cidade, estado, idfuncionario))  # Ordem correta dos parâmetros
        self.conn.commit()
