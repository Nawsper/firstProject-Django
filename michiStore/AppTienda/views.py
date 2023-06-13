from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    return render(request, "index.html")


def nosotros(request):
    return render(request, "nosotros.html")


def productos(request):
    return render(request, "productos.html")


def contacto(request):
    return render(request, "contacto.html")


def busqueda_productos(request):
    return render(request, "busquedaProd.html")


def buscar(request):
    msj = "Articulo buscado: %r" % request.GET["prod"]
    return HttpResponse(msj)
