from rest_framework import viewsets
from main.models import Produto
from main.serializer import ProdutoSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    
    def get_queryset(self):
        queryset = Produto.objects.all()
        descricao = self.request.query_params.get('descricao')
        sku = self.request.query_params.get('sku') 
        
        if descricao:
            queryset = queryset.filter(descricao__contains=descricao)
        elif sku:
            queryset = queryset.filter(sku__contains=sku)
        return queryset
