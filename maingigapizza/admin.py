from django.contrib import admin

from maingigapizza import models


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'is_ativo')

@admin.register(models.SubCategoria)
class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'is_ativo')
    
@admin.register(models.ItemComprado)
class ItemCompradoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'quantidade','unidade', 'is_ativo')
    
    
@admin.register(models.ItemVenda)
class ItemVendaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco','subcategoria', 'is_ativo')
    