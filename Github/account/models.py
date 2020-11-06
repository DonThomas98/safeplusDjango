from django.db import models
from django.contrib.auth.models import User 



class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.IntegerField()
    sueldo=models.IntegerField()
    edad=models.IntegerField()

    def __str__(self):
        return self.user.username

class Multa(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    monto_multa = models.BigIntegerField()
    descripcion = models.CharField(max_length=50)
    fecha_multa = models.DateField()
  
    def __str__(self):
        return str(self.monto_multa) 
   
    class Meta:
        db_table = 'multa'


class VisitaTerreno(models.Model):
    rut_trabajador = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='cliente')
    rut_cliente = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='trabajador')
    fecha_visita = models.DateField()

    class Meta:
        db_table = 'visita_terreno'

class InformeVisita(models.Model):
    id_visita = models.OneToOneField(VisitaTerreno, on_delete=models.CASCADE)
    introduccion = models.CharField(max_length=250)
    resultados_evaluacion = models.CharField(max_length=500)
    autoevaluacion = models.CharField(max_length=1)
    doc_actualizados = models.CharField(max_length=1)
    reg_interno = models.CharField(max_length=1)
    doc_seremi_trabajo = models.CharField(max_length=1)
    copia_documentos = models.CharField(max_length=1)
    informa_riesgos = models.CharField(max_length=1)
    informa_medidas = models.CharField(max_length=1)
    programa_orden = models.CharField(max_length=1)
    extintores = models.CharField(max_length=1, blank=True, null=True)
    capacitacion_extintor = models.CharField(max_length=1, blank=True, null=True)
    epp_inventario = models.CharField(max_length=1, blank=True, null=True)
    epp_certificados = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'informe_visita'



class Capacitacion(models.Model):
	fecha_solicitud    = models.DateField()
	fecha_capacitacion = models.DateField()
	rut_trabajador     = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='capacitacioncliente')
	rut_cliente        = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='capacitaciontrabajador')

	class Meta:
		db_table = 'capacitacion'


class MaterialCapacitaciones(models.Model):
    material = models.CharField(max_length=50)

    def __str__(self):
        return self.material
    class Meta:
        db_table = 'material_capacitaciones'


class MaterialSolicitado(models.Model):
    id_material = models.ManyToManyField(MaterialCapacitaciones)
    cantidad = models.BigIntegerField()
    id_capacitacion =models.ForeignKey(Capacitacion, on_delete=models.CASCADE, default="",)
    def __str__(self):
        return str(self.cantidad)

    class Meta:
        db_table = 'material_solicitado'




class TipoAccidente(models.Model):
    descripcion = models.CharField(max_length=15)

    def __str__(self):
        return self.descripcion
    class Meta:
        db_table = 'tipo_accidente'


class Accidente(models.Model):
    fecha_accidente = models.DateField()
    id_tipo_accidente = models.ForeignKey(TipoAccidente, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_tipo_accidente)
    class Meta:
        db_table = 'accidente'




class RegistroAccidentados(models.Model):
    id_accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE)
    rut_trabajador     = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='accidentecliente')
    def __str__(self):
        return str(self.rut_trabajador)
    class Meta:
        db_table = 'registro_accidentados'


class Asesoria(models.Model):
    evento = models.CharField(max_length=25)
    propuesta = models.CharField(max_length=500)
    visita_asesoria = models.ForeignKey(VisitaTerreno, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.evento
    class Meta:
        db_table = 'asesoria'


class AntecedentesAsesoria(models.Model):
    id_asesoria = models.ForeignKey(Asesoria, on_delete=models.CASCADE)
    descripcion_documento = models.CharField(max_length=50)
    documento = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'antecedentes_asesoria'

class TipoContrato(models.Model):
    descripcion = models.CharField(max_length=30)
    costo = models.BigIntegerField()

    class Meta:
        db_table = 'tipo_contrato'


class Contrato(models.Model):
    rut_cliente = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_contrato =models.OneToOneField(TipoContrato, on_delete=models.CASCADE)
    fecha_contratacion = models.DateField()
    
    def __str__(self):
        return str(self.fecha_contratacion)
    class Meta:
        db_table = 'contrato'

class RegistroPagos(models.Model):
    monto_pago = models.BigIntegerField()
    fecha_pago = models.DateField()
    id_contrato =  models.ForeignKey(Contrato, on_delete=models.CASCADE)

    class Meta:
        db_table = 'registro_pagos'

