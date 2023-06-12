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
