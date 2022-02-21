from rest_framework import serializers
from main.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'descricao', 'sku',
                  'categoria', 'sub_categoria', 'marca', 'modelo', 'fabricante']
