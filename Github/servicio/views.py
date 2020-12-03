from django.shortcuts import render
from django.http import HttpResponse,request
from django.db import connection
import cx_Oracle
from datetime import datetime
from django.utils import timezone
from django.shortcuts import redirect 
def Home(request):
    data= {

    }

    #data['mensaje'] = print(listado_accidentes_por_id(21))

    
    return render(request,'home.html')



##################### VISTAS Clientes , CASO USO 1      #############################
##########################################################################
def listado_clientes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("prc_listar_clientes",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def agregar_cliente(USERNAME,PASSWORD,FIRST_NAME,LAST_NAME,EMAIL):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('prc_insertar_cliente',[USERNAME,PASSWORD,FIRST_NAME,LAST_NAME,EMAIL,salida])
    return salida.getvalue()


def crear_cliente (request):

    data = {}

    if request.method == "POST":
        USERNAME = request.POST.get('USERNAME')
        PASSWORD =  request.POST.get('PASSWORD')
        FIRST_NAME = request.POST.get('FIRST_NAME')
        LAST_NAME = request.POST.get('LAST_NAME')
        EMAIL = request.POST.get('EMAIL')

        salida=agregar_cliente(USERNAME,PASSWORD,FIRST_NAME,LAST_NAME,EMAIL)

        if salida==1:
            data['mensaje'] = 'Se agrego el cliente de manera correcta'
            return redirect('extender_cliente')

        else:
            data['mensaje'] = 'No se creo un cliente nuevo'
    return render (request,'crear_cliente.html',data)


def agregar_cliente_datos(rut,sueldo,edad,user_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('prc_insertar_datos_cliente',[rut,sueldo,edad,user_id,salida])
    return salida.getvalue()



def extender_cliente (request):

    data= {
        'listado_clientes':listado_clientes()


    }
    if request.method == "POST":
        rut = request.POST.get('rut')
        sueldo =  request.POST.get('sueldo')
        edad = request.POST.get('edad')
        user_id = request.POST.get('user_id')

        salida=agregar_cliente_datos(rut,sueldo,edad,user_id)

        if salida==1:
            data['mensaje'] = 'Se agrego el cliente de manera correcta'

        else:
            data['mensaje'] = 'No se creo un cliente nuevo'
    return render (request,'extender_cliente.html',data)




def ver_accidentes_cliente_por_id(request):
    id_cliente = request.GET.get('id_cliente')
    data= {
        "listado_accidentes_por_id":listado_accidentes_por_id(id_cliente)
    }

    #data['mensaje'] = print(listado_accidentes_por_id(21))

    
    return render(request,'accidentes_por_id.html',data)




##############################################################################################################




##################### VISTAS TRABAJADOR ,  CASO USO 2      #############################
##########################################################################
def listado_trabajadores():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("prc_listar_trabajadores",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def agregar_trabajador(USERNAME,PASSWORD,FIRST_NAME,LAST_NAME,EMAIL):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('prc_insertar_trabajadores',[USERNAME,PASSWORD,FIRST_NAME,LAST_NAME,EMAIL,salida])
    return salida.getvalue()


def crear_trabajador (request):

    data = {}

    if request.method == "POST":
        USERNAME = request.POST.get('USERNAME')
        PASSWORD =  request.POST.get('PASSWORD')
        FIRST_NAME = request.POST.get('FIRST_NAME')
        LAST_NAME = request.POST.get('LAST_NAME')
        EMAIL = request.POST.get('EMAIL')

        salida=agregar_trabajador(USERNAME,PASSWORD,FIRST_NAME,LAST_NAME,EMAIL)

        if salida==1:
            data['mensaje'] = 'Se agrego el trabajador de manera correcta'
            return redirect('extender_trabajador')

        else:
            data['mensaje'] = 'No se creo un trabajador nuevo'
    return render (request,'crear_trabajador.html',data)

def agregar_trabajador_datos(rut,sueldo,edad,user_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('prc_insertar_datos_trabajador',[rut,sueldo,edad,user_id,salida])
    return salida.getvalue()



def extender_trabajador (request):

    data= {
        'listado_trabajadores':listado_trabajadores()
    }

    if request.method == "POST":
        rut = request.POST.get('rut')
        sueldo =  request.POST.get('sueldo')
        edad = request.POST.get('edad')
        user_id = request.POST.get('user_id')

        salida=agregar_trabajador_datos(rut,sueldo,edad,user_id)

        if salida==1:
            data['mensaje'] = 'Se agrego el trabajador extendido de manera correcta'

        else:
            data['mensaje'] = 'No se pudo añadir datos al trabajador'
    return render (request,'extender_trabajador.html',data)


##################### VISTAS CAPACITACION ,  CASO USO 3   , faltan los materiales   #############################
##########################################################################

def listado_trabajadores_extendidos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("prc_listar_trabajadores_extendidos",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def listado_clientes_extendidos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("prc_listar_clientes_extendidos",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_dia_capacitacion():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("prc_mostrar_dia_capacitacion",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def agregar_capacitacion(HORA_CAPACITACION,RUT_CLIENTE_ID,RUT_TRABAJADOR_ID):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('prc_insertar_capacitacion',[HORA_CAPACITACION,RUT_CLIENTE_ID,RUT_TRABAJADOR_ID,salida])
    return salida.getvalue()


def nueva_capacitacion (request):

    data= {
        'listado_clientes_extendidos':listado_clientes_extendidos(),
        'listado_trabajadores_extendidos':listado_trabajadores_extendidos(),
        'listado_dia_capacitacion':listado_dia_capacitacion(),

    }

    if request.method == "POST":
        HORA_CAPACITACION = request.POST.get('HORA_CAPACITACION')
        RUT_CLIENTE_ID =  request.POST.get('RUT_CLIENTE_ID')
        RUT_TRABAJADOR_ID = request.POST.get('RUT_TRABAJADOR_ID')

        salida=agregar_capacitacion(HORA_CAPACITACION,RUT_CLIENTE_ID,RUT_TRABAJADOR_ID)

        if salida==1:
            data['mensaje'] = 'La capacitacion fue agendada correctamente'

        else:
            data['mensaje'] = 'No se pudo Agendar la capacitacion'
    return render (request,'nueva_capacitacion.html',data)

#################VISTAS DE MATERIALES A USAR EN LA CAPACITACION


def agregar_materiales(material):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('prc_insertar_materiales',[material,salida])
    return salida.getvalue()

def nuevos_materiales(request):

    data= {

        'listado_materiales':listado_materiales()
    }

    if request.method == "POST":
        material = request.POST.get('material')
        salida=agregar_materiales(material)

        if salida==1:
            data['mensaje'] = 'Los materiales se agregaron de manera correcta'

        else:
            data['mensaje'] = 'No se pudo agregar materiales nuevos'
    return render (request,'nuevo_material.html',data)

def listado_materiales():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("prc_listar_material",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista



def listado_capacitaciones(rut_trabajador_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("prc_listar_capacitaciones",[out_cur,rut_trabajador_id])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def agregar_materiales_solicitados(id_material,cantidad,material_capacitacion_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('prc_insertar_materiales_solicitados',[id_material,cantidad,material_capacitacion_id,salida])
    return salida.getvalue()

def nuevos_materiales_solicitados(request):
    username = request.user.id    
    data= {
        'listado_materiales':listado_materiales(),
        'listado_capacitaciones':listado_capacitaciones(username),
    }

    if request.method == "POST":
        id_material = request.POST.get('id_material')
        cantidad = request.POST.get('cantidad')
        material_capacitacion_id = request.POST.get('material_capacitacion_id')
        salida=agregar_materiales_solicitados(id_material,cantidad,material_capacitacion_id)

        if salida==1:
            data['mensaje'] = 'Los materiales se agregaron de manera correcta'

        else:
            data['mensaje'] = 'No se pudo vincular materiales con la capacitacion'
    return render (request,'nuevo_material_solicitado.html',data)



##################### VISTAS VISITA TERRENO ,  CASO USO 4      #############################
##########################################################################


def agregar_visita_rutinaria(motivo_visita,fecha_visita,rut_cliente_id, rut_trabajador_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('prc_insertar_visita',[motivo_visita,fecha_visita,rut_cliente_id, rut_trabajador_id,salida])
    return salida.getvalue()





def nueva_visita_rutinaria (request):
    data= {
        'listado_clientes_extendidos':listado_clientes_extendidos(),
        'listado_trabajadores_extendidos':listado_trabajadores_extendidos(),

    }

    if request.method == "POST":
        motivo_visita = request.POST.get('motivo_visita')
        fecha_visita = request.POST.get('fecha_visita')
        rut_cliente_id = request.POST.get('rut_cliente_id')
        rut_trabajador_id = request.POST.get('rut_trabajador_id')

        salida=agregar_visita_rutinaria(motivo_visita,fecha_visita,rut_cliente_id, rut_trabajador_id)

        if salida==1:
            data['mensaje'] = 'La visita fue agendada correctamente'

        else:
            data['mensaje'] = 'No se pudo Agendar la visita'
    return render (request,'nuevo_visita_rutinaria.html',data)

def listado_visitas_sin_extender(rut):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()
    cursor.callproc("prc_listar_visitas_sin_extender",[out_cur,rut])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


##################### VISTAS REVISAR CLIENTE ,  CASO USO 5     #############################
##########################################################################
##ESTA FUNCION LISTA LOS DISTINTOS ACCIDENTES-ASESORIAS QUE SE LE HAN REALIZADO A UN CLIENTE
def listado_clientes_con_modulos(request):
    id_cliente = request.GET.get('id_cliente')
    id_accidente_id = request.GET.get('id_accidente_id')


    data= {
        "listado_accidentes_por_id":listado_accidentes_por_id(id_cliente),
        "listado_clientes_extendidos":listado_clientes_extendidos(),
        "listado_asesorias_por_id_accidente":listado_asesorias_por_id_accidente(id_accidente_id)
    }

    

    
    return render(request,'listar_clientes.html',data)










##################### VISTAS REPORTAR ACCIDENTE CLIENTE ,  CASO USO 6      #############################
##########################################################################


def agregar_accidente(naturaleza,partes_accidentadas,fuente_accidente,fecha_accidente,rut_cliente_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('prc_reportar_accidente',[naturaleza,partes_accidentadas,fuente_accidente,fecha_accidente,rut_cliente_id,salida])
    return salida.getvalue()

def nuevo_accidente (request):
    data= {
        'listado_clientes_extendidos':listado_clientes_extendidos(),

    }

    if request.method == "POST":
        naturaleza = request.POST.get('naturaleza')
        partes_accidentadas = request.POST.get('partes_accidentadas')
        fuente_accidente = request.POST.get('fuente_accidente')
        fecha_accidente = request.POST.get('fecha_accidente')
        rut_cliente_id = request.POST.get('rut_cliente_id')

        salida=agregar_accidente(naturaleza,partes_accidentadas,fuente_accidente, fecha_accidente,rut_cliente_id)

        if salida==1:
            data['mensaje'] = 'El accidente se reporto de manera exitosa'

        else:
            data['mensaje'] = 'El accidente no se pudo ingresar'
    return render (request,'nuevo_accidente.html',data)


def listado_accidentes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("prc_listar_accidentes",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def listado_accidentes_por_id(v_rut_cliente_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("prc_listar_accidentes_por_id",[out_cur,v_rut_cliente_id])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista




##################### VISTAS REPORTAR FISCALIZACION ESPECIAL CLIENTE       #############################
##########################################################################

def agregar_fiscalizacion(doc_revisados,descripcion_documento,documento,rut_cliente_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('prc_insertar_fiscalizacion',[doc_revisados,descripcion_documento,documento,rut_cliente_id,salida])
    return salida.getvalue()

def nueva_fiscalizacion (request):
    data= {
        'listado_clientes_extendidos':listado_clientes_extendidos(),

    }

    if request.method == "POST":
        doc_revisados = request.POST.get('doc_revisados')
        descripcion_documento = request.POST.get('descripcion_documento')
        documento = request.POST.get('documento')
        rut_cliente_id = request.POST.get('rut_cliente_id')

        salida=agregar_fiscalizacion(doc_revisados,descripcion_documento,documento,rut_cliente_id)

        if salida==1:
            data['mensaje'] = 'Se reporto la fiscalizacion de manera exitosa'

        else:
            data['mensaje'] = 'La fiscalizacion no se pudo reportar'
    return render (request,'nueva_fiscalizacion.html',data)


def listado_fiscalizaciones():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("prc_listar_fiscalizaciones",[out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


##################### VISTAS  CREAR CASO ASESORIA  ACCIDENTE,  CASO USO 7     #############################
##########################################################################




def agregar_asesoria_accidente(propuesta,id_accidente_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('prc_insertar_asesoria_accidente',[propuesta,id_accidente_id,salida])
    return salida.getvalue()


def nueva_asesoria_accidente (request):
    data= {
        'listado_accidentes':listado_accidentes(),

    }

    if request.method == "POST":
        propuesta = request.POST.get('propuesta')
        id_accidente_id = request.POST.get('id_accidente_id')


        salida=agregar_asesoria_accidente(propuesta,id_accidente_id)

        if salida==1:
            data['mensaje'] = 'Se ingreso exitosamente la asesoria '

        else:
            data['mensaje'] = 'No se pudo ingresar la asesoria'
    return render (request,'nueva_asesoria_accidente.html',data)


def listado_asesorias_por_id_accidente(id_accidente_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("prc_listar_asesorias_por_id_accidente",[out_cur,id_accidente_id])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista



def ver_asesorias_por_id_accidente(request):
    id_accidente_id = request.GET.get('id_accidente_id')
    data= {
        "listado_asesorias_por_id_accidente":listado_asesorias_por_id_accidente(id_accidente_id)
    }

    #data['mensaje'] = print(listado_accidentes_por_id(21))

    
    return render(request,'asesoria_por_id_accidente.html',data)

##################### VISTAS  CREAR CASO ASESORIA  FISCALIZACION,  CASO USO 7     #############################
##########################################################################



def agregar_asesoria_fiscalizaciones(propuesta,id_fiscalizacion_id ):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('prc_insertar_asesoria_fiscalizacion',[propuesta,id_fiscalizacion_id,salida])
    return salida.getvalue()


def nueva_asesoria_fiscalizaciones (request):
    data= {
        'listado_fiscalizaciones':listado_fiscalizaciones(),

    }

    if request.method == "POST":
        propuesta = request.POST.get('propuesta')
        id_fiscalizacion_id = request.POST.get('id_fiscalizacion_id')


        salida=agregar_asesoria_fiscalizaciones(propuesta,id_fiscalizacion_id)

        if salida==1:
            data['mensaje'] = 'Se ingreso exitosamente la asesoria '

        else:
            data['mensaje'] = 'No se pudo ingresar la asesoria'
    return render (request,'nueva_asesoria_fiscalizacion.html',data)



##################### VISTAS  CREAR CASO REVISAR MEJORA ,  CASO USO 8   #############################
##########################################################################
##FALTA QUE FILTRE LAS VISITAS POR LA ID DEL TRABAJADOR
def agregar_informe_visita(introduccion,RESULTADOS_EVALUACION,AUTOEVALUACION,DOC_ACTUALIZADOS,REG_INTERNO,
    DOC_SEREMI_TRABAJO,COPIA_DOCUMENTOS,INFORMA_RIESGOS,INFORMA_MEDIDAS,PROGRAMA_ORDEN,EXTINTORES,CAPACITACION_EXTINTOR,EPP_INVENTARIO,
    EPP_CERTIFICADOS,ID_VISITA_ID ):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)

    cursor.callproc('prc_insertar_informe_visita',[introduccion,RESULTADOS_EVALUACION,AUTOEVALUACION,DOC_ACTUALIZADOS,REG_INTERNO,
    DOC_SEREMI_TRABAJO,COPIA_DOCUMENTOS,INFORMA_RIESGOS,INFORMA_MEDIDAS,PROGRAMA_ORDEN,EXTINTORES,CAPACITACION_EXTINTOR,EPP_INVENTARIO,
    EPP_CERTIFICADOS,ID_VISITA_ID,salida])


    return salida.getvalue()


def nuevo_informe_visita (request):
    current_user = request.user
    data= {
        'listado_visitas_sin_extender':listado_visitas_sin_extender(current_user.id),

    }

    if request.method == "POST":
        introduccion = request.POST.get('introduccion')
        RESULTADOS_EVALUACION = request.POST.get('RESULTADOS_EVALUACION')
        AUTOEVALUACION = request.POST.get('AUTOEVALUACION')
        DOC_ACTUALIZADOS = request.POST.get('DOC_ACTUALIZADOS')
        REG_INTERNO = request.POST.get('REG_INTERNO')
        DOC_SEREMI_TRABAJO = request.POST.get('DOC_SEREMI_TRABAJO')
        COPIA_DOCUMENTOS = request.POST.get('COPIA_DOCUMENTOS')
        INFORMA_RIESGOS = request.POST.get('INFORMA_RIESGOS')
        INFORMA_MEDIDAS = request.POST.get('INFORMA_MEDIDAS')
        PROGRAMA_ORDEN = request.POST.get('PROGRAMA_ORDEN')
        EXTINTORES = request.POST.get('EXTINTORES')
        CAPACITACION_EXTINTOR = request.POST.get('CAPACITACION_EXTINTOR')
        EPP_INVENTARIO = request.POST.get('EPP_INVENTARIO')
        EPP_CERTIFICADOS = request.POST.get('EPP_CERTIFICADOS')
        ID_VISITA_ID = request.POST.get('ID_VISITA_ID')

        salida=agregar_informe_visita(introduccion,RESULTADOS_EVALUACION,AUTOEVALUACION,DOC_ACTUALIZADOS,REG_INTERNO,
        DOC_SEREMI_TRABAJO,COPIA_DOCUMENTOS,INFORMA_RIESGOS,INFORMA_MEDIDAS,PROGRAMA_ORDEN,EXTINTORES,CAPACITACION_EXTINTOR,EPP_INVENTARIO,
        EPP_CERTIFICADOS,ID_VISITA_ID)

        if salida==1:
            data['mensaje'] = 'Se ingreso exitosamente la asesoria '

        else:
            data['mensaje'] = 'No se pudo ingresar la asesoria'
    return render (request,'nuevo_informe_visita.html',data)


###CASO PAGOS



def contratos_por_id_pago(v_rut_cliente_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur=django_cursor.connection.cursor()

    cursor.callproc("prc_listar_contratos_por_id_pagos",[out_cur,v_rut_cliente_id])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def agregar_pago_cliente(monto_pago,fecha_pago,id_contrato_id ):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('prc_insertar_pago',[monto_pago,fecha_pago,id_contrato_id])
    return salida.getvalue()


def nuevo_registro_pagos(request):
    current_user = request.user
    usuario= current_user.id
    data= {
        'contratos_por_id_pago':contratos_por_id_pago(usuario),
    }

    if request.method == "POST":
        monto_pago = request.POST.get('monto_pago')
        fecha_pago = request.POST.get('fecha_pago')
        id_contrato_id = request.POST.get('id_contrato_id')
        


        agregar_pago_cliente(monto_pago,fecha_pago,id_contrato_id)

    return render (request,'nuevo_pago.html',data)

