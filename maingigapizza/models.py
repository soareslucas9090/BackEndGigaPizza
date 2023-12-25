from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255, null=False, unique=True)
    is_ativo = models.BooleanField(default=True, null=False)

    def __str__(self):
        return f"{self.nome}"


class SubCategoria(models.Model):
    nome = models.CharField(max_length=255, null=False, unique=False)
    categoria = models.ForeignKey(
        Categoria,
        related_name="categoria_principal",
        on_delete=models.RESTRICT,
        null=False,
    )
    is_ativo = models.BooleanField(default=True, null=False)

    def __str__(self):
        return f"{self.nome}"


class ItemComprado(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    preco = models.FloatField(null=False)
    quantidade = models.FloatField(null=False)
    unidade = models.CharField(max_length=255, null=False)
    is_ativo = models.BooleanField(default=True, null=False)

    def __str__(self):
        return f"{self.nome}"


class ItemVenda(models.Model):
    nome = models.CharField(max_length=255, null=False, unique=True)
    descricao = models.TextField(blank=True, null=True)
    preco = models.FloatField(null=False)
    subcategoria = models.ForeignKey(
        SubCategoria, on_delete=models.RESTRICT, related_name="subcategoria", null=False
    )
    ingredientes = models.ManyToManyField(
        ItemComprado,
        through="ItemCompradoVenda",
    )
    is_ativo = models.BooleanField(default=True, null=False)

    def __str__(self):
        return f"{self.nome}"


class ItemCompradoVenda(models.Model):
    item_venda = models.ForeignKey(
        ItemVenda,
        on_delete=models.RESTRICT,
        related_name="itemVenda",
    )
    item_comprado = models.ForeignKey(
        ItemComprado,
        on_delete=models.RESTRICT,
        related_name="itemComprado",
    )
    quantidade = models.FloatField(null=False)

    def __str__(self):
        return f"ItemCompradoVenda {self.item}, {self.insumo}, {self.quantidade}"


class Pizza(models.Model):
    nome = models.CharField(max_length=255, null=False)
    tamanho = models.IntegerField(null=False)
    preco = models.FloatField(null=False)

    def __str__(self):
        return f"Pizza {self.nome}"


class SaborPizza(models.Model):
    pizza = models.ForeignKey(
        Pizza, on_delete=models.RESTRICT, related_name="pizza", null=False
    )

    item_venda = models.ForeignKey(
        ItemVenda, on_delete=models.RESTRICT, related_name="item_venda", null=False
    )

    def __str__(self):
        return f"Pizza {self.nome}"


class Usuario(models.Model):
    nome = models.CharField(max_length=255, null=False)
    cpf = models.CharField(max_length=11, null=False, unique=True)
    tipo = models.CharField(max_length=64, null=False)
    telefone = models.CharField(max_length=11, null=False)
    endereco = models.CharField(max_length=255, null=False)
    email = models.EmailField(null=False, unique=True)
    senha = models.CharField(max_length=512, null=False)
    is_ativo = models.BooleanField(null=False, default=True)


class Sessao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT)
    is_ativo = models.BooleanField(default=True)
    ultima_interacao = models.DateTimeField()
