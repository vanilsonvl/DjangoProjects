from django.conf.urls import url
from .views import register_brand, brand_list, edit_brand, remove_brand, register_product, product_list, edit_product, \
    remove_product, list_product_brand

urlpatterns = [
    url(r'^marca/cadastrar', register_brand, name='cadastro_marca'),
    url(r'^marca/listar', brand_list, name='lista_marcas'),
    url(r'^marca/editar/(?P<pk>[0-9]+)', edit_brand, name='editar_marca'),
    url(r'^marca/remover/(?P<pk>[0-9]+)', remove_brand, name='remover_marca'),
    url(r'^marca/lista_produtos_marca/(?P<pk>[0-9]+)', list_product_brand, name='lista_produtos_marca'),

    url(r'^produto/cadastrar', register_product, name='cadastro_produto'),
    url(r'^produto/listar', product_list, name='lista_produtos'),
    url(r'^produto/editar/(?P<pk>[0-9]+)', edit_product, name='editar_produto'),
    url(r'^produto/remover/(?P<pk>[0-9]+)', remove_product, name='remover_produto'),
]