from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index),
    path('os_index', views.os_index, name='os_index'),
    path('os', views.add_os, name='add_os'),

    path('os/painel/<id>', views.detalhes_os, name='detalhes_os')
]