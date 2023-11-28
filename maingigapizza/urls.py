from django.urls import path
from .views import *

urlpatterns = [
    ###### CATEGORIAS ######
    path('cadastrar_categoria/', cadastrarCategoria, name='cadastrar_categoria'),
    path('editar_categoria/', editarCategoria, name='editar_categoria'),
    path('inativar_categoria/', inativarCategoria, name='inativar_categoria'),
    path('inativar_categoria/', ativarCategoria, name='ativar_categoria'),
    path('listar_categorias/', listarCategorias, name='listar_categorias'),
    path('listar_categoria/<int:pk>', listarCategoria, name='listar_categoria'),
    ###### SUBCATEGORIAS ######
    path('cadastrar_subcategoria/', cadastrarSubcategoria, name='cadastrar_subcategoria'),
    path('editar_subcategoria/', editarSubcategoria, name='editar_sucategoria'),
    path('inativar_subcategoria/', inativarSubcategoria, name='inativar_sucategoria'),
    path('ativar_subcategoria/', ativarSubcategoria, name='ativar_sucategoria'),
    path('listar_subcategorias/', listarSubcategorias, name='listar_sucategorias'),
    path('listar_subcategoria/<int:pk>', listarSubcategoria, name='listar_sucategoria'),
]