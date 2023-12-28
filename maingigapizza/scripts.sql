----------------------FUNÇÕES PARA LOGIN----------------------
----------------------FUNÇÕES PARA LOGIN----------------------
----------------------FUNÇÕES PARA LOGIN----------------------
CREATE OR REPLACE FUNCTION criar_sessao(id_usuario integer)
RETURNS INTEGER AS $$
declare
	id_sessao integer;
BEGIN
    insert into maingigapizza_sessao (is_ativo, ultima_interacao, usuario_id)
    values (true, now(), id_usuario);
   
    select max(id) into id_sessao from maingigapizza_sessao.id
    where maingigapizza_sessao.usuario_id = id_usuario;
  
	return id_sessao;
end;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION renovar_sessao(id_usuario integer)
RETURNS VOID AS $$
BEGIN
    UPDATE maingigapizza_sessao
    SET ultima_interacao = NOW()
    WHERE is_ativo = True AND usuario_id = id_usuario;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION atualizar_sessoes()
RETURNS VOID AS $$
BEGIN
    UPDATE maingigapizza_sessao
    SET is_ativo = False
    WHERE is_ativo = True AND ultima_interacao < NOW() - INTERVAL '10 minutes'
    and usuario_id != 2;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION fazer_login(login varchar, senha_login varchar)
RETURNS TABLE (
    id bigint,
    nome varchar,
    cpf varchar,
    telefone varchar,
    endereco varchar,
    email varchar,
    tipo varchar,
    sessao integer
) AS
$$
DECLARE 
    usuario record;
    sessao integer;
BEGIN
    -- Apenas mudar o where se quiser alterar o parametro de login
    SELECT * INTO usuario FROM maingigapizza_usuario
    WHERE (maingigapizza_usuario.cpf = login AND 
           maingigapizza_usuario.senha = senha_login) OR 
          (maingigapizza_usuario.email = login AND 
           maingigapizza_usuario.senha = senha_login);
    
    -- Retorna todas as colunas, menos a "SENHA"
    IF FOUND THEN
        IF usuario.is_ativo THEN
            SELECT criar_sessao INTO sessao FROM criar_sessao(usuario.id);

			PERFORM * FROM atualizar_sessoes

            
            IF EXISTS (SELECT 1 FROM pg_tables WHERE tablename = 'temp_retorno') THEN
                EXECUTE 'DROP TABLE temp_retorno';
            END IF;
            -- Insere os dados na tabela temporária
            CREATE TEMP TABLE temp_retorno ON COMMIT DROP AS
                SELECT
                    usuario.id,
                    usuario.nome,
                    usuario.cpf,
                    usuario.telefone,
                    usuario.endereco,
                    usuario.email,
                    usuario.tipo,
                    sessao;
            
            -- Retorna os dados da tabela temporária
            RETURN QUERY SELECT * FROM temp_retorno;
        ELSE
            -- Caso o usuário tenha sido encontrado, mas não está ativo, retorna 0
            RETURN QUERY SELECT 0::bigint, 'user inativo'::varchar,
           null::varchar, null::varchar, null::varchar, null::varchar, null::varchar,
           null::integer;
        END IF;
    ELSE
        -- Caso o usuário não tenha sido encontrado, retorna -1 e 'nao encontrado'
        RETURN QUERY SELECT -1::bigint, 'nao encontrado'::varchar,
           null::varchar, null::varchar, null::varchar, null::varchar, null::varchar,
           null::integer;
    END IF;

END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION fazer_logout(id_usuario integer)
RETURNS VOID AS $$
begin
	if id_usuario != 2 then
    	UPDATE maingigapizza_sessao
    	SET ultima_interacao = NOW(), is_ativo = False
    	WHERE usuario_id = id_usuario;
    end if;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION verificar_sessao_ativa(id_usuario integer)
RETURNS integer AS $$
begin
	-- Atualiza as seções
	perform * from atualizar_sessoes();
	-- Procura se há alguma sessao ativa
    perform * from maingigapizza_sessao
    where usuario_id = id_usuario
    and is_ativo = true;
   
    IF FOUND THEN
		perform * from renovar_sessao(id_usuario);
		return 1;
	else
		return 0;
	end if;
	
