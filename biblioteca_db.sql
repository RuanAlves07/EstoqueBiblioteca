create table usuarios(

	idusuario int not null auto_increment,
	nome varchar(40),
    usuario varchar(40),
    senha varchar(40),
    userperm varchar(3),
    primary key (idusuario)

);

create table produto(

    idproduto int not null auto_increment,
    nome varchar(40),
    descricao varchar(256),
    genero varchar(1),
    quantidade int,
    preco text,
    primary key (idproduto)

);

create table fornecedor(

    idfornecedor int not null auto_increment,
    nome varchar(40),
    nomefantasia varchar(60),
    CNPJ varchar(14),
    endereco varchar(40),
    primary key (idfornecedor)

);

create table funcionario(

    idfuncionario int not null auto_increment,
    nome varchar(40),
    telefone text,
    enderecofunc text,
    email varchar(40),
    datanascimento text,
    primary key (idfuncionario)   

);

create table cliente(

    numeroNFe int not null auto_increment,
    NomeCliente text,
    QuantidadeVendas text,
    Produto text,
    DataEmissao date,
    primary key(NumeroNFe)

);