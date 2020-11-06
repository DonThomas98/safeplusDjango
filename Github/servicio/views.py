from django.shortcuts import render
from django.http import HttpResponse,request
from django.db import connection
import cx_Oracle
from datetime import datetime
def Home(request):
    data= {
        'clientes':listar_clientes(),
        'datosclientes':listar_datos_clientes(),
    }
    ##agregar_datos_clientes(123456789,150000,28,141) funcional
    ##agregar_clientes('perroson','elguason','Juan','Aguilera','jg@gmail.com',)
   

    return render(request,'home.html',data)


def Crear_clientes(request):

    if request.method == 'POST':
        password =request.POST.get('password')
        usuario =request.POST.get('usuario')
        nombre =request.POST.get('nombre')
        apellido =request.POST.get('apellido')
        correo =request.POST.get('correo')
        agregar_clientes(password,usuario,nombre,apellido,correo)
       

    return render(request,'nuevo_cliente.html')

def Crear_datos_clientes(request):
    data= {
        'datosclientes':listar_datos_clientes(),
    }
    if request.method == 'POST':
        rut =request.POST.get('rut')
        sueldo =request.POST.get('sueldo')
        edad =request.POST.get('edad')
        userid =request.POST.get('userid')
        agregar_datos_clientes(rut,sueldo,edad,userid)
       
    return render(request,'nuevo_datos_cliente.html',data)


def Crear_trabajadores(request):

    if request.method == 'POST':
        password =request.POST.get('password')
        usuario =request.POST.get('usuario')
        nombre =request.POST.get('nombre')
        apellido =request.POST.get('apellido')
        correo =request.POST.get('correo')
        agregar_trabajadores(password,usuario,nombre,apellido,correo)
    return render(request,'nuevo_trabajador.html')
       

def Crear_datos_trabajadores(request):
    data= {
        'datostrabajadores':listar_trabajadores(),
    }
    if request.method == 'POST':
        rut =request.POST.get('rut')
        sueldo =request.POST.get('sueldo')
        edad =request.POST.get('edad')
        userid =request.POST.get('userid')
        agregar_datos_trabajadores(rut,sueldo,edad,userid)
       
    return render(request,'nuevo_datos_trabajador.html',data)

def Crear_materiales_capacitacion(request):

    if request.method == 'POST':
        material =request.POST.get('material')
        agregar_materiales_capacitacion(material)
    return render(request,'nuevo_material_capacitacion.html')
       





def listar_clientes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("prc_listar_cliente",[out_cur])

    lista=[]
    for fila in out_cur:
        lista.append(fila)
    return lista

def listar_datos_clientes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("prc_listar_id_clientes",[out_cur])

    lista=[]
    for fila in out_cur:
        lista.append(fila)
    return lista

def listar_trabajadores():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("prc_listar_id_trabajadores",[out_cur])

    lista=[]
    for fila in out_cur:
        lista.append(fila)
    return lista


def agregar_clientes(password,usuario,nombre,apellido,correo):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("prc_insertar_cliente",[password,usuario,nombre,apellido,correo])


def agregar_datos_clientes(rut,sueldo,edad,userid):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("prc_insertar_datos_cliente",[rut,sueldo,edad,userid])


def agregar_trabajadores(password,usuario,nombre,apellido,correo):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("prc_insertar_trabajadores",[password,usuario,nombre,apellido,correo])


def agregar_datos_trabajadores(rut,sueldo,edad,userid):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("prc_insertar_datos_trabajador",[rut,sueldo,edad,userid])


def agregar_materiales_capacitacion(material):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("prc_insertar_materiales_capacitacion",[material])