END;
$$ LANGUAGE plpgsql;




----------------------FUNÇÕES PARA CATEGORIA----------------------
----------------------FUNÇÕES PARA CATEGORIA----------------------
----------------------FUNÇÕES PARA CATEGORIA----------------------

-----Criar-----

CREATE OR REPLACE FUNCTION criar_categoria(nome_categoria varchar, id_usuario_requisitante integer)
RETURNS integer AS
$$
declare
	id_insercao integer;
	sessao_ativa integer;
begin 
	select verificar_sessao_ativa into sessao_ativa from verificar_sessao_ativa(id_usuario_requisitante);
	
	if sessao_ativa = 1 then
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
	else
		return -5;
	end if;

	--Legenda:
	--Retorna o id da nova categoria se a inserção for válida e única
	--Retorna '0' se a categoria a ser inserida já existe
	--Retorna -5 se nao há sessao ativa
END;
$$ LANGUAGE plpgsql;

-----Editar-----

CREATE OR REPLACE FUNCTION editar_categoria(id_categoria integer, nome_categoria varchar, id_usuario_requisitante integer)
RETURNS integer AS
$$
declare
	sessao_ativa integer;
begin 
	select verificar_sessao_ativa into sessao_ativa from verificar_sessao_ativa(id_usuario_requisitante);
	
	if sessao_ativa = 1 then
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
	else
		return -5;
	end if;

	--Legenda:
	--Retorna '1' se a edição for válida e única
	--Retorna '0' se o nome a ser inserido já existe
	--Retorna -5 se nao há sessao ativa
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

CREATE OR REPLACE FUNCTION criar_subcategoria(nome_subcategoria varchar, id_categoria integer, id_usuario_requisitante integer)
RETURNS integer AS
$$
declare
	id_insercao integer;
	sessao_ativa integer;
begin 
	select verificar_sessao_ativa into sessao_ativa from verificar_sessao_ativa(id_usuario_requisitante);
	
	if sessao_ativa = 1 then
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
	else
		return -5;
	end if;

	--Legenda:
	--Retorna o id da nova subcategoria se a inserção for válida e única
	--Retorna '0' se a subcategoria a ser inserida já existe na categoria
	--Retorna -5 se nao há sessao ativa
END;
$$ LANGUAGE plpgsql;

-----Editar-----

CREATE OR REPLACE FUNCTION editar_subcategoria(id_subcategoria integer, id_categoria integer, nome_subcategoria varchar, id_usuario_requisitante integer)
RETURNS integer AS
$$
declare
	sessao_ativa integer;
begin 
	select verificar_sessao_ativa into sessao_ativa from verificar_sessao_ativa(id_usuario_requisitante);
	
	if sessao_ativa = 1 then
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
	else
		return -5;
	end if;

	--Legenda:
	--Retorna '1' se a edição for válida e única
	--Retorna '0' se o nome a ser inserido já existe
	--Retorna -5 se nao há sessao ativa
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
    nome_item VARCHAR,
    preco float,
    quantidade float,
    unidade VARCHAR,
    id_usuario_requisitante integer
)
RETURNS INTEGER AS $$
DECLARE
    novo_id INTEGER;
	sessao_ativa integer;
begin 
	select verificar_sessao_ativa into sessao_ativa from verificar_sessao_ativa(id_usuario_requisitante);
	
	if sessao_ativa = 1 then
		--Verifica se há um item comprado com o mesmo nome
		
		PERFORM * FROM maingigapizza_itemcomprado
		WHERE INITCAP(maingigapizza_itemcomprado.nome) = INITCAP(nome_item);
		--se encontrar retorna 0
		IF FOUND THEN
			return 0;
		else
			select coalesce(max(maingigapizza_itemcomprado.id),0) + 1 from maingigapizza_itemcomprado into novo_id;
	
	    	INSERT INTO maingigapizza_itemcomprado (id,nome,is_ativo, preco, quantidade, unidade)
	    	VALUES (novo_id,nome_item, true, preco, quantidade, unidade);
	    
	    	return novo_id;
		end if;
		return 0;
	else
		return -5;
	end if;

		--Legenda:
		--Retorna o id do novo item comprado se a inserção for válida e única
		--Retorna '0' se o item comprado a ser inserido já existe
		--Retorna -5 se nao há sessao ativa
