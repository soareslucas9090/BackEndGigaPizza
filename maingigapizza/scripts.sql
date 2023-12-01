
----------------------FUNÇÕES PARA CATEGORIA----------------------
----------------------FUNÇÕES PARA CATEGORIA----------------------
----------------------FUNÇÕES PARA CATEGORIA----------------------

-----Criar-----

CREATE OR REPLACE FUNCTION criar_categoria(nome_categoria varchar)
RETURNS integer AS
$$
declare
	id_insercao integer;
begin 
	--Verifica se há uma categoria com o mesmo nome
	PERFORM * FROM maingigapizza_categoria
	WHERE INITCAP(maingigapizza_categoria.nome) = INITCAP(nome_categoria);
	--se encontrar retorna 0
	IF FOUND THEN
		return 0;
	else
		select coalesce(max(maingigapizza_categoria.id),0) + 1 from maingigapizza_categoria into id_insercao;
	
		insert into maingigapizza_categoria values
		(id_insercao, INITCAP(nome_categoria), true);
												
		RETURN id_insercao;
	END IF;
	RETURN 0;

	--Legenda:
	--Retorna o id da nova categoria se a inserção for válida e única
	--Retorna '0' se a categoria a ser inserida já existe
END;
$$ LANGUAGE plpgsql;

-----Editar-----

CREATE OR REPLACE FUNCTION editar_categoria(id_categoria integer, nome_categoria varchar)
RETURNS integer AS
$$
declare
begin 
	--Verifica se há uma categoria com o mesmo nome
	PERFORM * FROM maingigapizza_categoria
	WHERE INITCAP(maingigapizza_categoria.nome) = INITCAP(nome_categoria);
	--se encontrar é retornado 0
	IF FOUND THEN
		return 0;
	else
		update maingigapizza_categoria set nome = INITCAP(nome_categoria)
		where maingigapizza_categoria.id = id_categoria;
												
		RETURN 1;
	END IF;
	RETURN 0;

	--Legenda:
	--Retorna '1' se a edição for válida e única
	--Retorna '0' se o nome a ser inserido já existe
END;
$$ LANGUAGE plpgsql;

-----Inativar-----

CREATE OR REPLACE FUNCTION inativar_categoria(id_categoria integer)
RETURNS void AS
$$
declare
begin 
	update maingigapizza_categoria set is_ativo = false
	where maingigapizza_categoria.id = id_categoria;

END;
$$ LANGUAGE plpgsql;

-----Ativar-----

CREATE OR REPLACE FUNCTION ativar_categoria(id_categoria integer)
RETURNS void AS
$$
declare
begin 
	update maingigapizza_categoria set is_ativo = true
	where maingigapizza_categoria.id = id_categoria;

END;
$$ LANGUAGE plpgsql;

-----Listar-----

CREATE OR REPLACE FUNCTION listar_categorias()
returns table (id_categoria bigint, nome_categoria varchar, is_ativo boolean) as
$$
declare
begin
	--retorna todas as categorias em ordem alfabetica
    return query
    select maingigapizza_categoria.id,
   		   maingigapizza_categoria.nome,
   		   maingigapizza_categoria.is_ativo
   		  from maingigapizza_categoria
   		 order by maingigapizza_categoria.nome;
	   	
END;
$$ LANGUAGE plpgsql;

-----Listar Específico-----

CREATE OR REPLACE FUNCTION listar_categoria(id_categoria_pesquisada integer)
returns table (id_categoria bigint, nome_categoria varchar, is_ativo boolean) as
$$
declare
begin
	--retorna a categoria pesquisada
    return query
    select maingigapizza_categoria.id,
   		   maingigapizza_categoria.nome,
   		   maingigapizza_categoria.is_ativo
   		  from maingigapizza_categoria
		  where maingigapizza_categoria.id = id_categoria_pesquisada;
	   	
END;
$$ LANGUAGE plpgsql;
----------------------FUNÇÕES PARA SUBCATEGORIA----------------------
----------------------FUNÇÕES PARA SUBCATEGORIA----------------------
----------------------FUNÇÕES PARA SUBCATEGORIA----------------------

-----Criar-----

CREATE OR REPLACE FUNCTION criar_subcategoria(nome_subcategoria varchar, id_categoria integer)
RETURNS integer AS
$$
declare
	id_insercao integer;
