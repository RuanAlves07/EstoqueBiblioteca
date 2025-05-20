create table usuarios(

	idusuario int not null auto_increment,
	nome varchar(40),
    usuario varchar(40),
    senha varchar(40),
    email varchar(60),
    userperm varchar(3),
    primary key (idusuario)

);

create table fornecedor(

    idfornecedor int not null auto_increment,
    nome varchar(40),
    nomefantasia varchar(60),
    CNPJ varchar(20),
    primary key (idfornecedor)

);

create table produto(

    idproduto int not null auto_increment,
    idfornecedor int,
    nome varchar(40),
    descricao varchar(256),
    genero varchar(1),
    quantidade int,
    preco text,
    primary key (idproduto),
    FOREIGN KEY (idfornecedor) REFERENCES fornecedor(idfornecedor)

);

create table funcionario(

    idfuncionario int not null auto_increment,
    nome varchar(40),
    telefone text,
    email varchar(40),
    datanascimento text,
    primary key (idfuncionario)   

);

create table cliente(

 idcliente int not null auto_increment,
 NomeCliente text,
 CNPJ varchar(20),
 primary key (idcliente)

);

CREATE TABLE endereco (
    idendereco INT AUTO_INCREMENT PRIMARY KEY,
    rua VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    estado CHAR(2)
    
);

CREATE TABLE venda (
    idvenda INT AUTO_INCREMENT PRIMARY KEY,
    idcliente INT,
    idproduto INT,
    data_venda DATE,
    quantidade INT,
    valor_total DECIMAL(10,2),
    idusuario INT,
    FOREIGN KEY (idcliente) REFERENCES cliente(idcliente),
    FOREIGN KEY (idproduto) REFERENCES produto(idproduto),
    FOREIGN KEY (idusuario) REFERENCES usuarios(idusuario)
);

ALTER TABLE produto ADD FOREIGN KEY (idfornecedor) REFERENCES fornecedor(idfornecedor);

ALTER TABLE cliente ADD COLUMN idendereco INT;
ALTER TABLE cliente ADD FOREIGN KEY (idendereco) REFERENCES endereco(idendereco);

ALTER TABLE fornecedor ADD COLUMN idendereco INT;
ALTER TABLE fornecedor ADD FOREIGN KEY (idendereco) REFERENCES endereco(idendereco);

ALTER TABLE funcionario ADD COLUMN idendereco INT;
ALTER TABLE funcionario ADD FOREIGN KEY (idendereco) REFERENCES endereco(idendereco);