from django.urls import path

from . import views
from .views import *
urlpatterns = [
    path('', views.Home, name='home'),
    path('crear_clientes', views.Crear_clientes , name='crear_clientes'),
    path('crear_datos_clientes', views.Crear_datos_clientes , name='crear_datos_clientes'),##FUNCIONA
    path('crear_trabajadores', views.Crear_trabajadores , name='crear_trabajadores'),##FUNCIONA
    path('Crear_datos_trabajadores', views.Crear_datos_trabajadores , name='Crear_datos_trabajadores'),##FUNCIONA
    path('crear_materiales', views.Crear_materiales_capacitacion , name='Crear_materiales_capacitacion'),##Funciona
    path('crear_materiales_solicitados', views.Crear_datos_materiales_solicitados , name='Crear_datos_materiales_solicitados'),##FUNCIONA
    path('Crear_capacitaciones', views.Crear_capacitaciones , name='Crear_capacitaciones'),##SIN FUNCCIONAR
    path('reportar_tipo_accidentes', views.reportar_tipo_accidentes , name='reportar_tipo_accidentes'),
    path('reportar_accidentes', views.reportar_accidentes , name='reportar_accidentes'),
    path('reportar_tipo_accidentes', views.reportar_tipo_accidentes , name='reportar_tipo_accidentes'),
    path('Crear_registro_accidente', views.Crear_registro_accidente , name='Crear_registro_accidente'),
    path('registrar_visita_terreno', views.registrar_visita_terreno , name='registrar_visita_terreno'),
   









]
