from django.contrib import admin
from main.models import Produto


class Produtos(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'sku', 'custo', 'valor_venda',
                    'categoria', 'sub_categoria', 'marca', 'modelo', 'fabricante')
    list_display_links = ('id', 'descricao', 'sku')
    search_fields = ('descricao', )
    list_per_page = 20


admin.site.register(Produto, Produtos)
