from django.db import models

# Create your models here.

#1
class Cargo(models.Model):
    id_cargo = models.BigIntegerField(primary_key=True)
    cargo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cargo'



#2
class Cliente(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv_rut = models.CharField(max_length=1)
    p_nombre = models.CharField(max_length=50)
    s_nombre = models.CharField(max_length=50)
    p_apellido = models.CharField(max_length=50)
    s_apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=100)
    telefono = models.BigIntegerField(blank=True, null=True)
    celular = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'



#3

class Trabajador(models.Model):
    rut = models.IntegerField(primary_key=True)
    dv_rut = models.CharField(max_length=1)
    p_nombre = models.CharField(max_length=50)
    s_nombre = models.CharField(max_length=50)
    p_apellido = models.CharField(max_length=50)
    s_apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=100)
    telefono = models.BigIntegerField(blank=True, null=True)
    celular = models.BigIntegerField()
    habilitado = models.CharField(max_length=1)
    sueldo = models.BigIntegerField()
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo')
    contrasena = models.CharField(max_length=100)
    superuser = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'trabajador'

#4
class MaterialCapacitaciones(models.Model):
    id_material = models.BigIntegerField(primary_key=True)
    material = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'material_capacitaciones'


#5

class Capacitacion(models.Model):
    id_capacitacion = models.BigIntegerField(primary_key=True)
    fecha_solicitud = models.DateField()
    fecha_capacitacion = models.DateField()
    rut_trabajador = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='rut_trabajador')
    rut_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='rut_cliente')

    class Meta:
        managed = False
        db_table = 'capacitacion'


#6
class MaterialSolicitado(models.Model):
    id_registro = models.BigIntegerField(primary_key=True)
    id_material = models.ForeignKey(MaterialCapacitaciones, models.DO_NOTHING, db_column='id_material')
    cantidad = models.BigIntegerField()
    id_capacitacion = models.ForeignKey(Capacitacion, models.DO_NOTHING, db_column='id_capacitacion')

    class Meta:
        managed = False
        db_table = 'material_solicitado'

#7
class TipoContrato(models.Model):
    tipo_contrato = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)
    costo = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_contrato'

#8

class Contrato(models.Model):
    id_contrato = models.BigIntegerField(primary_key=True)
    rut_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rut_cliente')
    tipo_contrato = models.ForeignKey('TipoContrato', models.DO_NOTHING, db_column='tipo_contrato')
    fecha_contratacion = models.DateField()

    class Meta:
        managed = False
        db_table = 'contrato'

#9
class RegistroPagos(models.Model):
    id_pago = models.BigIntegerField(primary_key=True)
    monto_pago = models.BigIntegerField()
    fecha_pago = models.DateField()
    id_contrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='id_contrato')

    class Meta:
        managed = False
        db_table = 'registro_pagos'
#10
class TipoAccidente(models.Model):
    id_tipo_accidente = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'tipo_accidente'

#11

class Accidente(models.Model):
    id_accidente = models.BigIntegerField(primary_key=True)
    fecha_accidente = models.DateField()
    id_tipo_accidente = models.ForeignKey('TipoAccidente', models.DO_NOTHING, db_column='id_tipo_accidente')

    class Meta:
        managed = False
        db_table = 'accidente'

#12
class RegistroAccidentados(models.Model):
    id_accidentados = models.BigIntegerField(primary_key=True)
    id_accidente = models.ForeignKey(Accidente, models.DO_NOTHING, db_column='id_accidente')
    rut_trabajador = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rut_trabajador')

    class Meta:
        managed = False
        db_table = 'registro_accidentados'

#13
class VisitaTerreno(models.Model):
    id_visita = models.BigIntegerField(primary_key=True)
    rut_trabajador = models.ForeignKey(Trabajador, models.DO_NOTHING, db_column='rut_trabajador')
    rut_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rut_cliente')
    fecha_visita = models.DateField()

    class Meta:
        managed = False
        db_table = 'visita_terreno'

#14
class InformeVisita(models.Model):
    id_informe = models.BigIntegerField(primary_key=True)
    id_visita = models.ForeignKey('VisitaTerreno', models.DO_NOTHING, db_column='id_visita')
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
        managed = False
        db_table = 'informe_visita'

#15

class Multa(models.Model):
    id_multa = models.BigIntegerField(primary_key=True)
    monto_multa = models.BigIntegerField()
    descripcion = models.CharField(max_length=50)
    fecha_multa = models.DateField()
    rut_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='rut_cliente')

    class Meta:
        managed = False
        db_table = 'multa'




#16
class Asesoria(models.Model):
    id_asesoria = models.BigIntegerField(primary_key=True)
    evento = models.CharField(max_length=25)
    propuesta = models.CharField(max_length=500)
    id_visita = models.ForeignKey('VisitaTerreno', models.DO_NOTHING, db_column='id_visita')

    class Meta:
        managed = False
        db_table = 'asesoria'



#17

class AntecedentesAsesoria(models.Model):
    id_antecedente = models.BigIntegerField(primary_key=True)
    id_asesoria = models.ForeignKey('Asesoria', models.DO_NOTHING, db_column='id_asesoria')
    descripcion_documento = models.CharField(max_length=50)
    documento = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'antecedentes_asesoria'


