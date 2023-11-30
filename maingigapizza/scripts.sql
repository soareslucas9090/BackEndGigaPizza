
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
    nome VARCHAR(50),
    preco REAL,
    quantidade REAL,
    unidade VARCHAR(30)
)
returns integer as $$
declare
    novo_id INTEGER;
begin
	
    insert into item_comprado (nome, preco, quantidade, unidade)
    values (nome, preco, quantidade, unidade) returning id into novo_id;
    
    return novo_id;
end;
$$ language plpgsql;

-----Editar-----

create or replace function editar_item_comprado(
    item_comprado_id integer,
    novo_nome varchar(50),
    novo_preco real,
    nova_quantidade real,
    nova_unidade varchar(30)
)
returns void as $$
begin
	
    update item_comprado
    set nome = novo_nome, preco = novo_preco, quantidade = nova_quantidade, unidade = nova_unidade
    where id = item_comprado_id;

   end;
  
$$ language plpgsql;



