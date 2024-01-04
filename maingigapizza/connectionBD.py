from django.db import connection

###################     CATEGORIA     ###################


def criar_categoria(nome_categoria, id_usuario_requisitante):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute(
            "SELECT * from criar_categoria(%s,%s)",
            [nome_categoria, id_usuario_requisitante],
        )
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado


def editar_categoria(id_categoria, nome_categoria, id_usuario_requisitante):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute(
            "SELECT * from editar_categoria(%s,%s,%s)",
            [id_categoria, nome_categoria, id_usuario_requisitante],
        )
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado


def inativar_categoria(id_categoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from inativar_categoria(%s)", [id_categoria])
        cursor.fetchall()
        cursor.close()


def ativar_categoria(id_categoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from ativar_categoria(%s)", [id_categoria])
        cursor.fetchall()
        cursor.close()


def listar_categorias():
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_categorias()")
        resultado = cursor.fetchall()
        cursor.close()
        return resultado


def listar_categoria(id_categoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_categoria(%s)", [id_categoria])
        resultado = cursor.fetchall()
        cursor.close()
        return resultado


###################     SUBCATEGORIA     ###################


def criar_subcategoria(nome_subcategoria, id_subcategoria, id_usuario_requisitante):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute(
            "SELECT * from criar_subcategoria(%s,%s,%s)",
            [nome_subcategoria, id_subcategoria, id_usuario_requisitante],
        )
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado


def editar_subcategoria(
    id_subcategoria, id_categoria, nome_subcategoria, id_usuario_requisitante
):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute(
            "SELECT * from editar_subcategoria(%s,%s,%s,%s)",
            [id_subcategoria, id_categoria, nome_subcategoria, id_usuario_requisitante],
        )
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado


def inativar_subcategoria(id_subcategoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from inativar_subcategoria(%s)", [id_subcategoria])
        cursor.fetchall()
        cursor.close()


def ativar_subcategoria(id_subcategoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from ativar_subcategoria(%s)", [id_subcategoria])
        cursor.fetchall()
        cursor.close()


def listar_subcategorias():
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_subcategorias()")
        resultado = cursor.fetchall()
        cursor.close()
        return resultado


def listar_subcategoria(id_subcategoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_subcategoria(%s)", [id_subcategoria])
        resultado = cursor.fetchall()
        cursor.close()
        return resultado


###################     ITEM COMPRADO    ###################


def criar_item_comprado(
    nome_item_comprado,
    preco_item_comprado,
    quantidade_item_comprado,
    unidade_item_comprado,
    id_usuario_requisitante,
):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute(
            "SELECT * from criar_item_comprado(%s, %s, %s, %s,%s)",
            [
                nome_item_comprado,
                preco_item_comprado,
                quantidade_item_comprado,
                unidade_item_comprado,
                id_usuario_requisitante,
            ],
        )
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado


def editar_item_comprado(
    item_comprado_id, nome, preco, quantidade, unidade, id_usuario_requisitante
):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute(
            "SELECT * from editar_item_comprado(%s, %s, %s, %s, %s,%s)",
            [
                item_comprado_id,
                nome,
                preco,
                quantidade,
                unidade,
                id_usuario_requisitante,
            ],
        )
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado


def inativar_item_comprado(id_item_comprado):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from inativar_item_comprado(%s)", [id_item_comprado])
        cursor.fetchall()
        cursor.close()


def ativar_item_comprado(id_item_comprado):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from ativar_item_comprado(%s)", [id_item_comprado])
        cursor.fetchall()
        cursor.close()


def listar_itens_comprado():
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_itens_comprado()")
        resultado = cursor.fetchall()
        cursor.close()
        return resultado


def listar_item_comprado(id_item_comprado):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_item_comprado(%s)", [id_item_comprado])
        resultado = cursor.fetchall()
        cursor.close()
        return resultado


###################     ITEM VENDA    ###################


def criar_item_venda(
    nome_item_venda, descricao, preco, id_subcategoria, id_usuario_requisitante
):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute(
            "SELECT * from criar_item_venda(%s, %s, %s, %s, %s)",
            [
                nome_item_venda,
                descricao,
                preco,
                id_subcategoria,
                id_usuario_requisitante,
            ],
        )
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado


def editar_item_venda(id_item_venda, nome, descricao, preco, id_usuario_requisitante):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute(
            "SELECT * from editar_item_venda(%s, %s, %s, %s, %s)",
            [id_item_venda, nome, descricao, preco, id_usuario_requisitante],
        )
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado


def inativar_item_venda(id_item_venda):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from inativar_item_venda(%s)", [id_item_venda])
        cursor.fetchall()
        cursor.close()


def ativar_item_venda(id_item_venda):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from ativar_item_venda(%s)", [id_item_venda])
        cursor.fetchall()
        cursor.close()


def listar_itens_venda():
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_itens_venda()")
        resultado = cursor.fetchall()
        cursor.close()
        return resultado


def listar_item_venda(id_item_venda):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_item_venda(%s)", [id_item_venda])
        resultado = cursor.fetchall()
        cursor.close()
        return resultado


def listar_itens_pedido(id_pedido):
    ...


def criar_pedido(
    hora_entrega, descricao_pedido, id_usuario_requisitante, id_usuario_pedido
):
    ...


def editar_pedido(
    id_pedido, hora_entrega, nova_descricao_pedido, id_usuario_requisitante
):
    ...


def finalizar_pedido(id_pedido):
    ...


def listar_pedido():
    ...


def listar_pedido(pedido_id):
    ...


def listar_pedido_cliente(cliente_id):
    ...


def criar_pizza(id_item_venda, tamanho_pizza):
    ...


def listar_pizza():
    ...


def listar_pizzas_pedido(id_pedido_busca):
    ...


def criar_sabor_pizza(pizza_id, itemvenda_id):
    ...


def criar_pizzapedido(pedido_id, pizza_id):
    ...


def criar_itempedido(valor, quantidade, item_venda_id, pedido_id):
    ...
