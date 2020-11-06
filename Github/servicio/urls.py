from django.urls import path

from . import views
from .views import *
urlpatterns = [
    path('', views.Home, name='home'),
    path('crear_clientes', views.Crear_clientes , name='crear_clientes'),
    path('crear_datos_clientes', views.Crear_datos_clientes , name='crear_datos_clientes'),
    path('crear_trabajadores', views.Crear_trabajadores , name='crear_trabajadores'),
    path('Crear_datos_trabajadores', views.Crear_datos_trabajadores , name='Crear_datos_trabajadores'),
    path('crear_materiales', views.Crear_materiales_capacitacion , name='Crear_materiales_capacitacion'),


]