END;
$$ LANGUAGE plpgsql;


-----Editar-----

create or replace function editar_item_comprado(
    item_comprado_id INTEGER,
    novo_nome VARCHAR,
    novo_preco float,
    nova_quantidade float,
    nova_unidade VARCHAR,
    id_usuario_requisitante integer
)
RETURNS integer AS $$
DECLARE
	sessao_ativa integer;
begin 
	select verificar_sessao_ativa into sessao_ativa from verificar_sessao_ativa(id_usuario_requisitante);
	
	if sessao_ativa = 1 then
		--Verifica se há um Item comprado com o mesmo nome
		PERFORM * FROM maingigapizza_itemcomprado
		WHERE INITCAP(maingigapizza_itemcomprado.nome) = INITCAP(novo_nome)
		and maingigapizza_itemcomprado.id != item_comprado_id;
		--se encontrar é retornado 0
		IF FOUND THEN
			return 0;
		else
	    	UPDATE maingigapizza_itemcomprado
	    	SET nome = novo_nome, preco = novo_preco, quantidade = nova_quantidade, unidade = nova_unidade
	    	WHERE id = item_comprado_id;
			RETURN 1;
		--Legenda:
		--Retorna '1' se a edição for válida e única
		--Retorna '0' se o nome a ser inserido já existe
		--Retorna -5 se nao há sessao ativa
		END IF;
		RETURN 0;
	else
		return -5;
	end if;
END;
$$ LANGUAGE plpgsql;


-----Inativar-----

create or replace function inativar_item_comprado(id_item_comprado integer)
returns void as 
$$
begin 
	update maingigapizza_itemcomprado set is_ativo = false
	where maingigapizza_itemcomprado.id = id_item_comprado;
end
$$ language plpgsql;

-----Ativar-----

create or replace function ativar_item_comprado(id_item_comprado integer)
returns void as 
$$
begin 
	update maingigapizza_itemcomprado set is_ativo = true
	where maingigapizza_itemcomprado.id = id_item_comprado;
end
$$ language plpgsql;

-----Listar-----

create or replace function listar_itens_comprado()
returns table(id bigint,nome varchar, preco float, qtd float, unidade varchar, is_ativo boolean) as
$$
begin
	--retorna todos os items comprados pesquisados
	return query
	select maingigapizza_itemcomprado.id,
		   maingigapizza_itemcomprado.nome,
		   maingigapizza_itemcomprado.preco,
		   maingigapizza_itemcomprado.quantidade,
		   maingigapizza_itemcomprado.unidade,
		   maingigapizza_itemcomprado.is_ativo
	from maingigapizza_itemcomprado
	order by maingigapizza_itemcomprado.nome;
end;
$$ language plpgsql;

-----Listar Específico-----

create or replace function listar_item_comprado(id_item_comprado_pesquisado integer)
returns table(id_item_comprado bigint,nome_item_comprado varchar, preco float,
				qtd float, unidade varchar, is_ativo bool) as
$$
begin
	--retorna o item comprado pesquisado
	return query
	select maingigapizza_itemcomprado.id,
		   maingigapizza_itemcomprado.nome,
		   maingigapizza_itemcomprado.preco,
		   maingigapizza_itemcomprado.quantidade,
		   maingigapizza_itemcomprado.unidade,
		   maingigapizza_itemcomprado.is_ativo
	from maingigapizza_itemcomprado
	where maingigapizza_itemcomprado.id = id_item_comprado_pesquisado;
end;
$$ language plpgsql;

----------------------FUNÇÕES PARA ITEM VENDA----------------------
----------------------FUNÇÕES PARA ITEM VENDA----------------------
----------------------FUNÇÕES PARA ITEM VENDA----------------------


----Criar-----

CREATE OR REPLACE FUNCTION criar_item_venda(
	nome_item VARCHAR,
	descricao VARCHAR,
	preco FLOAT,
	subcategoria_id integer,
    id_usuario_requisitante integer
)

RETURNS INTEGER AS $$
DECLARE
	novo_id integer;
	sessao_ativa integer;
