from django.db import models
from django.contrib.auth.models import User 



class UserProfile(models.Model):
    rut = models.IntegerField()
    sueldo=models.IntegerField()
    edad=models.IntegerField()
    user=models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

class Multa(models.Model):
    monto_multa = models.BigIntegerField()
    descripcion = models.CharField(max_length=50)
    fecha_multa = models.DateField()
    multa_cliente = models.ForeignKey(User, on_delete=models.CASCADE)

  
    def __str__(self):
        return str(self.monto_multa) 
   
    class Meta:
        db_table = 'multa'


class VisitaTerreno(models.Model):
    fecha_visita = models.DateField()
    motivo_visita=models.CharField(max_length=50)
    rut_trabajador = models.ForeignKey(User, on_delete=models.CASCADE,related_name='cliente')
    rut_cliente = models.ForeignKey(User, on_delete=models.CASCADE,related_name='trabajador')

    class Meta:
        db_table = 'visita_terreno'

class InformeVisita(models.Model):
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
    id_visita = models.OneToOneField(VisitaTerreno, on_delete=models.CASCADE)


    class Meta:
        db_table = 'informe_visita'


class MaterialCapacitaciones(models.Model):
    material = models.CharField(max_length=50)

    def __str__(self):
        return self.material
    class Meta:
        db_table = 'material_capacitaciones'



class Capacitacion(models.Model):
    fecha_solicitud              = models.DateField()
    fecha_capacitacion           = models.DateField()
    hora_capacitacion            = models.CharField(max_length=50)
    rut_trabajador               = models.ForeignKey(User, on_delete=models.CASCADE,related_name='capacitacioncliente')
    rut_cliente                  = models.ForeignKey(User, on_delete=models.CASCADE,related_name='capacitaciontrabajador')

    class Meta:
        db_table = 'capacitacion'
    def __str__(self):
        return str(self.fecha_capacitacion)



class MaterialSolicitado(models.Model):
    cantidad = models.BigIntegerField()
    id_material = models.ForeignKey(MaterialCapacitaciones, on_delete=models.CASCADE)
    material_capacitacion        = models.ForeignKey(Capacitacion, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cantidad)

    class Meta:
        db_table = 'material_solicitado'



class Accidente(models.Model):
    naturaleza = models.CharField(max_length=50)
    partes_accidentadas = models.CharField(max_length=50)
    fuente_accidente = models.CharField(max_length=50)
    fecha_accidente   = models.DateField()
    rut_cliente       = models.ForeignKey(User, on_delete=models.CASCADE,related_name='accidentecliente')
    def __str__(self):
        return "{0} {1} {2}".format(self.naturaleza,', cliente', self.rut_cliente)
    class Meta:
        db_table = 'accidente'

class fiscalizacion(models.Model):
    doc_revisados = models.CharField(max_length=50)
    descripcion_documento = models.CharField(max_length=50)
    documento = models.TextField(blank=True, null=True)  
    rut_cliente      = models.ForeignKey(User, on_delete=models.CASCADE,related_name='fiscalizacioncliente')


    class Meta:
        db_table = 'fiscalizacion'




class Asesoria(models.Model):
    evento = models.CharField(max_length=25)
    propuesta = models.CharField(max_length=500)
    asesoria_especial=models.CharField(max_length=2)
    id_accidente = models.ForeignKey(Accidente, on_delete=models.CASCADE,blank=True, null=True)
    id_fiscalizacion = models.ForeignKey(fiscalizacion, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.evento
    class Meta:
        db_table = 'asesoria'




class Contrato(models.Model):
    descripcion = models.CharField(max_length=30)
    costo = models.BigIntegerField()
    fecha_contratacion = models.DateField()
    rut_cliente = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return  "{0} {1} {2}".format(self.rut_cliente,', con contrato ', self.descripcion)  
    class Meta:
        db_table = 'contrato'

class RegistroPagos(models.Model):
    monto_pago = models.BigIntegerField()
    fecha_pago = models.DateField()
    id_contrato =  models.ForeignKey(Contrato, on_delete=models.CASCADE)

    class Meta:
        db_table = 'registro_pagos'


class Costo_adicional(models.Model):
    monto_adicional = models.BigIntegerField()
    fecha_costoadicional =  models.DateField()
    id_contrato =  models.ForeignKey(Contrato, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Costo_adicional'


 

