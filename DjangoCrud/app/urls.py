from django.conf.urls import url
from .views import register_car, car_list, edit_car, remove_car

urlpatterns = [
    url(r'cadastrar_carro', register_car, name='cadastro_carro'),
    url(r'lista_carros', car_list, name='lista_carros'),
    url(r'^editar_carro/(?P<pk>[0-9]+)', edit_car, name='editar_carro'),
    url(r'^remover_carro/(?P<pk>[0-9]+)', remove_car, name='remover_carro'),
]