begin 
	select verificar_sessao_ativa into sessao_ativa from verificar_sessao_ativa(id_usuario_requisitante);
	
	if sessao_ativa = 1 then
		PERFORM * FROM maingigapizza_itemvenda
		WHERE INITCAP(maingigapizza_itemvenda.nome) = INITCAP(nome_item);
		--se encontar retorna 0
		
		IF FOUND THEN
			return 0;
			
		ELSE
			SELECT coalesce(max(maingigapizza_itemvenda.id),0) +1 FROM maingigapizza_itemvenda into novo_id;
			
		INSERT INTO maingigapizza_itemvenda (id, nome, descricao, preco, subcategoria_id, is_ativo)
		VALUES (novo_id, nome_item, descricao, preco, subcategoria_id,true);
		
		RETURN novo_id;
		END IF;
		RETURN 0;
	else
		return -5;
	end if;
		--Legenda:
		--Retorna o id do novo item venda se a inserção for válida e única
		--Retorna '0' se o novo item venda a ser inserido já existe
		--Retorna -5 se nao há sessao ativa

END
$$ language plpgsql;

-----editar-----

CREATE OR REPLACE FUNCTION editar_item_venda(
	id_item_venda INTEGER,
	novo_nome VARCHAR(50),
	nova_descricao VARCHAR(50),
	novo_preco FLOAT,
	id_usuario_requisitante integer
)

RETURNS INTEGER AS $$
DECLARE
	sessao_ativa integer;
begin 
	select verificar_sessao_ativa into sessao_ativa from verificar_sessao_ativa(id_usuario_requisitante);
	
	if sessao_ativa = 1 then
		PERFORM * FROM maingigapizza_itemvenda
		WHERE INITCAP(maingigapizza_itemvenda.nome) = INITCAP(novo_nome)
		and maingigapizza_itemvenda.id != id_item_venda;
		IF FOUND THEN 
			RETURN 0;
		ELSE
		UPDATE maingigapizza_itemvenda
		SET nome = novo_nome, descricao = nova_descricao, preco = novo_preco
		WHERE id = id_item_venda;
				RETURN 1;
		END IF;
		RETURN 0;
	else
		return -5;
	end if;
	--Retorna -5 se nao há sessao ativa
END
$$ language plpgsql;

-----ativar-----

CREATE OR REPLACE FUNCTION ativar_item_venda(id_item_venda INTEGER)
RETURNS VOID AS $$
BEGIN
	UPDATE maingigapizza_itemvenda set is_ativo = true
	WHERE maingigapizza_itemvenda.id = id_item_venda;
END	
$$ language plpgsql;


-----inativar-----

CREATE OR REPLACE FUNCTION inativar_item_venda(id_item_venda INTEGER)
RETURNS VOID AS $$
BEGIN
	UPDATE maingigapizza_itemvenda set is_ativo = false
	WHERE maingigapizza_itemvenda.id = id_item_venda;
END	
$$ language plpgsql;

----- Listar -----

create or replace function listar_itens_venda()
returns table(id bigint,nome varchar, descricao text, preco float, id_subcategoria bigint, is_ativo boolean) as
$$
begin
	--retorna todos os items venda pesquisados
	return query
	select maingigapizza_itemvenda.id,
		   maingigapizza_itemvenda.nome,
		   maingigapizza_itemvenda.descricao,
		   maingigapizza_itemvenda.preco,
		   maingigapizza_itemvenda.subcategoria_id,
		   maingigapizza_itemvenda.is_ativo 
	from maingigapizza_itemvenda
	order by maingigapizza_itemvenda.nome;
end;
$$ language plpgsql;

----- Listar Específico -----

create or replace function listar_item_venda(id_itemvenda integer)
returns table(id bigint, nome varchar, descricao text, preco float, id_subcategoria bigint, is_ativo boolean) as
$$
begin
	--retorna o item venda pesquisado
	return query
	select maingigapizza_itemvenda.id,
		   maingigapizza_itemvenda.nome,
		   maingigapizza_itemvenda.descricao,
		   maingigapizza_itemvenda.preco,
		   maingigapizza_itemvenda.subcategoria_id,
		   maingigapizza_itemvenda.is_ativo 
	from maingigapizza_itemvenda
	where maingigapizza_itemvenda.id = id_itemvenda;
