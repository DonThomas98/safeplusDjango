from django.shortcuts import render
from django.http import HttpResponse,request
from django.db import connection
import cx_Oracle
from datetime import datetime
def Home(request):
    data= {
        'clientes':listar_clientes()
    }
    ##agregar_clientes('perroson','elguason','Juan','Aguilera','jg@gmail.com',)
    if request.method == 'POST':
        password =request.POST.get('password')
        usuario =request.POST.get('usuario')
        nombre =request.POST.get('nombre')
        apellido =request.POST.get('apellido')
        correo =request.POST.get('correo')
        agregar_clientes(password,usuario,nombre,apellido,correo)
       

    return render(request,'home.html',data)


def listar_clientes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("prc_listar_cliente",[out_cur])

    lista=[]
    for fila in out_cur:
        lista.append(fila)
    return lista

def listar_trabajadores():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("prc_listar_trabajadores",[out_cur])

    lista=[]
    for fila in out_cur:
        lista.append(fila)
    return lista


def agregar_clientes(password,usuario,nombre,apellido,correo):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("prc_insertar_cliente",[password,usuario,nombre,apellido,correo])
