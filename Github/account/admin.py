from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Multa)
admin.site.register(VisitaTerreno)
admin.site.register(InformeVisita)
admin.site.register(MaterialCapacitaciones)
admin.site.register(MaterialSolicitado)
admin.site.register(Capacitacion)
admin.site.register(TipoAccidente)
admin.site.register(Accidente)
admin.site.register(RegistroAccidentados)
admin.site.register(Asesoria)
admin.site.register(AntecedentesAsesoria)
admin.site.register(TipoContrato)
admin.site.register(Contrato)
admin.site.register(RegistroPagos)

