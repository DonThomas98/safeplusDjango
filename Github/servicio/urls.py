from django.urls import path

from . import views
from .views import Home,Crear_clientes,Crear_datos_clientes
urlpatterns = [
    path('', views.Home, name='home'),
    path('crear_clientes', views.Crear_clientes , name='crear_clientes'),
    path('crear_datos_clientes', views.Crear_datos_clientes , name='crear_datos_clientes'),




]
