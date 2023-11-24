from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255, null=False)
    is_ativo = models.BooleanField(default=True, null=False)

    def __str__(self):
        return f'{self.nome}'
    
class SubCategoria(models.Model):
    nome = models.CharField(max_length=255, null=False)
    categoria = models.ForeignKey(Categoria, related_name='categoria_principal',
                                  on_delete=models.RESTRICT, null=False)
    is_ativo = models.BooleanField(default=True, null=False)

    def __str__(self):
        return f'{self.nome}'
    
class Insumo(models.Model):
    nome = models.CharField(max_length=255)
    preco = models.FloatField(null=False)
    quantidade = models.FloatField(null=False)

    def __str__(self):
        return f'{self.nome}'
    

    
class Item(models.Model):
    nome = models.CharField(max_length=255, null=False)
    descricao = models.TextField(blank=True, null=True)
    preco = models.FloatField(null=False)
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.RESTRICT,
        related_name='subcategoria', null=False)
    ingredientes = models.ManyToManyField(
        'Insumo',
        through='ItemInsumo',
    )

    def __str__(self):
        return f'Item {self.nome}'
    
class ItemInsumo(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.RESTRICT,
        related_name='item_insumos',
    )
    insumo = models.ForeignKey(
        Insumo,
        on_delete=models.RESTRICT,
        related_name='item_insumos',
    )
    quantidade = models.FloatField(null=False)

    def __str__(self):
        return f'ItemInsumo {self.item}, {self.insumo}, {self.quantidade}'


class Pizza(models.Model):
    nome = models.CharField(max_length=255, null=False)
    tamanho = models.IntegerField(null=False)
    sabor1 = models.ForeignKey(
        Item,
        on_delete=models.RESTRICT,
        related_name='pizzas_sabores_1',
    )
    sabor2 = models.ForeignKey(
        Item,
        on_delete=models.RESTRICT,
        related_name='pizzas_sabores_2',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Pizza {self.nome}'










