from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index),
    path('os', views.add_os, name='add_os')
]