from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context


# Create your views here.

@csrf_exempt
def show(request, recurso):
    estado = "<br>\n<br>\n"
    if request.user.is_authenticated():
        estado += "Eres " + request.user.username + "."
        estado += "<a href='/admin/logout/'>Logout</a>"
    else:
        estado += "No has hecho login. " + "<a href='/admin/'>Login</a>"
    fila = Pages.objects.filter(name=recurso)
    salida = ""
    found = 0
    if request.method == "GET":
        if not fila:
            salida += "Pagina no encontrada"
        else:
            salida += fila[0].page
            found = 1
    elif request.method == "PUT":
        if request.user.is_authenticated():
            if not fila:
                if recurso == "":
                    fila = Pages(name=recurso, page="Pagina principal")
                else:
                    fila = Pages(name=recurso, page="Pagina de " + recurso)
                fila.save()
                salida += fila.page
                found = 1
            else:
                salida += "Esta pagina ya esta almacenada"
                found = 1
        else:
            salida += "Solo usuarios registrados pueden " + \
                      "cambiar contenido"
            found = 1
    else:
        salida += "Metodo erroneo"
        
    if found:
        return HttpResponse(salida + estado)
    else:
        return HttpResponseNotFound(salida + estado)

@csrf_exempt
def show_annotated(request, recurso):
    estado = ""
    accion = ""
    enlace = ""
    if request.user.is_authenticated():
        estado += "Eres " + request.user.username + "."
        accion += "Logout"
        enlace += "/admin/logout/"
    else:
        estado += "No has hecho login. "
        accion += "Login"
        enlace += "/admin/"
    fila = Pages.objects.filter(name=recurso)
    salida = ""
    found = 0
    if request.method == "GET":
        if not fila:
            salida += "Pagina no encontrada"
        else:
            salida += fila[0].page
            found = 1
    elif request.method == "PUT":
        if request.user.is_authenticated():
            if not fila:
                if recurso == "":
                    fila = Pages(name=recurso, page="Pagina principal")
                else:
                    fila = Pages(name=recurso, page="Pagina de " + recurso)
                fila.save()
                salida += fila.page
                found = 1
            else:
                salida += "Esta pagina ya esta almacenada"
                found = 1
        else:
            salida += "Solo usuarios registrados pueden " + \
                      "cambiar contenido"
            found = 1
    else:
        salida += "Metodo erroneo"
        
    # 1. Indicar plantilla
    template = get_template("index.html")
    # 2. Marcar contexto -> contenido: salida
    c = Context({'contenido': salida, 
                 'estado': estado,
                 'accion': accion,
                 'enlace': enlace})
    # 3. Renderizar
    rendered = template.render(c)
    
    if found:
        return HttpResponse(rendered)
    else:
        return HttpResponseNotFound(rendered)
