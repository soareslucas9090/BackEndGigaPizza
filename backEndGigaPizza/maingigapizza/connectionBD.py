from django.db import connection
from django.conf import settings
database={
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'oymneljm',
                'USER': 'oymneljm',
                'PASSWORD': 'vBFWwJBJIH6I7rRcjrx8bFvo0y2N8Cyj',
                'HOST': 'isabelle.db.elephantsql.com',
                'PORT': '5432',
            }
        }

def criar_categoria(nome_categoria):
    #Essa linha é necessária para dizer ao django como se conectar ao banco
    settings.configure(DATABASES = database)
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from criar_categoria(%s)",[nome_categoria])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado

def editar_categoria(id_categoria, nome_categoria):
    #Essa linha é necessária para dizer ao django como se conectar ao banco
    settings.configure(DATABASES = database)
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from editar_categoria(%s,%s)",[id_categoria,nome_categoria])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        return resultado
    
def inativar_categoria(id_categoria):
    #Essa linha é necessária para dizer ao django como se conectar ao banco
    settings.configure(DATABASES = database)
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from inativar_categoria(%s)",[id_categoria])
        resultado = cursor.fetchall()
        cursor.close()
    
def ativar_categoria(id_categoria):
    #Essa linha é necessária para dizer ao django como se conectar ao banco
    settings.configure(DATABASES = database)
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from ativar_categoria(%s)",[id_categoria])
        resultado = cursor.fetchall()
        cursor.close()
        
def listar_categoria():
    #Essa linha é necessária para dizer ao django como se conectar ao banco
    settings.configure(DATABASES = database)
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_categorias()")
        resultado = cursor.fetchall()
        cursor.close()
        return resultado
    
    