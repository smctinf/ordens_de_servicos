from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index),
    path('os_index', views.os_index, name='os_index'),
    path('os', views.add_os, name='add_os'),

    path('os/painel/<id>', views.detalhes_os, name='detalhes_os'),

    path('funcionario', views.funcionario_listar, name='funcionarios'),
    path('funcionario/cadastrar', views.funcionario_cadastrar, name='cadastrar funcionarios'),
    path('funcionario/editar/<id>', views.funcionario_editar, name='editar funcionarios')


]