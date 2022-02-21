from django.contrib import admin
from django.urls import path, include
from main.views import ProdutosViewSet
from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register('produtos', ProdutosViewSet, basename='Produtos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/', include(router.urls))
]
