from django.test import TestCase

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
'''
def main(nome_categoria):
    #criar
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from criar_categoria(%s)",[nome_categoria])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        print(resultado)
        cursor.close()
'''
''' 
def main(nome_categoria):
    #editar
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from editar_categoria(%s,%s)",[2,nome_categoria])
        resultado = cursor.fetchall()
        # O resultado é um vetor dentro de um vetor, por isso o [0][0]
        resultado = resultado[0][0]
        print(resultado)
        cursor.close()
'''           
def main():
    #Essa linha é necessária para dizer ao django como se conectar ao banco
    with connection.cursor() as cursor:
        # Aqui chamo a função criada no banco
        cursor.execute("SELECT * from listar_categorias()")
        resultado = cursor.fetchall()
        cursor.close()
        print(resultado)

if __name__ == '__main__':
    settings.configure(DATABASES = database)
    main()