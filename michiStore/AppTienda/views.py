from django.shortcuts import render
from AppTienda.models import Producto


def inicio(request):
    return render(request, "index.html")


def nosotros(request):
    return render(request, "nosotros.html")


def productos(request):
    productos = Producto.objects.all()
    return render(request, "productos.html", {"productos": productos})


def contacto(request):
    return render(request, "contacto.html")
