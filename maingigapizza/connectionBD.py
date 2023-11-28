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
    
    