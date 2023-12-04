from django.urls import path

from .views import *

urlpatterns = [
    ###### CATEGORIAS ######
    path('cadastrar_categoria/', cadastrarCategoria, name='cadastrar_categoria'),
    path('editar_categoria/', editarCategoria, name='editar_categoria'),
    path('inativar_categoria/', inativarCategoria, name='inativar_categoria'),
    path('ativar_categoria/', ativarCategoria, name='ativar_categoria'),
    path('listar_categorias/', listarCategorias, name='listar_categorias'),
    path('listar_categoria/<int:pk>', listarCategoria, name='listar_categoria'),
    ###### SUBCATEGORIAS ######
    path('cadastrar_subcategoria/', cadastrarSubcategoria, name='cadastrar_subcategoria'),
    path('editar_subcategoria/', editarSubcategoria, name='editar_sucategoria'),
    path('inativar_subcategoria/', inativarSubcategoria, name='inativar_sucategoria'),
    path('ativar_subcategoria/', ativarSubcategoria, name='ativar_sucategoria'),
    path('listar_subcategorias/', listarSubcategorias, name='listar_sucategorias'),
    path('listar_subcategoria/<int:pk>', listarSubcategoria, name='listar_sucategoria'),
    ###### ITEM COMPRADO ######
    path('criar_item_comprado/', criar_item_comprado, name='criar_item_comprado'),
    path('editar_item_comprado/', editar_item_comprado, name='editar_item_comprado'),
    path('inativar_Subcategoria/', inativar_item_comprado, name='inativar_Subcategoria'),
    path('ativar_item_comprado/', ativar_item_comprado, name='ativar_item_comprado'),
    path('listar_itens_comprados/', listar_itens_comprados, name='listar_itens_comprado'),
    path('listar_item_compradoo/<int:pk>', listar_item_comprado, name='listar_item_comprado'),

]
