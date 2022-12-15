from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index),
    path('os_index', views.os_index, name='os_index'),
    path('os', views.add_os, name='add_os'),

    path('os/painel/<id>', views.detalhes_os, name='detalhes_os'),

    path('funcionario', views.funcionarios_listar, name='funcionarios'),
    path('funcionario/cadastrar', views.funcionario_cadastrar, name='cadastrar funcionario'),
    path('funcionario/editar/<id>', views.funcionario_editar, name='editar funcionario'),
    path('funcionario/deletar/<id>', views.funcionario_deletar, name='deletar funcionario'),

    path('os/painel/<id>/equipe', views.atribuir_equipe, name='atribuir equipe')
]