begin 
	--Verifica se há uma subcategoria com o mesmo nome e mesma categoria
	PERFORM * FROM maingigapizza_subcategoria
	WHERE INITCAP(maingigapizza_subcategoria.nome) = INITCAP(nome_subcategoria) and 
	maingigapizza_subcategoria.categoria_id = id_categoria;
	--se encontrar retorna 0
	IF FOUND THEN
		return 0;
	else
		select coalesce(max(maingigapizza_subcategoria.id),0) + 1 from maingigapizza_subcategoria into id_insercao;
	
		insert into maingigapizza_subcategoria values
		(id_insercao, INITCAP(nome_subcategoria), true, id_categoria);
												
		RETURN id_insercao;
	END IF;
	RETURN 0;

	--Legenda:
	--Retorna o id da nova subcategoria se a inserção for válida e única
	--Retorna '0' se a subcategoria a ser inserida já existe na categoria
END;
$$ LANGUAGE plpgsql;

-----Editar-----

CREATE OR REPLACE FUNCTION editar_subcategoria(id_subcategoria integer, id_categoria integer, nome_subcategoria varchar)
RETURNS integer AS
$$
declare
begin 
	--Verifica se há uma subcategoria com o mesmo nome e mesma categoria
	PERFORM * FROM maingigapizza_subcategoria
	WHERE INITCAP(maingigapizza_subcategoria.nome) = INITCAP(nome_subcategoria) and 
				maingigapizza_subcategoria.categoria_id = id_categoria;
	--se encontrar é retornado 0
	IF FOUND THEN
		return 0;
	else
		update maingigapizza_subcategoria set nome = INITCAP(nome_subcategoria)
		where maingigapizza_subcategoria.id = id_subcategoria;
												
		RETURN 1;
	END IF;
	RETURN 0;

	--Legenda:
	--Retorna '1' se a edição for válida e única
	--Retorna '0' se o nome a ser inserido já existe
END;
$$ LANGUAGE plpgsql;

-----Inativar-----

CREATE OR REPLACE FUNCTION inativar_subcategoria(id_subcategoria integer)
RETURNS void AS
$$
declare
begin 
	update maingigapizza_subcategoria set is_ativo = false
	where maingigapizza_subcategoria.id = id_subcategoria;

END;
$$ LANGUAGE plpgsql;

-----Ativar-----

CREATE OR REPLACE FUNCTION ativar_subcategoria(id_subcategoria integer)
RETURNS void AS
$$
declare
begin 
	update maingigapizza_subcategoria set is_ativo = true
	where maingigapizza_subcategoria.id = id_subcategoria;

END;
$$ LANGUAGE plpgsql;

-----Listar-----

CREATE OR REPLACE FUNCTION listar_subcategorias()
returns table (id_subcategoria bigint, nome_subcategoria varchar, id_categoria bigint, is_ativo boolean) as
$$
declare
begin
	--retorna todas as subcategorias em ordem alfabetica
    return query
    select maingigapizza_subcategoria.id,
   		   maingigapizza_subcategoria.nome,
   		   maingigapizza_subcategoria.categoria_id,
   		   maingigapizza_subcategoria.is_ativo
   		  from maingigapizza_subcategoria
   		 order by maingigapizza_subcategoria.nome;
	   	
END;
$$ LANGUAGE plpgsql;

-----Listar Específico-----

CREATE OR REPLACE FUNCTION listar_subcategoria(id_subcategoria_pesquisada integer)
returns table (id_subcategoria bigint, nome_subcategoria varchar, id_categoria bigint, is_ativo boolean) as
$$
declare
begin
	--retorna a subcategoria pesquisada
    return query
    select maingigapizza_subcategoria.id,
   		   maingigapizza_subcategoria.nome,
   		   maingigapizza_subcategoria.categoria_id,
   		   maingigapizza_subcategoria.is_ativo
   		  from maingigapizza_subcategoria
		  where maingigapizza_subcategoria.id = id_subcategoria_pesquisada;
	   	
END;
$$ LANGUAGE plpgsql;


----------------------FUNÇÕES PARA ITEM COMPRADO----------------------
----------------------FUNÇÕES PARA ITEM COMPRADO----------------------
----------------------FUNÇÕES PARA ITEM COMPRADO----------------------

-----Criar-----

create or replace function criar_item_comprado(
    nome VARCHAR,
    preco float,
    quantidade float,
    unidade VARCHAR
)
RETURNS INTEGER AS $$
DECLARE
    novo_id INTEGER;
