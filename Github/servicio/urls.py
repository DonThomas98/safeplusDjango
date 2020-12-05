from django.urls import path,include

from . import views
from .views import *


urlpatterns = [
    path('', views.Home, name='home'),
    path('', include('pwa.urls')),
    path('guardar-token/', guardar_token, name='guardar_token'),
    path('extender_cliente', views.extender_cliente, name='extender_cliente'),
    path('crear_cliente', views.crear_cliente, name='crear_cliente'),
    path('crear_trabajador', views.crear_trabajador, name='crear_trabajador'),
    path('extender_trabajador', views.extender_trabajador, name='extender_trabajador'),
    path('nueva_capacitacion', views.nueva_capacitacion, name='nueva_capacitacion'),
    path('nuevos_materiales', views.nuevos_materiales, name='nuevos_materiales'),
    path('nuevos_materiales_solicitados', views.nuevos_materiales_solicitados, name='nuevos_materiales_solicitados'),
    path('nueva_visita_rutinaria', views.nueva_visita_rutinaria, name='nueva_visita_rutinaria'),
    path('nuevo_accidente', views.nuevo_accidente, name='nuevo_accidente'),
    path('nueva_asesoria_accidente', views.nueva_asesoria_accidente, name='nueva_asesoria_accidente'),
    path('nueva_fiscalizacion', views.nueva_fiscalizacion, name='nueva_fiscalizacion'),
    path('nueva_asesoria_fiscalizaciones', views.nueva_asesoria_fiscalizaciones, name='nueva_asesoria_fiscalizaciones'),
    path('ver_accidentes_cliente_por_id', views.ver_accidentes_cliente_por_id, name='ver_accidentes_cliente_por_id'),##LISTA LOS ACCIDENTES DE UN CLIENTE AL PASARLE LA ID DE ESTE
    path('listado_clientes_con_modulos', views.listado_clientes_con_modulos, name='listado_clientes_con_modulos'),
    path('asesoria_id', views.ver_asesorias_por_id_accidente, name='ver_asesorias_por_id_accidente'),
    path('nuevo_informe_visita', views.nuevo_informe_visita, name='nuevo_informe_visita'),
    path('nuevo_registro_pagos', views.nuevo_registro_pagos, name='nuevo_registro_pagos'),









]
