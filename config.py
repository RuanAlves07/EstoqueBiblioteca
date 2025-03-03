
import mysql.connector # Importa o modulo mysql.connector para conectar ao banco de dados MYSQL

class Config:
    def __init__(self):
        # Conecta ao banco de dados MySQL com as credencias fornecidas
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "biblioteca_db"

        )
        self.cursor = self.conn.cursor() # Cria um cursor para exucutar comando SQL
        # Cria a tabela "Usuario" se ela não existir
        self.cursor.execute ('''CREATE TABLE IF NOT EXISTS USUARIO(
                             idUsuario int AUTO_INCREMENT PRIMARY KEY,
                             nome TEXT (255),
                             email TEXT (255),
                             usuario TEXT (255),
                             senha TEXT (255)
                             );''')
        self.conn.commit() # Confirma a criação da tabela 
        print ("Conectado ao Banco de Dados") # Imprime uma mensagem de confirmação

    # Metódo para registrar um novo usuario no banco de dados
    def RegistrarNoBanco(self, nome, email, usuario, senha):
        self.cursor.execute("INSERT INTO usuario (nome, email, usuario, senha) VALUES (%s ,%s ,%s ,%s)",
                            (nome,email,usuario,senha)) # Insere os dados do usuario na tabela
        self.conn.commit() # Confirma a inseção dos dados

    # Metodo para alterar os dados de um usuario existente no banco de dados
    def alterar (self, IdUsuario, nome, email, usuario, senha):
        self.conn.execute("UPDATE usuario SET nome=%s, email=%s, usuario=%s, senha=%s WHERE IdUsuario=%s",(nome, email, usuario, senha, IdUsuario)) # Atualiza os dados do usuario com o id fornecido
        self.conn.commit() # Confirma a atualização dos dados

    # Metodo para excluir um usuario do banco de dados
    def excluir (self, IdUsuario) :
        self.cursor.execute ("DELETE FROM usuario WHERE IdUsuario = %s", (IdUsuario,)) # Excluir o usuario com idusuario
        self.conn.commit() # Confirma a exclusão dos dados

    # Metodo para buscar os dados de um usuario no banco de dados
    def buscar(self, IdUsuario):
        self.cursor.execute("SELECT * FROM usuario WHERE IdUsuario= %s", (IdUsuario,)) # Seleciona os dados do usuario com o id fornecido
        return self.cursor.fetchone() # Retorna os dados do usuario encontrado
    
    # Metodo chama quando a instancia da classe é destruida
    def __del__(self):
        self.conn.close() # Fecha a conexão com o banco de dados