BEGIN
	PERFORM * FROM maingigapizza_item_comprado
	WHERE INITCAP(maingigapizza_item_comprado.nome) = INITCAP(nome);
	--se encontrar retorna 0
	IF FOUND THEN
		return 0;
	else
		select coalesce(max(maingigapizza_item_comprado.id),0) + 1 from maingigapizza_item_comprado into novo_id;

    	INSERT INTO maingigapizza_item_comprado (id,nome,is_ativo, preco, quantidade, unidade)
    	VALUES (novo_id,nome, true, preco, quantidade, unidade);
    
    	return novo_id;
		end if;
		return 0;

		--Legenda:
		--Retorna o id da nova categoria se a inserção for válida e única
		--Retorna '0' se a categoria a ser inserida já existe
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION criar_categoria(nome_categoria varchar)
RETURNS integer AS
$$
declare
	id_insercao integer;
begin 
	--Verifica se há uma categoria com o mesmo nome
	PERFORM * FROM maingigapizza_categoria
	WHERE INITCAP(maingigapizza_categoria.nome) = INITCAP(nome_categoria);
	--se encontrar retorna 0
	IF FOUND THEN
		return 0;
	else
		select coalesce(max(maingigapizza_categoria.id),0) + 1 from maingigapizza_categoria into id_insercao;
	
		insert into maingigapizza_categoria values
		(id_insercao, INITCAP(nome_categoria), true);
												
		RETURN id_insercao;
	END IF;
	RETURN 0;

	--Legenda:
	--Retorna o id da nova categoria se a inserção for válida e única
	--Retorna '0' se a categoria a ser inserida já existe
END;
$$ LANGUAGE plpgsql;

-----Editar-----

create or replace function editar_item_comprado(
    item_comprado_id INTEGER,
    novo_nome VARCHAR,
    novo_preco float,
    nova_quantidade float,
    nova_unidade VARCHAR
)
RETURNS integer AS $$
BEGIN

	--Verifica se há uma subcategoria com o mesmo nome e mesma categoria
	PERFORM * FROM maingigapizza_item_comprado
	WHERE INITCAP(maingigapizza_item_comprado.nome) = INITCAP(novo_nome);
	--se encontrar é retornado 0
	IF FOUND THEN
		return 0;
	else
    	UPDATE maingigapizza_item_comprado
    	SET nome = novo_nome, preco = novo_preco, quantidade = nova_quantidade, unidade = nova_unidade
    	WHERE id = item_comprado_id;
		RETURN 1;
	--Legenda:
	--Retorna '1' se a edição for válida e única
	--Retorna '0' se o nome a ser inserido já existe
	END IF;
	RETURN 0;
END;
$$ LANGUAGE plpgsql;

-----Inativar-----

create or replace function inativar_item_comprado(id_item_comprado integer)
returns void as 
$$
begin 
	update maingigapizza_item_comprado set is_ativo = false
	where maingigapizza_item_comprado.id = id_item_comprado;
end
$$ language plpgsql;

-----Ativar-----

create or replace function ativar_item_comprado(id_item_comprado integer)
returns void as 
$$
begin 
	update maingigapizza_item_comprado set is_ativo = true
	where maingigapizza_item_comprado.id = id_item_comprado;
end
$$ language plpgsql;

-----Listar-----

create or replace function listar_itens_comprado()
returns table(id integer,nome varchar, preco float, qtd float, unidade varchar, is_ativo boolean) as
$$
begin
	--retorna todas as categorias pesquisadas
	return query
	select maingigapizza_item_comprado.id,
		   maingigapizza_item_comprado.nome,
		   maingigapizza_item_comprado.preco,
		   maingigapizza_item_comprado.quantidade,
		   maingigapizza_item_comprado.unidade,
		   maingigapizza_item_comprado.is_ativo
	from maingigapizza_item_comprado
	order by maingigapizza_item_comprado.nome;
end;
$$ language plpgsql;

-----Listar Específico-----

create or replace function listar_item_comprado(id_item_comprado_pesquisado integer)
returns table(id_item_comprado integer,nome_item_comprado varchar,is_ativo bool) as
$$
begin
	--retorna a categoria pesquisada
	return query
	select maingigapizza_item_comprado.id,
		   maingigapizza_item_comprado.nome,
		   maingigapizza_item_comprado.preco,
		   maingigapizza_item_comprado.quantidade,
		   maingigapizza_item_comprado.unidade,
		   maingigapizza_item_comprado.is_ativo
	from maingigapizza_item_comprado
	where maingigapizza_item_comprado.id = id_item_comprado_pesquisado;
end;
$$ language plpgsql;
