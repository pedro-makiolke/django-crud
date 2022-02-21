from django.db import models


class Produto(models.Model):
    descricao = models.CharField(max_length=255, null=True)
    sku = models.CharField(max_length=30, null=True)
    custo = models.DecimalField
    valor_venda = models.DecimalField
    categoria = models.CharField(max_length=30, null=True)
    sub_categoria = models.CharField(max_length=30, null=True)
    marca = models.CharField(max_length=30, null=True)
    modelo = models.CharField(max_length=30, null=True)
    fabricante = models.CharField(max_length=30, null=True)
