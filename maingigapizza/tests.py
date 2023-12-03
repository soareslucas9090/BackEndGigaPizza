from django.conf import settings
from django.db import connection
from django.test import TestCase

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

def main1(nome_categoria):
    #criar
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from criar_categoria(%s)",[nome_categoria])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        print(resultado)
        cursor.close()

def main2(nome_categoria):
    #editar
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from editar_categoria(%s,%s)",[2,nome_categoria])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        print(resultado)
        cursor.close()
          
def main3():
    #Essa linha é necessária para dizer ao django como se conectar ao banco
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_categorias()")
        resultado = cursor.fetchall()
        cursor.close()
        print(resultado)


def main4():
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from criar_item_comprado(%s, %s, %s, %s)",["teste2", "6.80",
                                                                            "11.0", "und"])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        print(resultado)
    
def main5():      
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_itens_comprado()")
        resultado = cursor.fetchall()
        cursor.close()
        print(resultado)
        
def main6():
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from editar_item_comprado(%s, %s, %s, %s, %s)",[1, "teste2", "6.0", "15", "und"])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        cursor.close()
        print(resultado)
        
def main7():        
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from inativar_item_comprado(%s)",[1])
        cursor.fetchall()
        cursor.close()
        
def main8():        
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from ativar_item_comprado(%s)",[1])
        cursor.fetchall()
        cursor.close()
        
def main():      
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_item_comprado(%s)",[1])
        resultado = cursor.fetchall()
        cursor.close()
        print(resultado)

if __name__ == '__main__':
    settings.configure(DATABASES = database)
    main()