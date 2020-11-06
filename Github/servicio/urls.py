from django.urls import path

from . import views
from .views import Home,Crear_clientes,Crear_datos_clientes,Crear_trabajadores,Crear_datos_trabajadores
urlpatterns = [
    path('', views.Home, name='home'),
    path('crear_clientes', views.Crear_clientes , name='crear_clientes'),
    path('crear_datos_clientes', views.Crear_datos_clientes , name='crear_datos_clientes'),
    path('crear_trabajadores', views.Crear_trabajadores , name='crear_trabajadores'),
    path('Crear_datos_trabajadores', views.Crear_datos_trabajadores , name='Crear_datos_trabajadores'),


]
