from django.db import connection

###################     CATEGORIA     ###################

def criar_categoria(nome_categoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from criar_categoria(%s)",[nome_categoria])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado

def editar_categoria(id_categoria, nome_categoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from editar_categoria(%s,%s)",[id_categoria,nome_categoria])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado
    
def inativar_categoria(id_categoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from inativar_categoria(%s)",[id_categoria])
        cursor.fetchall()
        cursor.close()
    
def ativar_categoria(id_categoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from ativar_categoria(%s)",[id_categoria])
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
        cursor.execute("SELECT * from listar_categoria(%s)",[id_categoria])
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    

###################     SUBCATEGORIA     ###################


def criar_subcategoria(nome_subcategoria, id_subcategoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from criar_subcategoria(%s,%s)",[nome_subcategoria, id_subcategoria])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado

def editar_subcategoria(id_subcategoria, id_categoria,nome_subcategoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from editar_subcategoria(%s,%s,%s)",[id_subcategoria,id_categoria,nome_subcategoria])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado
    
def inativar_subcategoria(id_subcategoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from inativar_subcategoria(%s)",[id_subcategoria])
        cursor.fetchall()
        cursor.close()
    
def ativar_subcategoria(id_subcategoria):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from ativar_subcategoria(%s)",[id_subcategoria])
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
        cursor.execute("SELECT * from listar_subcategoria(%s)",[id_subcategoria])
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    


###################     ITEM     ###################


def criar_item_comprado(nome_item_comprado, preco_item_comprado, quantidade_item_comprado, unidade_item_comprado):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from criar_item_comprado(%s)",[nome_item_comprado])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado

def editar_item_comprado(item_comprado_id, nome_item_comprado):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from editar_item_comprado(%s,%s)",[item_comprado_id, nome_item_comprado])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado

def inativar_item_comprado(id_item_comprado):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from inativar_item_comprado(%s)",[id_item_comprado])
        cursor.fetchall()
        cursor.close()

def ativar_item_comprado(id_item_comprado):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from ativar_item_comprado(%s)",[id_item_comprado])
        cursor.fetchall()
        cursor.close()

def listar_itens_comprado():
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_itens_comprado()")
        resultado = cursor.fetchall()
        cursor.close()
        return resultado

def listar_item_comprado(id_item_comprado_pesquisado):
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_item_comprado(%s)",[id_item_comprado_pesquisado])
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
