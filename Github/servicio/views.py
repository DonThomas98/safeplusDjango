from django.shortcuts import render
from django.http import HttpResponse,request
from django.db import connection


def Home(request):
    data= {
        'clientes':listar_clientes()
    }

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



