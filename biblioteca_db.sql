create table login(

	idusuario int not null auto_increment,
	nome text,
    usuario text,
    senha text,
    endereco text,
    telefone text,
    primary key (idusuario)

);

create table produtos(

    idproduto int not null auto_increment,
    nome text,
    descricao text,
    genero text,
    quantidade text,
    preco text,
    primary key (idproduto)

);

create table fornecedor(

    idfornecedor int not null auto_increment,
    nome text,
    nomefantasia text,
    CNPJ text,
    endereco text,
    primary key (idfornecedor)

);