end;
$$ language plpgsql;

----------------------FUNÇÕES PARA PEDIDO----------------------
----------------------FUNÇÕES PARA PEDIDO----------------------
----------------------FUNÇÕES PARA PEDIDO----------------------


----Criar-----

CREATE OR REPLACE FUNCTION criar_pedido(
	hora_solicitacao TIME,
	hora_entrega TIME,
	data_pedido DATE,
	descricao_pedido VARCHAR
)

RETURNS INTEGER AS $$
DECLARE
	novo_id integer;
	sessao_ativa integer;
begin 
	select verificar_sessao_ativa into sessao_ativa from verificar_sessao_ativa(id_usuario_requisitante);
	
	if sessao_ativa = 1 then
		SELECT coalesce(max(maingigapizza_pedido.id),0) +1 FROM maingigapizza_pedido into novo_id;
			
		INSERT INTO maingigapizza_pedido (id, horaSolicitacao, horaEntrega, dataPedido, descricao, isFinalizado)
		VALUES (novo_id, hora_solicitacao, hora_entrega, data_pedido, descricao_pedido,false);
		
		RETURN novo_id;
	else
		return -5;
	end if;
		--Legenda:
		--Retorna o id do novo pedido se a inserção for válida
		--Retorna -5 se nao há sessao ativa

END
$$ language plpgsql;

-----editar-----

CREATE OR REPLACE FUNCTION editar_pedido(
	id_pedido INTEGER,
	nova_hora_solicitacao TIME,
	nova_hora_entrega TIME,
	nova_data_pedido DATE,
	nova_descricao_pedido VARCHAR,
	id_usuario_requisitante integer
)

RETURNS INTEGER AS $$
DECLARE
	sessao_ativa integer;
begin 
	select verificar_sessao_ativa into sessao_ativa from verificar_sessao_ativa(id_usuario_requisitante);
	
	if sessao_ativa = 1 then
		UPDATE maingigapizza_pedido
		SET horaSolicitacao = nova_hora_solicitacao, 
		horaEntrega = nova_hora_entrega, 
		dataPedido = nova_data_pedido, 
		descricao = nova_descricao_pedido
		WHERE id = id_item_venda;
				RETURN 1;
	else
		return -5;
	end if;
	--Legenda:
	--Retorna 1 se o update for realizado com sucesso
	--Retorna -5 se nao há sessao ativa
END
$$ language plpgsql;

-----finalizar-----

CREATE OR REPLACE FUNCTION finalizar_pedido(id_pedido INTEGER)
RETURNS VOID AS $$
BEGIN
	UPDATE maingigapizza_pedido set isFinalizado = true
	WHERE maingigapizza_pedido.id = id_pedido;
END	
$$ language plpgsql;

----- Listar -----

create or replace function listar_pedidos()
returns table(id bigint,
		hora_solicitacao time, 
		hora_entrega time, 
		data_pedido date, 
		descricao text, 
		isFinalizado bool) as
$$
begin
	--retorna todos os pedidos salvos por data
	return query
	select maingigapizza_pedido.id,
		   maingigapizza_pedido.horaSolicitacao,
		   maingigapizza_pedido.horaEntrega,
		   maingigapizza_pedido.dataPedido,
		   maingigapizza_pedido.descricao,
		   maingigapizza_pedido.isFinalizado 
	from maingigapizza_pedido
	order by maingigapizza_pedido.dataPedido;
end;
$$ language plpgsql;

----- Listar Específico -----

create or replace function listar_pedido(id_pedido integer)
returns table(id bigint,
		hora_solicitacao time, 
		hora_entrega time, 
		data_pedido date, 
		descricao text, 
		isFinalizado bool) as
$$
begin
	--retorna o pedido pesquisado
	return query
	select maingigapizza_pedido.id,
		   maingigapizza_pedido.horaSolicitacao,
		   maingigapizza_pedido.horaEntrega,
		   maingigapizza_pedido.dataPedido,
		   maingigapizza_pedido.descricao,
		   maingigapizza_pedido.isFinalizado
	from maingigapizza_pedido
	where maingigapizza_pedido.id = id_pedido;
end;
$$ language plpgsql;
